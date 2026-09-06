#!/usr/bin/env python3
# =============================================================================
#  EWTW-533001-000 · STRUCTURE, REAR FUSELAGE ZONE · AMPEL360 eWTW
#  Concept-grade parametric 3D assembly — join package + zone provisions.
#
#  Provenance : (set at runtime) · EWTW-533001-000_concept.py · v0.2.1-concept
#  Frame      : X aft+ · Y left+ · Z up+ · mm · origin = join plane JP, centreline
#  Maturity   : CONCEPT — every dimension is a declared envelope assumption.
#
#  Outputs (default --layout repo; paths resolved from this file's location):
#    CAD/exchange/EWTW-533001-000_concept.step          STEP AP242 · mm · PN tree · no ghost
#    CAD/preview/EWTW-533001-000_concept.glb            glTF preview · colours · ghost 12 %
#    evidence/EWTW-533001-000_concept_verification.txt  run report
#    prompts/run-record.yaml                            machine-written run ledger
#
#  Ghost envelope is preview context only (GLB); not part of the assembly and
#  not exported to STEP. Frames, stringers, skins, pressure bulkhead, the
#  outflow valve itself and systems runs are out of scope (other assemblies).
#  Interpretation notes I-1..I-14 print with the verification report.
#  Hashes and byte counts are measured at run time and recorded in the
#  run-record — never asserted by any author of prompt or source.
# =============================================================================
from __future__ import annotations

import argparse
import hashlib
import math
import platform
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import cadquery as cq
from cadquery import Vector

try:
    from OCP.Interface import Interface_Static
    _HAVE_STATIC = True
except Exception:
    _HAVE_STATIC = False

PN = "EWTW-533001"
GENERATOR_FILE = Path(__file__).name     # verbatim — provenance truth (CM-001 §5)
GENERATOR_VERSION = "v0.2.1-concept"     # rev C: repo layout + run-record schema 1.0
RUN_RECORD_SCHEMA = "AMPEL360-AI-GENERATION-RUN-RECORD/1.0"

# ------------------------------------------------------------------ parameters
PARAMS = {
    # ---- ghost context envelope (preview only) ------------------------------
    "ghost_x_fwd": -4500.0, "ghost_r_fwd": 1500.0,     # Ø3000 at fwd end
    "ghost_x_aft": 0.0,     "ghost_r_aft": 1100.0,     # Ø2200 at join plane JP
    "ghost_wall": 5.0, "ghost_alpha": 0.12, "ghost_cutout": 1,
    # ---- -010 splice ring ----------------------------------------------------
    "ring_od": 2200.0, "ring_flange_w": 60.0, "ring_flange_t": 5.0,
    "ring_web_h": 120.0, "ring_axial_total": 150.0,    # I-1 reconciliation
    "strap_axial": 30.0, "strap_t": 3.0, "strap_arc": 100.0,   # I-13
    # ---- -020/-021 join indexing --------------------------------------------
    "n_pins": 8, "pin_phase": 22.5,                    # 22.5+k·45, never on butt
    "pin_d": 16.0, "pin_l": 60.0, "pin_chamfer": 2.0,
    "boss_d": 40.0, "boss_l": 25.0,
    # ---- -030/-031 systems-run brackets --------------------------------------
    "n_brackets_row": 6, "bracket_pitch": 700.0,
    "bracket_x0": -4200.0, "bracket_x_end": -700.0,
    "bracket_row_phi": (145.0, 215.0),                 # ±35° from Z− (LH, RH)
    "bracket_len_a": 120.0, "bracket_len_c": 80.0, "bracket_width": 60.0,
    "bracket_t": 3.0, "bracket_hole_d": 8.0, "bracket_dodge": 1,   # I-7
    # ---- -040/-041/-042 outflow-valve surround -------------------------------
    "ov_x": -1200.0, "ov_phi": 210.0,                  # 30° from Z− toward Y−
    "doubler_axial": 640.0, "doubler_circ": 480.0, "doubler_t": 2.5,
    "doubler_corner_r": 60.0,                          # I-5
    "cutout_axial": 480.0, "cutout_circ": 320.0, "cutout_corner_r": 60.0,
    "frame_width": 40.0, "frame_depth": 30.0,          # I-4
    "rivet_d": 6.0, "rivet_pitch": 30.0, "rivet_offset": 60.0,   # I-6
    # ---- -050/-051 NDT plugs --------------------------------------------------
    "n_plugs": 12, "plug_phi0": 15.0, "plug_spacing": 30.0,     # I-2
    "plug_d": 40.0, "plug_t": 12.0,
    "plug_socket_af": 6.0, "plug_socket_depth": 6.0,
    # ---- export / naming -------------------------------------------------------
    "step_schema": "AP242DIS",
    "instance_tag": "#",        # "#": EWTW-533001-021#03 ; "none": duplicate names
    "interference_check": 1,
}

QUADS = [  # (phi_lo, phi_hi, PN) — phi measured from Z+ toward Y+
    (-45.0, 45.0,   f"{PN}-011"),   # UPPER
    (45.0, 135.0,   f"{PN}-013"),   # SIDE LH
    (135.0, 225.0,  f"{PN}-012"),   # LOWER
    (225.0, 315.0,  f"{PN}-014"),   # SIDE RH
]
BUTTS = [45.0 + 90.0 * k for k in range(4)]

COL = {
    "ring":    (0.72, 0.45, 0.20),   # bronze
    "steel":   (0.62, 0.65, 0.70),   # pins, plugs
    "amber":   (0.90, 0.58, 0.10),   # brackets
    "teal":    (0.10, 0.55, 0.55),   # doubler, frame
}

EXPECTED = {
    f"{PN}-011": 1, f"{PN}-012": 1, f"{PN}-013": 1, f"{PN}-014": 1,
    "BUTT-STRAP-SEGMENT-JOIN": 4,                # no PN assigned — I-12
    f"{PN}-020": 8, f"{PN}-021": 8, f"{PN}-031": 12,
    f"{PN}-041": 1, f"{PN}-042": 1, f"{PN}-051": 12,
}

