# Generated 2026-11-13 - freecad_roundtrip.py (0.1.0)
"""Round trip of a STEP file through FreeCAD: read what the file declares, import it, export it, import it again.

In FreeCAD:  Macro > Macros... > select this file > Execute. Two dialogs ask for the STEP file and for the report.
Headless:    ROUNDTRIP_STEP=<file.step> ROUNDTRIP_OUT=<report.txt> freecadcmd tools/freecad_roundtrip.py

Optional:    ROUNDTRIP_KEEP=<file.FCStd>     save the imported document

The report compares the products the file declares with the tree FreeCAD builds - bodies, containers, labels,
solids, volumes - and shows what changes when FreeCAD writes the file again. It records observations and makes
no statement of conformity.
"""
import collections
import datetime
import os
import re
import tempfile

import FreeCAD
import Import
import Part

RELATIVE = 1e-6                                   # volumes agree within this relative difference


def declared(path):
    """What the file declares: product names, the names that are assemblies, and solids per leaf product."""
    with open(path, encoding="utf-8", errors="replace") as handle:
        text = re.sub(r"\s+", " ", handle.read())
    schema = re.search(r"FILE_SCHEMA\s*\(\s*\(\s*'([^']*)'", text)
    entity = {int(m[1]): (m[2], m[3]) for m in re.finditer(r"#(\d+)\s*=\s*([A-Z_0-9]+)\s*\((.*?)\)\s*;", text)}
    refs = lambda arguments: [int(x) for x in re.findall(r"#(\d+)", re.sub(r"'[^']*'", "", arguments))]  # not the # of a name
    first = lambda kind: {i: refs(a)[0] for i, (k, a) in entity.items() if k.startswith(kind) and refs(a)}
    product = {i: re.match(r"\s*'([^']*)'", a)[1] for i, (k, a) in entity.items() if k == "PRODUCT"}
    formation, definition = first("PRODUCT_DEFINITION_FORMATION"), {
        i: refs(a)[0] for i, (k, a) in entity.items() if k == "PRODUCT_DEFINITION" and refs(a)}
    name = {i: product[formation[f]] for i, f in definition.items() if formation.get(f) in product}
    usages = [refs(a) for k, a in entity.values() if k == "NEXT_ASSEMBLY_USAGE_OCCURRENCE"]
    assemblies = {name[r[0]] for r in usages if len(r) > 1 and r[0] in name}

    shape_of = {i: refs(a)[0] for i, (k, a) in entity.items() if k == "PRODUCT_DEFINITION_SHAPE" and refs(a)}
    representation = {refs(a)[0]: refs(a)[1] for k, a in entity.values()
                      if k == "SHAPE_DEFINITION_REPRESENTATION" and len(refs(a)) > 1}
    related = collections.defaultdict(list)
    for kind, arguments in entity.values():
        if kind == "SHAPE_REPRESENTATION_RELATIONSHIP" and len(refs(arguments)) > 1:
            a, b = refs(arguments)[:2]
            related[a].append(b)
            related[b].append(a)

    def solids(rep, seen):
        if rep in seen or rep not in entity:
            return 0
        seen.add(rep)
        own = sum(1 for x in refs(entity[rep][1]) if entity.get(x, ("",))[0] == "MANIFOLD_SOLID_BREP")
        return own + sum(solids(other, seen) for other in related[rep])

    per_leaf = {}
    for shape, pd in shape_of.items():
        if pd in name and name[pd] not in assemblies and shape in representation:
            per_leaf[name[pd]] = solids(representation[shape], set())
    return {"schema": schema.group(1).strip() if schema else "not found", "names": set(product.values()),
            "assemblies": assemblies, "leaves": set(product.values()) - assemblies,
            "several": {n: c for n, c in sorted(per_leaf.items()) if c > 1}}


def global_shape(obj):
    """The shape of an object placed in the frame of the document."""
    shape = obj.Shape.copy()
    try:
        shape.Placement = obj.getGlobalPlacement()
    except Exception:                             # older versions: the local placement is the best available
        pass
    return shape


def inventory(path, name):
    """Import a STEP file into a new document. Return (document, container labels, bodies by label)."""
    doc = FreeCAD.newDocument(name)
    Import.insert(path, doc.Name)
    doc.recompute()
    containers, bodies = [], collections.defaultdict(list)
    for obj in doc.Objects:
        if obj.TypeId in ("App::Part", "App::LinkGroup"):
            containers.append(obj.Label)
        elif obj.isDerivedFrom("Part::Feature") and not obj.Shape.isNull():
            shape = global_shape(obj)
            box = shape.BoundBox
            bodies[obj.Label].append({
                "solids": len(shape.Solids), "volume": shape.Volume, "kind": shape.ShapeType,
                "box": (box.XMin, box.XMax, box.YMin, box.YMax, box.ZMin, box.ZMax)})
    return doc, sorted(containers), dict(bodies)


def envelope(bodies):
    boxes = [item["box"] for items in bodies.values() for item in items]
    return tuple(round((min if i % 2 == 0 else max)(box[i] for box in boxes), 3) for i in range(6)) if boxes else None


def short(values, limit=12):
    values = list(values)
    return values if len(values) <= limit else values[:limit] + [f"and {len(values) - limit} more"]


