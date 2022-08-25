"""
/**
* @author João Lucas Gomes Alencar
* @email alencarj2021@mail.com
* @create date 2022-02-24 14:27:00
* @modify date 2022-02-24 14:27:00
* @desc returns the total skin friction drag coefficient
*/
"""
def total_skin_friction_drag_coefficient(adjust_cf: float, rocket_fineness_ratio: float, body_total_area: float, 
                                            fin_thickness: float, mean_aerodynamic_chord: float, a_wet_fins: float, 
                                            reference_area: float) -> float:
    """
    Parameters:
        a_wet_fins: Area of both sides of the fins
        fin_thickness: Thickness of only one fin 
    """
    if mean_aerodynamic_chord == 0:
        return adjust_cf * (1 + 1 / (2 * rocket_fineness_ratio)) * body_total_area / reference_area
    
    else:
        return adjust_cf * ((1 + 1 / (2 * rocket_fineness_ratio)) * body_total_area + (1 + 2 * fin_thickness / mean_aerodynamic_chord) * a_wet_fins) / reference_area