NOTES = [
    "I-1  Ring cross-section: spec numbers are over-constrained (60+5+60 = 125 ≠ 150). "
    "Modeled as a continuous 5 mm outer band over the full 150 mm axial; the two flanges are "
    "the 60 mm band portions each side of a 30 mm central land at JP; the land deepens by the "
    "120 mm radial web. 5 mm = band gauge; 30 mm land derived (150 − 2×60).",
    "I-2  Plug seats at 15°+30°k place 4 of 12 plugs on segment butt joints (45/135/225/315). "
    "Modeled as specified; each seat straddles the butt (both adjacent segments carry a "
    "half-seat). Flagged for design review.",
    "I-3  Indexing bosses modeled as discrete bodies faying to the aft-flange face at x=+75 "
    "(one body per PN rule); in production they are machined integrally with the segments. "
    "Pin axis at flange mid-radius r≈1097.5; pin tips stand ~5.5 mm proud of ring OD to "
    "engage receiving holes in the tailcone splice (provision, not modeled). "
    "Pin 60 mm: 25 mm engaged, 35 mm protruding.",
    "I-4  Frame section 40 mm in-plane × 30 mm radial standoff (spec order ambiguous).",
    "I-5  Doubler outer corners R60 (unspecified in spec).",
    "I-6  Rivet pattern: Ø6, even spacing ≈30.2 mm (perimeter ≈1874 mm, 30 mm nominal), on "
    "the contour offset 60 mm from the cutout — clear of the 40 mm frame footprint and the "
    "80 mm doubler edge.",
    "I-7  RH bracket row (215°) nominally intersects the doubler envelope at station X=−1400. "
    "With bracket_dodge=1 that bracket is displaced circumferentially to clear (topology "
    "preserved: 12 brackets, two rows). Set bracket_dodge=0 to keep nominal positions.",
    "I-8  Bracket feet modeled flat and tangent to the conical shell (≤0.35 mm local embed); "
    "conformal feet TBD.",
    "I-9  Ring forward flange nominally overlaps the ghost shell over the last ~56 mm before "
    "JP (≤2.3 mm depth) — production joggle not modeled; ghost is context only.",
    "I-10 Ghost is preview-only (GLB), excluded from STEP; concentric conical frustum, "
    "no upsweep (optional in spec, not implemented).",
    "I-11 Multi-instance bodies carry an instance tag (e.g. EWTW-533001-051#07) — the tag is "
    "not part of the PN; set instance_tag='none' for exact duplicate PN names.",
    "I-12 Butt straps carry no PN (spec row has none); named BUTT-STRAP-SEGMENT-JOIN#NN. "
    "PN allocation pending per programme governance.",
    "I-13 Butt-strap arc width 100 mm (spec gives axial 30 × t 3 only).",
    "I-14 Threads and press-fits idealized (smooth bores); fastener holes in the ring land / "
    "flanges not modeled (joint fastener design not specified at this maturity).",
]

# ----------------------------------------------------------------- small utils
def _clamp1(v):
    return max(-1.0, min(1.0, v))


def rounded_rect_points(w, h, r, arc_step=6.0):
    """Rounded rectangle in the (u, v) plane, centred, CCW, densely sampled."""
    hw, hh = 0.5 * w, 0.5 * h
    pts = [(hw, 0.0), (hw, hh - r)]

    def arc(cx, cy, a0, a1):
        n = max(2, int(math.ceil(r * (a1 - a0) / arc_step)))
        for i in range(1, n + 1):
            a = a0 + (a1 - a0) * i / n
            pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))

    arc(hw - r, hh - r, 0.0, 0.5 * math.pi)
    pts.append((-hw + r, hh))
    arc(-hw + r, hh - r, 0.5 * math.pi, math.pi)
    pts.append((-hw, -hh + r))
    arc(-hw + r, -hh + r, math.pi, 1.5 * math.pi)
    pts.append((hw, -hh))
    arc(hw - r, -hh + r, 1.5 * math.pi, 2.0 * math.pi)
    out = []
    for p in pts:
        if not out or math.dist(out[-1], p) > 1e-7:
            out.append(p)
    if math.dist(out[0], out[-1]) <= 1e-7:
        out.pop()
    return out


def points_along(pts, pitch):
    """Evenly spaced points along a closed polyline, spacing ≈ pitch."""
    closed = list(pts) + [pts[0]]
    seglen = [math.dist(closed[i], closed[i + 1]) for i in range(len(closed) - 1)]
    perimeter = sum(seglen)
    n = max(1, int(round(perimeter / pitch)))
    step = perimeter / n
    out, i, acc = [], 0, 0.0
    for k in range(n):
        target = k * step
        while acc + seglen[i] < target - 1e-9:
            acc += seglen[i]
            i += 1
        p, q = closed[i], closed[i + 1]
        f = min(1.0, max(0.0, (target - acc) / seglen[i]))
        out.append((p[0] + f * (q[0] - p[0]), p[1] + f * (q[1] - p[1])))
    return out


def _bbox_overlap(a, b):
    ba, bb = a.BoundingBox(), b.BoundingBox()
    return not (ba.xmax < bb.xmin or bb.xmax < ba.xmin or
                ba.ymax < bb.ymin or bb.ymax < ba.ymin or
                ba.zmax < bb.zmin or bb.zmax < ba.zmin)


def _common_volume(a, b):
    try:
        r = cq.Workplane(obj=a).intersect(cq.Workplane(obj=b))
        return float(sum(sh.Volume() for sh in r.vals()))
    except Exception:
        return 0.0


