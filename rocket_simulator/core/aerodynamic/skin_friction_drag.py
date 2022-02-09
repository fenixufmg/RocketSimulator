from numpy import log as ln

def skin_friction_drag(reynolds_number: float, critical_reynolds_number: float, 
                        material_roughness: float, rocket_length: float) -> float:
    if reynolds_number < 10000:
        return 0.0148

    elif 10000 < reynolds_number < critical_reynolds_number:
        return 1 / (1.5 * ln(reynolds_number) - 5.6) ** 2
    
    elif reynolds_number > critical_reynolds_number:
        return 0.032 * (material_roughness / rocket_length) ** 0.2