def run(step, out, keep=None):
    lines, counts = [], {"PASS": 0, "FAIL": 0, "INFO": 0}

    def say(kind, label, expected, actual):
        counts[kind] += 1
        lines.append(f"[{kind}] {label}: expected {expected} | actual {actual}")

    def hold(label, expected, actual):
        say("PASS" if expected == actual else "FAIL", label, expected, actual)

    stem = os.path.splitext(os.path.basename(step))[0]
    file = declared(step)
    doc, sets, bodies = inventory(step, "RoundTripA")
    count = sum(len(items) for items in bodies.values())
    volume = sum(item["volume"] for items in bodies.values() for item in items)

    lines.append("== A | the tree FreeCAD builds against the products the file declares ==")
    hold("bodies shown, against leaf products declared", len(file["leaves"]), count)
    hold("containers shown, against assemblies declared", len(file["assemblies"]), len(sets))
    hold("labels shown that the file does not declare", [], short(sorted((set(bodies) | set(sets)) - file["names"])))
    moved = sorted((file["assemblies"] - set(sets)) | (file["leaves"] - set(bodies)))
    hold("declared names shown on another kind of object, or not shown", [], short(moved))
    hold("labels carried by more than one object", [], short(sorted(
        label for label, n in collections.Counter(list(sets) + [b for b, i in bodies.items() for _ in i]).items() if n > 1)))
    hold("bodies that are not solids", [], short(sorted(
        f"{label} ({item['kind']})" for label, items in bodies.items() for item in items if not item["solids"])))
    say("INFO", "leaf products that hold more than one solid in the file", "listed", file["several"] or "none")
    say("INFO", "solids inside the bodies shown", "counted",
        sum(item["solids"] for items in bodies.values() for item in items))
    say("INFO", "total volume (mm3)", "computed", round(volume, 1))
    say("INFO", "envelope xmin xmax ymin ymax zmin zmax (mm)", "computed", envelope(bodies))

    exported = os.path.join(tempfile.mkdtemp(prefix="roundtrip-"), stem + "_from-freecad.step")
    Import.export([obj for obj in doc.Objects if not obj.InList], exported)
    if keep:
        doc.saveAs(keep)
    doc2, sets2, bodies2 = inventory(exported, "RoundTripB")

    lines += ["", "== B | what changes when FreeCAD writes the file again =="]
    say("INFO", "FILE_SCHEMA", file["schema"], declared(exported)["schema"])
    hold("body labels kept", True, sorted(bodies) == sorted(bodies2))
    hold("container labels kept", True, sets == sets2)
    hold("bodies shown", count, sum(len(items) for items in bodies2.values()))
    drift = []
    for label in sorted(set(bodies) & set(bodies2)):
        a, b = sum(i["volume"] for i in bodies[label]), sum(i["volume"] for i in bodies2[label])
        if abs(a - b) > RELATIVE * max(abs(a), 1.0):
            drift.append((label, round(a, 3), round(b, 3)))
    hold("bodies whose volume changed", [], short(drift))
    hold("envelope kept", envelope(bodies), envelope(bodies2))
    say("INFO", "file size (bytes)", os.path.getsize(step), os.path.getsize(exported))
    for document in (doc, doc2):
        FreeCAD.closeDocument(document.Name)

    version = ".".join(str(part) for part in FreeCAD.Version()[:3])
    head = [
        "=" * 78,
        f" {stem}  --  round trip through FreeCAD",
        f" FreeCAD {version} | Open CASCADE {Part.OCC_VERSION} | freecad_roundtrip.py 0.1.0",
        f" run: {datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')} | interface: "
        f"{'yes' if FreeCAD.GuiUp else 'no'}",
        "=" * 78, ""]
    tail = ["", f"RESULT: {counts['PASS']} PASS | {counts['FAIL']} FAIL | {counts['INFO']} INFO"]
    text = "\n".join(head + lines + tail) + "\n"
    with open(out, "w", encoding="utf-8") as handle:
        handle.write(text)
    return text


def ask():
    """Paths from the environment or, with the interface up, from two dialogs."""
    step, out = os.environ.get("ROUNDTRIP_STEP"), os.environ.get("ROUNDTRIP_OUT")
    if not step and FreeCAD.GuiUp:
        try:
            from PySide import QtWidgets as dialogs
        except ImportError:
            from PySide import QtGui as dialogs
        step = dialogs.QFileDialog.getOpenFileName(None, "STEP file to check", "", "STEP (*.step *.stp)")[0]
        if step:
            folder = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(step))), "evidence")
            folder = folder if os.path.isdir(folder) else os.path.dirname(step)
            suggestion = os.path.join(folder, os.path.splitext(os.path.basename(step))[0] + "_freecad-roundtrip.txt")
            out = dialogs.QFileDialog.getSaveFileName(None, "Report", suggestion, "Text (*.txt)")[0]
    return step, out


STEP, OUT = ask()
if STEP and OUT:
    REPORT = run(STEP, OUT, os.environ.get("ROUNDTRIP_KEEP"))
    FreeCAD.Console.PrintMessage(REPORT + f"\nReport written to {OUT}\n")
else:
    FreeCAD.Console.PrintError("freecad_roundtrip: no STEP file or no report path given\n")