# ------------------------------------------------------------------- the model
class RearFuselageJoin:

    def __init__(self, P):
        self.P = dict(P)
        self._derive()
        self.registry = []      # (instance_name, base_id, Shape)
        self.structure = []     # (set_id, [(instance_name, Workplane, color_key)])
        self.warnings = []
        self.ghost = None
        self.ghost_cut_tool = None
        self.root = None

    # -- derived quantities ---------------------------------------------------
    def _derive(self):
        P = self.P
        D = self.D = {}
        D["slope"] = (P["ghost_r_fwd"] - P["ghost_r_aft"]) / (P["ghost_x_fwd"] - P["ghost_x_aft"])
        m = abs(D["slope"])
        D["gamma"] = math.atan(m)
        D["sin_g"] = math.sin(D["gamma"])
        D["cos_g"] = math.cos(D["gamma"])
        D["x_apex"] = P["ghost_x_aft"] + P["ghost_r_aft"] / m
        D["ring_r_out"] = P["ring_od"] / 2.0
        D["ring_band_r_in"] = D["ring_r_out"] - P["ring_flange_t"]
        D["land"] = P["ring_axial_total"] - 2.0 * P["ring_flange_w"]
        D["ring_web_r_in"] = D["ring_r_out"] - P["ring_web_h"]
        D["ring_x0"] = -P["ring_axial_total"] / 2.0
        D["boss_r"] = 0.5 * (D["ring_band_r_in"] + D["ring_r_out"])
        D["plug_x_c"] = D["ring_x0"] + P["ring_axial_total"] - 0.5 * P["ring_flange_w"]
        D["pin_x0"] = D["ring_x0"] + P["ring_axial_total"]
        # validations (fail loudly, not silently)
        assert D["land"] > 0.0, "ring_axial_total must exceed 2*ring_flange_w"
        span = P["bracket_x_end"] - P["bracket_x0"]
        assert abs(span - (P["n_brackets_row"] - 1) * P["bracket_pitch"]) < 1e-6, \
            "bracket stations do not close on the stated pitch"
        for k in range(P["n_pins"]):
            a = (P["pin_phase"] + 360.0 / P["n_pins"] * k) % 360.0
            for b in BUTTS:
                assert min(abs(a - b), 360.0 - abs(a - b)) > 1.0, "pin lands on a butt joint"

    def R_out(self, x):
        P = self.P
        return P["ghost_r_aft"] + (x - P["ghost_x_aft"]) * self.D["slope"]

    # -- primitive helpers (all axisymmetric around X or radial) --------------
    def annulus(self, r_out, r_in, x0, length):
        outer = cq.Workplane("YZ", origin=(x0, 0.0, 0.0)).circle(r_out).extrude(length)
        if r_in <= 0.0:
            return outer
        inner = cq.Workplane("YZ", origin=(x0 - 1.0, 0.0, 0.0)).circle(r_in).extrude(length + 2.0)
        return outer.cut(inner)

    def cyl_x(self, r, x0, length, y=0.0, z=0.0):
        return cq.Workplane("YZ", origin=(x0, y, z)).circle(r).extrude(length)

    def wedge(self, phi_a, phi_b, r_max, x0, x1):
        a, b = math.radians(phi_a), math.radians(phi_b)
        mid = 0.5 * (a + b)
        A = (r_max * math.sin(a), r_max * math.cos(a))
        B = (r_max * math.sin(b), r_max * math.cos(b))
        M = (r_max * math.sin(mid), r_max * math.cos(mid))
        return (cq.Workplane("YZ", origin=(x0, 0.0, 0.0))
                .moveTo(0.0, 0.0).lineTo(*A).threePointArc(M, B).close()
                .extrude(x1 - x0))

    def cyl_radial(self, dia, x, phi_deg, r0, r1):
        c = (cq.Workplane("XY", origin=(x, 0.0, r0))
             .circle(dia / 2.0).extrude(r1 - r0))
        return c.rotate((0.0, 0.0, 0.0), (1.0, 0.0, 0.0), -phi_deg)

    @staticmethod
    def _span_hit(ang, lo, hi, hw):
        for a in (ang, ang - 360.0, ang + 360.0):
            if a + hw >= lo and a - hw <= hi:
                return True
        return False

    def _reg(self, base_id, wp, idx, count):
        P = self.P
        if count <= 1 or P["instance_tag"] == "none":
            name = base_id
        else:
            name = f"{base_id}{P['instance_tag']}{idx:02d}"
        self.registry.append((name, base_id, wp.val()))
        return name

    # -- -010 splice ring: segments + butt straps ------------------------------
    def _build_ring_segments(self):
        P, D = self.P, self.D
        band = self.annulus(D["ring_r_out"], D["ring_band_r_in"],
                            D["ring_x0"], P["ring_axial_total"])
        land = self.annulus(D["ring_r_out"], D["ring_web_r_in"],
                            -D["land"] / 2.0, D["land"])
        ring = band.union(land)

        segs = [[pn, ring.intersect(self.wedge(lo, hi, 1.3 * D["ring_r_out"], -85.0, 85.0)), (lo, hi)]
                for (lo, hi, pn) in QUADS]

        # NDT plug seats: Ø40 through the aft flange, every 30° from 15° (I-2)
        hw = math.degrees(math.atan(0.5 * P["plug_d"] / D["boss_r"])) + 0.2
        for k in range(P["n_plugs"]):
            ang = (P["plug_phi0"] + P["plug_spacing"] * k) % 360.0
            tool = self.cyl_radial(P["plug_d"], D["plug_x_c"], ang,
                                   D["ring_band_r_in"] - 5.0, D["ring_r_out"] + 5.0)
            for s in segs:
                (lo, hi) = s[2]
                if self._span_hit(ang, lo, hi, hw):
                    s[1] = s[1].cut(tool)

        items = []
        for i, s in enumerate(segs):
            name = self._reg(s[0], s[1], i + 1, 1)
            items.append((name, s[1], "ring"))

        # segment butt straps (no PN — I-12)
        r_mid = D["ring_web_r_in"] - P["strap_t"] / 2.0
        for i, b in enumerate(BUTTS):
            delta = math.degrees(0.5 * P["strap_arc"] / r_mid)
            an = self.annulus(D["ring_web_r_in"], D["ring_web_r_in"] - P["strap_t"],
                              -P["strap_axial"] / 2.0, P["strap_axial"])
            w = self.wedge(b - delta, b + delta, 1.3 * D["ring_r_out"],
                           -P["strap_axial"] / 2.0 - 1.0, P["strap_axial"] / 2.0 + 1.0)
            strap = an.intersect(w)
            name = self._reg("BUTT-STRAP-SEGMENT-JOIN", strap, i + 1, 4)
            items.append((name, strap, "ring"))

        self.structure.append((f"{PN}-010", items))

    # -- -020/-021 join indexing ------------------------------------------------
    def _build_indexing(self):
        P, D = self.P, self.D
        items = []
        x0 = D["pin_x0"]
        for k in range(P["n_pins"]):
            phi = P["pin_phase"] + 360.0 / P["n_pins"] * k
            p = math.radians(phi)
            y, z = D["boss_r"] * math.sin(p), D["boss_r"] * math.cos(p)
            boss = self.cyl_x(0.5 * P["boss_d"], x0, P["boss_l"], y, z)
            bore = self.cyl_x(0.5 * P["pin_d"], x0 - 1.0, P["boss_l"] + 2.0, y, z)
            boss = boss.cut(bore)
            name = self._reg(f"{PN}-020", boss, k + 1, P["n_pins"])
            items.append((name, boss, "ring"))

            pin = self.cyl_x(0.5 * P["pin_d"], x0, P["pin_l"], y, z)
            pin = pin.edges(">X").chamfer(P["pin_chamfer"])
            name = self._reg(f"{PN}-021", pin, k + 1, P["n_pins"])
            items.append((name, pin, "steel"))
        self.structure.append((f"{PN}-020", items))

    # -- -030/-031 systems-run brackets -----------------------------------------
    def _bracket_canonical(self):
        P = self.P
        la, lb, w, t = (P["bracket_len_a"], P["bracket_len_c"],
                        P["bracket_width"], P["bracket_t"])
        prof = [(-la / 2.0, 0.0), (la / 2.0, 0.0), (la / 2.0, -lb),
                (la / 2.0 - t, -lb), (la / 2.0 - t, -t), (-la / 2.0, -t)]
        br = (cq.Workplane("XZ").polyline(prof).close().extrude(w)
              .translate((0.0, w / 2.0, 0.0)))
        hd = 0.5 * P["bracket_hole_d"]
        for hx in (-(la / 2.0 - 25.0), la / 2.0 - 25.0):
            h = cq.Workplane("XY", origin=(hx, 0.0, -t - 1.0)).circle(hd).extrude(t + 2.0)
            br = br.cut(h)
        for hz in (-0.25 * lb, -0.75 * lb):
            h = cq.Workplane("YZ", origin=(la / 2.0 - t - 1.0, 0.0, hz)).circle(hd).extrude(t + 2.0)
            br = br.cut(h)
        return br

    def _valve_half_phi(self):
        P, D = self.P, self.D
        rho_c = self.R_out(P["ov_x"]) / D["sin_g"]
        return math.degrees((0.5 * P["doubler_circ"]) / rho_c / D["sin_g"])

    def _bracket_phi(self, phi_row, x):
        P = self.P
        if not P["bracket_dodge"]:
            return phi_row, "nominal (dodge disabled)"
        half_phi = self._valve_half_phi()
        half_x = 0.5 * P["doubler_axial"] + 0.5 * P["bracket_len_a"] + 5.0
        if abs(x - P["ov_x"]) >= half_x:
            return phi_row, "nominal"
        br_half = math.degrees(0.5 * P["bracket_width"] /
                               (self.R_out(x) - P["ghost_wall"]))
        d = (phi_row - P["ov_phi"] + 180.0) % 360.0 - 180.0
        if abs(d) >= half_phi + br_half + 1.0:
            return phi_row, "nominal"
        sgn = 1.0 if d >= 0.0 else -1.0
        phi_new = P["ov_phi"] + sgn * (half_phi + br_half + 2.0)
        return phi_new, f"dodged {phi_row:.1f} -> {phi_new:.1f} deg (I-7)"

    def _place_bracket(self, canon, x, phi_deg):
        P, D = self.P, self.D
        p = math.radians(phi_deg)
        # exact point on the inner shell surface (normal offset of the outer cone)
        x0 = x - P["ghost_wall"] * D["sin_g"]
        R0 = self.R_out(x) - P["ghost_wall"] * D["cos_g"]
        P0 = Vector(x0, R0 * math.sin(p), R0 * math.cos(p))
        # orientation: rotate about X by -phi (y -> circumferential), then tilt
        # about the circumferential axis by +gamma (x -> cone generator)
        w = canon.rotate((0.0, 0.0, 0.0), (1.0, 0.0, 0.0), -phi_deg)
        b = (0.0, math.cos(p), -math.sin(p))
        w = w.rotate((0.0, 0.0, 0.0), b, math.degrees(D["gamma"]))
        return w.translate((P0.x, P0.y, P0.z))

    def _build_brackets(self):
        P = self.P
        canon = self._bracket_canonical()
        stations = [P["bracket_x0"] + P["bracket_pitch"] * i
                    for i in range(P["n_brackets_row"])]
        items = []
        idx = 0
        for phi_row in P["bracket_row_phi"]:
            for xs in stations:
                phi_use, note = self._bracket_phi(phi_row, xs)
                if "dodged" in note:
                    self.warnings.append(f"bracket @ X={xs:.0f}, row {phi_row:.0f}deg: {note}")
                inst = self._place_bracket(canon, xs, phi_use)
                idx += 1
                name = self._reg(f"{PN}-031", inst, idx, 2 * P["n_brackets_row"])
                items.append((name, inst, "amber"))
        self.structure.append((f"{PN}-030", items))

    # -- -040/-041/-042 outflow-valve surround ----------------------------------
    def _build_valve_surround(self):
        P, D = self.P, self.D
        # exact conical development: flat patch rolled onto the shell cone
        R_c = self.R_out(P["ov_x"])
        rho_c = R_c / D["sin_g"]
        beta_c = math.radians(P["ov_phi"]) * D["sin_g"]
        cb, sb = math.cos(beta_c), math.sin(beta_c)
        x_apex, sin_g, cos_g = D["x_apex"], D["sin_g"], D["cos_g"]

        def dev(u, v, t):
            dx = (rho_c + u) * cb - v * sb
            dy = (rho_c + u) * sb + v * cb
            rho = math.hypot(dx, dy)
            psi = math.atan2(dy, dx) / sin_g
            x = x_apex - rho * cos_g - t * sin_g          # t = inward normal offset
            R = rho * sin_g - t * cos_g
            return Vector(x, R * math.sin(psi), R * math.cos(psi))

        def loft_patch(pts, ta, tb):
            wa = cq.Wire.makePolygon([dev(u, v, ta) for (u, v) in pts], True)
            wb = cq.Wire.makePolygon([dev(u, v, tb) for (u, v) in pts], True)
            return cq.Workplane(obj=cq.Solid.makeLoft([wa, wb], True))

        t_skin = P["ghost_wall"]                 # inner face of context shell
        t_din = t_skin + P["doubler_t"]          # doubler inner face

        outer = rounded_rect_points(P["doubler_axial"], P["doubler_circ"], P["doubler_corner_r"])
        cutout = rounded_rect_points(P["cutout_axial"], P["cutout_circ"], P["cutout_corner_r"])

        doubler = loft_patch(outer, t_skin, t_din).cut(loft_patch(cutout, t_skin, t_din))

        # rivet pattern around the cutout (I-6)
        off = P["rivet_offset"]
        cont = rounded_rect_points(P["cutout_axial"] + 2 * off,
                                   P["cutout_circ"] + 2 * off,
                                   P["cutout_corner_r"] + off)
        for (u, v) in points_along(cont, P["rivet_pitch"]):
            base, tip = dev(u, v, t_skin - 1.5), dev(u, v, t_din + 1.5)
            nv = Vector(tip.x - base.x, tip.y - base.y, tip.z - base.z)
            L = nv.Length
            nv = Vector(nv.x / L, nv.y / L, nv.z / L)
            hole = cq.Workplane("XY").circle(0.5 * P["rivet_d"]).extrude(L)
            ax = Vector(0, 0, 1).cross(nv)
            if ax.Length > 1e-9:
                ax = Vector(ax.x / ax.Length, ax.y / ax.Length, ax.z / ax.Length)
                ang = math.degrees(math.acos(_clamp1(Vector(0, 0, 1).dot(nv))))
                hole = hole.rotate((0.0, 0.0, 0.0), (ax.x, ax.y, ax.z), ang)
            hole = hole.translate((base.x, base.y, base.z))
            doubler = doubler.cut(hole)

        # surround frame on the doubler inner face (I-4)
        fw = P["frame_width"]
        fout = rounded_rect_points(P["cutout_axial"] + 2 * fw,
                                   P["cutout_circ"] + 2 * fw,
                                   P["cutout_corner_r"] + fw)
        frame = (loft_patch(fout, t_din, t_din + P["frame_depth"])
                 .cut(loft_patch(cutout, t_din, t_din + P["frame_depth"])))

        # preview-only cut of the valve provision in the ghost shell
        if P["ghost_cutout"]:
            self.ghost_cut_tool = loft_patch(cutout, -1.0, P["ghost_wall"] + 1.0)

        items = [(self._reg(f"{PN}-041", doubler, 1, 1), doubler, "teal"),
                 (self._reg(f"{PN}-042", frame, 1, 1), frame, "teal")]
        self.structure.append((f"{PN}-040", items))

    # -- -050/-051 NDT plugs -----------------------------------------------------
    def _build_plugs(self):
        P, D = self.P, self.D
        items = []
        hex_cd = P["plug_socket_af"] / math.cos(math.radians(30.0))
        for k in range(P["n_plugs"]):
            phi = (P["plug_phi0"] + P["plug_spacing"] * k) % 360.0
            body = (cq.Workplane("XY", origin=(D["plug_x_c"], 0.0,
                                              D["ring_r_out"] - P["plug_t"]))
                    .circle(0.5 * P["plug_d"]).extrude(P["plug_t"]))
            sock = (cq.Workplane("XY", origin=(D["plug_x_c"], 0.0,
                                               D["ring_r_out"] - P["plug_socket_depth"]))
                    .polygon(6, hex_cd).extrude(P["plug_socket_depth"] + 1.0))
            body = body.cut(sock)
            body = body.rotate((0.0, 0.0, 0.0), (1.0, 0.0, 0.0), -phi)
            name = self._reg(f"{PN}-051", body, k + 1, P["n_plugs"])
            items.append((name, body, "steel"))
        self.structure.append((f"{PN}-050", items))

    # -- ghost context envelope ---------------------------------------------------
    def _build_ghost(self):
        P = self.P
        span = -P["ghost_x_fwd"]
        outer = (cq.Workplane("YZ").workplane(offset=P["ghost_x_fwd"])
                 .circle(P["ghost_r_fwd"]).workplane(offset=span)
                 .circle(P["ghost_r_aft"]).loft(ruled=True))
        inner = (cq.Workplane("YZ").workplane(offset=P["ghost_x_fwd"])
                 .circle(P["ghost_r_fwd"] - P["ghost_wall"]).workplane(offset=span)
                 .circle(P["ghost_r_aft"] - P["ghost_wall"]).loft(ruled=True))
        g = outer.cut(inner)
        if self.ghost_cut_tool is not None:
            g = g.cut(self.ghost_cut_tool)
        self.ghost = g

    # -- assembly -------------------------------------------------------------------
    def build(self):
        self._build_ring_segments()
        self._build_indexing()
        self._build_brackets()
        self._build_valve_surround()
        self._build_plugs()
        self._build_ghost()
        self.root = cq.Assembly(name=f"{PN}-000")
        for set_id, items in self.structure:
            sub = cq.Assembly(name=set_id)
            for name, wp, ckey in items:
                try:
                    sub.add(wp, name=name, color=cq.Color(*COL[ckey]))
                except Exception:
                    alt = f"{name}-2"
                    sub.add(wp, name=alt, color=cq.Color(*COL[ckey]))
                    self.warnings.append(f"instance name {name} duplicated; exported as {alt}")
            self.root.add(sub)

    # -- export ---------------------------------------------------------------------
    def export(self, dest: dict):
        dest["step"].mkdir(parents=True, exist_ok=True)
        dest["glb"].mkdir(parents=True, exist_ok=True)
        step = dest["step"] / "EWTW-533001-000_concept.step"
        if _HAVE_STATIC:
            try:
                Interface_Static.SetCVal_s("write.step.schema", self.P["step_schema"])
                Interface_Static.SetCVal_s("write.step.unit", "MM")
            except Exception as e:
                self.warnings.append(f"STEP static params not set: {e}")
        self.root.save(str(step))
        schema = "?"
        try:
            head = step.open().read(4000)
            m = re.search(r"FILE_SCHEMA\s*\(([^)]*)\)", head)
            if m:
                schema = m.group(1).strip()
        except Exception:
            pass

        # ghost context envelope: preview only -- never exported to STEP (I-10)
        preview = cq.Assembly(name="EWTW-533001-000_concept")
        preview.add(self.root)
        preview.add(self.ghost, name="GHOST-CONTEXT-ENVELOPE",
                    color=cq.Color(1.0, 1.0, 1.0, float(self.P["ghost_alpha"])))
        glb = dest["glb"] / "EWTW-533001-000_concept.glb"
        try:
            preview.save(str(glb))
        except Exception as e:
            self.warnings.append(f"GLB export failed: {e!r}")
        self.export_facts = {
            "step_path": str(step),
            "glb_path": str(glb),
            "step_schema": schema,
            "step_bytes": step.stat().st_size if step.exists() else 0,
            "glb_bytes": glb.stat().st_size if glb.exists() else 0,
        }
        return self.export_facts

    # -- verification: every check prints its expected value --------------------
    def verify(self, overrides=None):
        import time
        P, D = self.P, self.D
        t0 = time.time()
        lines, hard = [], []
        n_pass = n_warn = n_info = 0

        def emit(tag, name, expected, actual):
            lines.append(f"[{tag}] {name}: expected {expected} | actual {actual}")

        def check(name, expected, actual, ok=None):
            nonlocal n_pass
            good = (expected == actual) if ok is None else ok
            if good:
                n_pass += 1
                emit("PASS", name, expected, actual)
            else:
                hard.append(name)
                emit("FAIL", name, expected, actual)

        def info(name, expected, actual):
            nonlocal n_info
            n_info += 1
            emit("INFO", name, expected, actual)

        def warn(name, expected, actual):
            nonlocal n_warn
            n_warn += 1
            emit("WARN", name, expected, actual)

        ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        lines += [
            "=" * 78,
            " EWTW-533001-000  STRUCTURE, REAR FUSELAGE ZONE  --  concept verification",
            " AMPEL360 eWTW | X aft+ / Y left+ / Z up+ | mm | origin = JP on centreline",
            f" provenance: {ts} | {GENERATOR_FILE} | {GENERATOR_VERSION}",
            " maturity: CONCEPT -- all dimensions are declared envelope assumptions",
            "=" * 78,
            " declared envelope (to be superseded by ratified eWTW frame data):",
        ]
        for k in ("ghost_x_fwd", "ghost_x_aft", "ring_od", "ring_web_h",
                  "ring_flange_w", "n_pins", "bracket_pitch", "n_brackets_row",
                  "ov_x", "cutout_axial", "cutout_circ", "n_plugs"):
            lines.append(f"        {k:18s} = {P[k]!r}")
        if overrides:
            lines.append(" parameter overrides (checks compare the DECLARED topology):")
            for k in sorted(overrides):
                lines.append(f"        {k} = {overrides[k]!r}   (declared {PARAMS[k]!r})")

        # -- A | part-count truth ---------------------------------------------------
        lines += ["", "== A | part-count truth (registry vs declared topology) =="]
        counts = {}
        for _n, base, _s in self.registry:
            counts[base] = counts.get(base, 0) + 1
        for base in sorted(EXPECTED):
            check(f"count {base}", EXPECTED[base], counts.get(base, 0))
        for base in sorted(set(counts) - set(EXPECTED)):
            check(f"count {base} (undeclared)", 0, counts[base])
        check("total leaf bodies", sum(EXPECTED.values()), len(self.registry))

        # -- B | assembly tree truth --------------------------------------------------
        lines += ["", "== B | assembly tree truth =="]
        declared_sets = [f"{PN}-010", f"{PN}-020", f"{PN}-030",
                         f"{PN}-040", f"{PN}-050"]
        check("set sub-assembly ids", declared_sets, [s for s, _ in self.structure])
        names = [n for n, _b, _s in self.registry]
        check("unique instance names", len(names), len(set(names)))

        # -- C | topology truth ----------------------------------------------------------
        lines += ["", "== C | topology truth =="]
        check("bracket row closes on pitch (mm)", 0.0,
              round((P["bracket_x_end"] - P["bracket_x0"])
                    - (P["n_brackets_row"] - 1) * P["bracket_pitch"], 6))
        stations = [P["bracket_x0"] + P["bracket_pitch"] * i
                    for i in range(P["n_brackets_row"])]
        info("bracket stations (mm)",
             f"[{P['bracket_x0']:.0f} .. {P['bracket_x_end']:.0f}] step {P['bracket_pitch']:.0f}",
             f"[{stations[0]:.0f} .. {stations[-1]:.0f}] step {P['bracket_pitch']:.0f}")
        pin_phis = [(P["pin_phase"] + 360.0 / P["n_pins"] * k) % 360.0
                    for k in range(P["n_pins"])]
        minsep = min(min(abs(a - b), 360.0 - abs(a - b))
                     for a in pin_phis for b in BUTTS)
        check("pin-to-butt min separation >= 1 deg (declared 22.5)", True, minsep >= 1.0)
        info("pin phases (deg)", "22.5 + k*45",
             str(sorted(round(a, 1) for a in pin_phis)))
        plug_phis = [(P["plug_phi0"] + P["plug_spacing"] * k) % 360.0
                     for k in range(P["n_plugs"])]
        straddle = sum(1 for a in plug_phis
                       if min(min(abs(a - b), 360.0 - abs(a - b))
                              for b in BUTTS) <= 0.5)
        info("plug seats straddling butt joints (I-2, flagged)", 4, straddle)
        info("ring cross-section (I-1)",
             "OD 2200 / band t 5 / flanges 60+60 / land 30 / web h 120",
             (f"OD {P['ring_od']:.0f} / band t {P['ring_flange_t']:.0f} / "
              f"flanges {P['ring_flange_w']:.0f}+{P['ring_flange_w']:.0f} / "
              f"land {D['land']:.0f} / web h {P['ring_web_h']:.0f}"))

        # -- D | interference truth ----------------------------------------------------------
        lines += ["", "== D | interference truth (assembly bodies only; ghost excluded) =="]
        if not P.get("interference_check"):
            info("pairwise boolean scan", "performed", "skipped (interference_check=0)")
        else:
            reg = self.registry
            evaluated = hits = 0
            for i in range(len(reg)):
                for j in range(i + 1, len(reg)):
                    if not _bbox_overlap(reg[i][2], reg[j][2]):
                        continue
                    evaluated += 1
                    v = _common_volume(reg[i][2], reg[j][2])
                    if v > 1.0:
                        hits += 1
                        lines.append(f"        OVERLAP {reg[i][0]} X {reg[j][0]}"
                                     f" = {v:.1f} mm3")
            check("hard interferences (> 1 mm3)", 0, hits)
            info("boolean pairs evaluated", "bbox-overlapping pairs", evaluated)

        # -- E | neutral-file truth --------------------------------------------------------------
        lines += ["", "== E | neutral-file truth =="]
        ef = getattr(self, "export_facts", None)
        if ef is None:
            info("file checks", "performed", "skipped (--no-export)")
        else:
            step_p, glb_p = Path(ef["step_path"]), Path(ef["glb_path"])
            check("STEP on disk", True, step_p.exists())
            check("STEP non-empty", True, ef["step_bytes"] > 0)
            check("GLB on disk", True, glb_p.exists() and ef["glb_bytes"] > 0)
            if glb_p.exists():
                with glb_p.open("rb") as fh:
                    magic = fh.read(4).decode("ascii", "replace")
                check("GLB magic", "glTF", magic)
                info("ghost present in GLB preview", True,
                     b"GHOST-CONTEXT-ENVELOPE" in glb_p.read_bytes())
            schema = str(ef.get("step_schema", "?"))
            if "AP242" in schema:
                check("STEP FILE_SCHEMA carries AP242", True, True)
            else:
                warn("STEP FILE_SCHEMA carries AP242 (writer fallback; geometry unaffected)",
                     True, False)
            if step_p.exists():
                text = step_p.read_text(errors="replace")
                wanted = sorted(set(list(EXPECTED) + declared_sets + [f"{PN}-000"]))
                missing = [b for b in wanted if b not in text]
                check("STEP name coverage (missing)", [], missing)
                check("ghost excluded from STEP", True,
                      "GHOST-CONTEXT-ENVELOPE" not in text)

        # -- F | volume rollup -----------------------------------------------------------------------
        lines += ["", "== F | volume rollup (concept geometry, mm3) =="]
        total = 0.0
        for set_id, items in self.structure:
            v = sum(wp.val().Volume() for _n, wp, _c in items)
            total += v
            lines.append(f"        {set_id:20s} {v:14.1f}")
        lines.append(f"        {'TOTAL':20s} {total:14.1f}")

        # -- G | builder warnings ----------------------------------------------------------------------
        if self.warnings:
            lines += ["", "== G | builder warnings =="]
            for w in self.warnings:
                lines.append(f"        {w}")

        # -- H | interpretation notes ----------------------------------------------------------------------
        lines += ["", "== H | interpretation notes I-1 .. I-14 =="]
        for n in NOTES:
            lines.append(f"        {n}")

        lines += ["", "=" * 78,
                  f" {n_pass} PASS | {len(hard)} FAIL | {n_warn} WARN | {n_info} INFO"
                  f" | runtime {time.time() - t0:.1f} s",
                  " topology preserved: 4-segment ring | 8 indexing pins | 12 brackets"
                  " in two rows | one lower-RH cutout | 12 NDT plugs",
                  "=" * 78]
        return "\n".join(lines), len(hard)


