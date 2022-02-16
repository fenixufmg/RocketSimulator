def total_skin_friction_drag_coefficient(adjust_cf: float, rocket_fineness_ratio: float, body_total_area: float, 
                                            fin_thickness: float, mean_aerodynamic_chord: float, a_wet_fins: float, 
                                            reference_area: float) -> float:
    '''
    Parameters:
        a_wet_fins: Area of both sides of the fins
        fin_thickness: Thickness of only one fin 
    '''
    return adjust_cf * ((1 + 1 / (2 * rocket_fineness_ratio)) * body_total_area + (1 + 2 * fin_thickness / mean_aerodynamic_chord) * a_wet_fins) / reference_area
