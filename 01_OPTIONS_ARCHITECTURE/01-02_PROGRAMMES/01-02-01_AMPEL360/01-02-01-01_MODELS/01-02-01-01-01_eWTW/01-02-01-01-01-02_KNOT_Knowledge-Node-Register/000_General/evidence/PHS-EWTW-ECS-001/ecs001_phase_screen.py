"""Conditional dry-air reference model for KNU-EWTW-ECS-001-02 (LC-A).
Run: python3 -I ecs001_phase_screen.py > eWTW-ECS-001_phase-screen_2026-11-27.csv
All output powers cover the operating shipset. Failed-source cases use blank unknowns.
"""
import csv
import math
import sys
from dataclasses import dataclass

CP = 1.005                 # kJ/(kg K), dry air
GAMMA = 1.4
R = 287.05
BETA = (GAMMA - 1) / GAMMA
OCCUPANTS = 104
T_CABIN = 297.15
KT = 1852 / 3600
ETA_COMP = 0.78
ETA_DRIVE = 0.94
ETA_EXPANDER = 0.78
SHAFT_ASSIST = 0.85
HX_APPROACH = 8.0
FLOW_FRACTION_RECIRC = 0.4

@dataclass(frozen=True)
class Point:
    key: str
    conops: str
    alt_ft: int
    tas_kt: int
    delta_isa: float
    cabin_ft: int
    gain_kw: float        # net sensible load into cabin at setpoint, before ventilation
    mode: str = 'normal'
    note: str = 'illustrative'

POINTS = [
    Point('stand_hot', 'stand', 0, 0, 20, 0, 40, note='doors_open_duty_assumed'),
    Point('stand_hot_low', 'stand', 0, 0, 20, 0, 25, note='doors_open_sensitivity'),
    Point('stand_hot_high', 'stand', 0, 0, 20, 0, 55, note='doors_open_sensitivity'),
    Point('stand_humid', 'stand', 0, 0, 20, 0, 40, 'humid',
          '80pct_outside_50pct_zone_equivalent_latent_no_door_moisture'),
    Point('stand_cold', 'stand', 0, 0, -26, 0, -18, note='heating_case'),
    Point('stand_pca', 'stand', 0, 0, 20, 0, 40, 'off', 'adequate_external_PCA_assumed'),
    Point('taxi_out', 'taxi-out', 0, 10, 15, 0, 30),
    Point('takeoff_on', 'take-off', 0, 125, 10, 0, 25),
    Point('takeoff_shed', 'take-off', 0, 125, 10, 0, 25, 'off', 'conditional_STO_policy'),
    Point('climb', 'climb', 15000, 240, 0, 4000, 19),
    Point('cruise_250', 'cruise', 25000, 360, 0, 8000, 16),
    Point('cruise_310', 'cruise', 31000, 360, 0, 8000, 16),
    Point('cruise_350', 'cruise', 35000, 360, 0, 8000, 16),
    Point('descent', 'descent', 10000, 220, 0, 3000, 18),
    Point('hold', 'hold_coincidence', 5000, 170, -8, 3500, 18),
    Point('taxi_in', 'taxi-in', 0, 10, 10, 0, 25),
    Point('one_pack_310', 'pack-inoperative', 31000, 360, 0, 8000, 16, 'one',
          'full_cabin_duty_demand_one_survivor_capacity_unproven'),
    Point('one_pack_reduced', 'pack-inoperative', 31000, 360, 0, 8000, 6, 'one',
          'reduced_duty_survivor_purely_illustrative_no_altitude_credit'),
    Point('one_generator', 'turbogenerator-lost', 31000, 360, 0, 8000, 16, 'unknown',
          'GEN_load_shed_open'),
    Point('lost_normal', 'normal-generation-lost', 31000, 360, 0, 8000, 16, 'off',
          'ELA_sheds_packs_separate_essential_loads'),
    Point('both_off', 'packs-off-in-flight', 8000, 180, 0, 8000, 16, 'off',
          'emergency_ventilation_separate'),
    Point('pressure_loss', 'cabin-pressure-lost', 31000, 300, 0, 8000, 16, 'unknown',
          'transient_leak_and_descent_required'),
    Point('smoke', 'smoke', 10000, 220, 0, 3000, 18, 'unknown',
          'isolation_no_recirc_purge_flow_and_path_open'),
    Point('stand_no_supply_on', 'stand-without-supply', 0, 0, 20, 0, 40, note='onboard_source_assumed'),
    Point('stand_no_supply_off', 'stand-without-supply', 0, 0, 20, 0, 40, 'off',
          'unconditioned_service_outcome_open'),
]