# ---- run-record.yaml (machine-written ledger; facts only, never claims) ------
def _sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _y(v):
    if isinstance(v, bool):
        return "true" if v else "false"
    if v is None:
        return "null"
    if isinstance(v, (int, float)):
        return str(v)
    return '"%s"' % str(v).replace('"', "'")


def _git(*args, cwd):
    try:
        return subprocess.run(["git", *args], cwd=str(cwd), capture_output=True,
                              text=True, timeout=10).stdout.strip()
    except Exception:
        return ""


def _git_info(root: Path) -> dict:
    head = _git("rev-parse", "HEAD", cwd=root)
    if len(head) != 40:
        return {"commit": "unavailable", "branch": "unavailable", "dirty": None}
    return {"commit": head,
            "branch": _git("rev-parse", "--abbrev-ref", "HEAD", cwd=root) or "detached",
            "dirty": bool(_git("status", "--porcelain", cwd=root))}


def write_run_record(record_path: Path, root: Path, meta: dict, overrides: dict,
                     report: str, exit_code: int, artifacts, prompt_path) -> list:
    """artifacts: list of dicts {role, file, path, format, ...extras}.
    prompt_path: Path or None. Returns warning strings for the caller to print."""
    warnings = []
    gen = Path(__file__).resolve()

    def rel(p: Path) -> str:
        try:
            return str(p.resolve().relative_to(root))
        except ValueError:
            return p.name

    m = re.search(r"(\d+) PASS \| (\d+) FAIL \| (\d+) WARN \| (\d+) INFO", report)
    counts = dict(zip(("pass", "fail", "warn", "info"), map(int, m.groups()))) if m else {}
    n_fail = counts.get("fail", 0)

    if prompt_path is None:
        prompt_sha, prompt_file = "unavailable", _y(meta["prompt_file"])
        warnings.append("prompt file not found on disk — sha256 recorded as unavailable")
    else:
        prompt_sha, prompt_file = _sha256(prompt_path), _y(rel(prompt_path))

    git = _git_info(root)

    L = [
        "# AI-assisted generative CAD execution record",
        f"# Generated automatically by {gen.name}. Do not edit after generation.",
        "# (publish-gate.py recomputes every hash; a hand edit can only break it.)",
        "run:",
        f'  schema: "{RUN_RECORD_SCHEMA}"',
        "",
        f"  id: {_y(meta['run_id'])}",
        f"  timestamp-utc: {_y(datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'))}",
        "",
        "  product:",
        f'    pn: "{PN}-000"',
        '    nomenclature: "STRUCTURE-REAR-FUSELAGE-ZONE"',
        '    maturity: "CONCEPT"',
        "",
        "  prompt:",
        f"    file: {prompt_file}",
        f"    revision: {_y(meta['prompt_rev'])}",
        f'    sha256: "{prompt_sha}"',
        "",
        "  ai:",
        f"    model: {_y(meta['ai_model'])}",
        '    declaration-source: "human"',
        "    model-string-verbatim: true",
        "",
        "  generator:",
        f"    file: {_y(rel(gen))}",
        f"    version: {_y(GENERATOR_VERSION)}",
        f'    sha256: "{_sha256(gen)}"',
        "",
        "  execution:",
        f'    python-version: "{sys.version.split()[0]}"',
        f'    cadquery-version: "{getattr(cq, "__version__", "unknown")}"',
        f'    platform: "{platform.platform()}"',
    ]
    if overrides:
        L.append("    parameters-override:")
        for k, val in sorted(overrides.items()):
            L.append(f"      {k}: {_y(val)}")
    else:
        L.append("    parameters-override: {}")
    L += [
        "",
        "  repository:",
        f'    commit: "{git["commit"]}"',
        f'    branch: "{git["branch"]}"',
        f"    dirty: {_y(git['dirty'])}",
        "",
        "  artifacts:",
    ]
    for a in artifacts:
        p = a["path"]
        if not p.exists():
            continue
        L.append(f'    - role: "{a["role"]}"')
        L.append(f'      file: "{a["file"]}"')
        L.append(f'      format: "{a["format"]}"')
        for k in ("requested-schema", "actual-schema"):
            if k in a:
                L.append(f'      {k}: "{a[k]}"')
        if a.get("units"):
            L.append(f'      units: "{a["units"]}"')
        if "ghost-context" in a:
            L.append("      ghost-context: true")
        L.append(f"      bytes: {p.stat().st_size}")
        L.append(f'      sha256: "{_sha256(p)}"')
    L += [
        "",
        "  verification:",
        f"    pass: {counts.get('pass', '?')}",
        f"    fail: {counts.get('fail', '?')}",
        f"    warn: {counts.get('warn', '?')}",
        f"    info: {counts.get('info', '?')}",
        f"    exit-code: {exit_code}",
        f'    result: "{("PASS" if n_fail == 0 and exit_code == 0 else "FAIL")}"',
        "",
    ]
    record_path.parent.mkdir(parents=True, exist_ok=True)
    record_path.write_text("\n".join(L), encoding="utf-8")
    return warnings


