from numpy import log as ln

def skin_friction_drag(reynolds_number: float, critical_reynolds_number: float, 
                        material_roughness: float, rocket_length: float, 
                        mach_number: float) -> float:
    if reynolds_number <= 10000:
        cf = 0.0148

    elif 10000 < reynolds_number < critical_reynolds_number:
        cf = 1 / (1.5 * ln(reynolds_number) - 5.6) ** 2
    
    elif reynolds_number > critical_reynolds_number:
        cf = 0.032 * (material_roughness / rocket_length) ** 0.2

    #adjust_skin_friction_drag_coefficient according to the mach number
    adjust_cf = cf * (1 - 0.1 * mach_number ** 2)
    return adjust_cf