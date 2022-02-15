def external_radius(internal_radius:float, parameter_a:float) -> float:
    """
    This function calculates the motor external radius given that parameter_a is already known

    Args:
        internal_radius (float): motor internal radius 
        parameter_a (float): parameter_a

    Returns:
        external_radius (flat): motor external radius
    """
    return parameter_a*internal_radius