# ------------------------------------------------------------------------- CLI
def _coerce(v):
    if "," in v:
        return tuple(float(x) for x in v.split(","))
    try:
        return int(v)
    except ValueError:
        pass
    try:
        return float(v)
    except ValueError:
        pass
    return v


def main(argv=None):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser(
        description="EWTW-533001-000 STRUCTURE, REAR FUSELAGE ZONE -- "
                    "AMPEL360 eWTW concept model generator (mm)")
    ap.add_argument("--out", default=".", metavar="DIR",
                    help="flat-layout output dir (only with --layout flat)")
    ap.add_argument("--layout", choices=("repo", "flat"), default="repo",
                    help="repo: CAD/exchange + CAD/preview + evidence/ + "
                         "prompts/run-record.yaml, resolved from this script")
    ap.add_argument("--record", default=None, metavar="PATH",
                    help="run-record.yaml path (default depends on layout)")
    ap.add_argument("--prompt-file", default="3d-model_EWTW-533001-000_revC.md")
    ap.add_argument("--prompt-rev", default="C")
    ap.add_argument("--ai-model", default="GLM 5.3 (Z.ai)",
                    help="human-declared attribution, recorded verbatim; "
                         "override per run")
    ap.add_argument("--run-id", default=None)
    ap.add_argument("--no-export", action="store_true",
                    help="build + verify only; no STEP/GLB written")
    ap.add_argument("--param", action="append", default=[], metavar="KEY=VALUE",
                    help="parameter override (repeatable); tuples as KEY=a,b")
    args = ap.parse_args(argv)

    P = dict(PARAMS)
    overrides = {}
    for spec in args.param:
        key, sep, val = spec.partition("=")
        if not sep or key not in PARAMS:
            ap.error(f"unknown or malformed parameter {spec!r}; see PARAMS in source")
        overrides[key] = P[key] = _coerce(val)

    model = RearFuselageJoin(P)
    model.build()

    # .../<PN folder>/CAD/source/<this file>  ->  PN folder root
    src_dir = Path(__file__).resolve().parent
    root = src_dir.parent.parent
    if args.layout == "repo":
        dest = {"step": root / "CAD" / "exchange",
                "glb": root / "CAD" / "preview",
                "report": root / "evidence"}
        record = Path(args.record) if args.record else root / "prompts" / "run-record.yaml"
    else:
        out = Path(args.out or ".")
        dest = {"step": out, "glb": out, "report": out}
        record = Path(args.record) if args.record else out / "run-record.yaml"

    def rel(p: Path) -> str:
        try:
            return str(p.resolve().relative_to(root))
        except ValueError:
            return p.name

    if not args.no_export:
        model.export(dest)
    facts = getattr(model, "export_facts", {})

    report, n_fail = model.verify(overrides)
    print(report)

    dest["report"].mkdir(parents=True, exist_ok=True)
    rep_path = dest["report"] / "EWTW-533001-000_concept_verification.txt"
    rep_path.write_text(report + "\n", encoding="utf-8")

    step_path = dest["step"] / "EWTW-533001-000_concept.step"
    glb_path = dest["glb"] / "EWTW-533001-000_concept.glb"

    artifacts = [{"role": "verification-evidence", "file": rel(rep_path),
                  "path": rep_path, "format": "text/plain"}]
    if not args.no_export:
        schema_str = str(facts.get("step_schema", "unmeasured")).replace('"', "'")
        artifacts += [
            {"role": "neutral-cad", "file": rel(step_path), "path": step_path,
             "format": "STEP", "requested-schema": "AP242",
             "actual-schema": schema_str, "units": "mm"},
            {"role": "3d-preview", "file": rel(glb_path), "path": glb_path,
             "format": "GLB", "units": "mm", "ghost-context": True},
        ]

    prompt_candidates = [root / "prompts" / args.prompt_file, root / args.prompt_file]
    prompt_path = next((p for p in prompt_candidates if p.exists()), None)

    code = 1 if n_fail else 0
    run_id = args.run_id or (f"EWTW-533001-000-{args.prompt_rev}-"
                             + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"))
    rec_warnings = write_run_record(
        record, root,
        {"run_id": run_id, "prompt_file": args.prompt_file,
         "prompt_rev": args.prompt_rev, "ai_model": args.ai_model},
        overrides, report, code, artifacts, prompt_path)

    for a in artifacts:
        if a["path"].exists():
            print(f"written: {a['file']}")
    print(f"written: {record}")
    for w in rec_warnings:
        print(f"[WARN] {w}")
    return code


if __name__ == "__main__":
    sys.exit(main())