def isa(ft):
    t = 288.15 - 0.0065 * ft * 0.3048
    return t, 101325 * (t / 288.15) ** 5.25588

def compressor_temperature(t, pressure_ratio):
    return t * (1 + (pressure_ratio ** BETA - 1) / ETA_COMP)

def air_cycle(m, q, inlet_t, inlet_p, delivery_p):
    target = T_CABIN - q / (m * CP)
    def states(high_p):
        hot = compressor_temperature(inlet_t, high_p / inlet_p)
        cold_hx = min(hot, inlet_t + HX_APPROACH)
        factor = 1 - ETA_EXPANDER * (1 - (delivery_p / high_p) ** BETA)
        return hot, cold_hx, factor

    minimum = max(delivery_p, inlet_p)
    high = minimum
    hot, cold_hx, factor = states(high)
    if cold_hx * factor > target:
        upper = 15 * minimum
        if states(upper)[1] * states(upper)[2] > target:
            raise ValueError('Unreachable dry-air target in search range')
        lower = minimum
        for _ in range(65):
            middle = (lower + upper) / 2
            _, cold_hx, factor = states(middle)
            if cold_hx * factor > target:
                lower = middle
            else:
                upper = middle
        high = upper
    hot, cold_hx, factor = states(high)
    # Variable bypass; expansion can assist the compressor shaft.
    before_turbine = max(cold_hx, min(hot, target / factor))
    discharge = before_turbine * factor
    comp = m * CP * (hot - inlet_t)
    expander = m * CP * (before_turbine - discharge)
    electric = max(0, comp - SHAFT_ASSIST * expander) / ETA_DRIVE
    heater = m * CP * max(0, target - discharge)
    reject = m * CP * (hot - before_turbine)
    return electric, heater, reject, hot, high / inlet_p

def vapour_cycle(m, q, inlet_t, inlet_p, delivery_p, cop):
    ratio = max(1, delivery_p / inlet_p)
    hot = compressor_temperature(inlet_t, ratio)
    drive = m * CP * (hot - inlet_t) / ETA_DRIVE
    # The CAC aftercooler can precool to cabin setpoint, no colder. Any
    # additional cooling goes to the refrigerant circuit in this architecture.
    needed = q + m * CP * (hot - T_CABIN)
    precool = min(max(needed, 0), m * CP * max(0, hot - max(inlet_t + HX_APPROACH, T_CABIN)))
    evap = max(0, needed - precool)
    heater = max(0, -needed)
    return drive, heater, precool, hot, ratio, evap, evap / cop

def cooling_stream(hx_heat, hot_t, sink_t, rise_target):
    if hx_heat < 1e-9:
        return 0.0
    # Hot-end terminal difference >= 4 K. The active cooler design also
    # enforces a cold-end approach. Heat capacity and UA must be sized later.
    allowed_rise = min(rise_target, hot_t - sink_t - 4)
    if allowed_rise <= 0:
        raise ValueError('Insufficient exchanger temperature difference')
    return hx_heat / (CP * allowed_rise)

METRICS = ('fresh_kg_s','recirc_kg_s','added_latent_kWth','CAC_or_ACM_drive_kW','VCC_evap_kWth',
           'VCC_drive_kW','trim_heat_kW','recirc_fan_kW','sink_fan_kW','bus_steady_kW',
           'bus_incremental_peak_kW','HX_hot_side_kWth','condenser_kWth','HX_sink_kg_s',
           'condenser_sink_kg_s','total_sink_kg_s','captured_sink_kg_s','CAC_pressure_ratio')

def solve(p, option):
    base_t, pressure = isa(p.alt_ft)
    ta = base_t + p.delta_isa
    speed = p.tas_kt * KT
    total_t = ta + speed ** 2 / (2 * CP * 1000)
    inlet_p = pressure * (1 + 0.90 * ((total_t / ta) ** (1 / BETA) - 1))
    cabin_p = isa(p.cabin_ft)[1]
    delivery_p = 1.04 * cabin_p
    t5 = CP * base_t * (max(1, cabin_p / pressure) ** BETA - 1)
    row = {'case':p.key, 'conops_key':p.conops, 'option':option, 'class':'D',
           'status':p.mode, 'alt_ft':p.alt_ft, 'TAS_kt':p.tas_kt,'static_C':ta-273.15,
           'inlet_total_C':total_t-273.15,'cabin_ft':p.cabin_ft,
           'net_sensible_gains_kW':p.gain_kw,'ideal_static_T5_kJ_kg_ISA':t5,'scope':p.note}
    row.update(dict.fromkeys(METRICS))
    if p.mode == 'unknown':
        return row
    if p.mode == 'off':
        for key in METRICS:
            if key not in ('CAC_pressure_ratio','bus_incremental_peak_kW'):
                row[key] = 0.0
        return row
    vent_floor = OCCUPANTS * (0.18 if p.mode == 'one' else 0.25) / 60
    # Set a common supply duty with a 2 C minimum fresh-stream design target.
    m = max(vent_floor, max(0, p.gain_kw) / (CP * (T_CABIN - 275.15)))
    recirc = m * FLOW_FRACTION_RECIRC / (1 - FLOW_FRACTION_RECIRC)
    latent = 0.0
    if p.mode == 'humid':
        def humidity_ratio(temp_k, rh):
            celsius = temp_k - 273.15
            vapour_pa = rh * 611.21 * math.exp((18.678-celsius/234.5)*celsius/(257.14+celsius))
            return 0.62198 * vapour_pa / (pressure - vapour_pa)
        latent = m * 2450 * max(0, humidity_ratio(ta,0.8)-humidity_ratio(T_CABIN,0.5)) + OCCUPANTS*.031
        if option == 'A':
            row.update(fresh_kg_s=m,recirc_kg_s=recirc,added_latent_kWth=latent,
                       scope='wet_turbine_condensation_separator_map_required')
            return row
    cabin_density = cabin_p / (R * T_CABIN)
    recirc_fan = 650 * recirc / (cabin_density * 0.60 * 1000)
    condenser_t = max(308.15, total_t + 18)
    evap_t = 273.15
    cop = 0.38 * evap_t / (condenser_t - evap_t)
    use_air = option == 'A' or (option == 'C' and p.conops not in ('stand','taxi-out','taxi-in','stand-without-supply'))
    if use_air:
        evap = max(0, p.gain_kw) * (0.30 if option == 'C' else 0)
        # Turn recirculation trim down when full ACM bypass would otherwise
        # call for simultaneous reheating. Evaluate at minimum delivery head.
        minimum = max(delivery_p, inlet_p)
        bypass_t = compressor_temperature(total_t, minimum / inlet_p)
        bypass_t *= 1 - ETA_EXPANDER * (1 - (delivery_p / minimum) ** BETA)
        evap = min(evap, max(0, p.gain_kw + m * CP * (bypass_t - T_CABIN)))
        drive, heater, hx_heat, hot, ratio = air_cycle(m, p.gain_kw - evap, total_t, inlet_p, delivery_p)
        vcc = evap / cop
    else:
        drive, heater, hx_heat, hot, ratio, evap, vcc = vapour_cycle(m,p.gain_kw,total_t,inlet_p,delivery_p,cop)
        evap += latent
        vcc = evap / cop
    condenser = evap + vcc
    fan_driven = p.tas_kt < 30
    dt = 15 if fan_driven else 25
    hx_flow = cooling_stream(hx_heat, hot, total_t, dt)
    cond_flow = cooling_stream(condenser, condenser_t, total_t, dt)
    sink = hx_flow + cond_flow
    rho = pressure / (R * ta)
    fan_power = 1000 * sink / (rho * 0.62 * 1000) if fan_driven else 0
    bus = drive + heater + vcc + recirc_fan + fan_power
    values = (m,recirc,latent,drive,evap,vcc,heater,recirc_fan,fan_power,bus,None,
              hx_heat,condenser,hx_flow,cond_flow,sink,0 if fan_driven else sink,ratio)
    row.update(zip(METRICS,values))
    return row

def main():
    rows = [solve(point, opt) for point in POINTS for opt in 'ABC']
    writer = csv.DictWriter(sys.stdout,fieldnames=rows[0].keys(),lineterminator='\n')
    writer.writeheader()
    for row in rows:
        writer.writerow({k: format(v,'.5f') if isinstance(v,float) else v for k,v in row.items()})

if __name__ == '__main__':
    main()
