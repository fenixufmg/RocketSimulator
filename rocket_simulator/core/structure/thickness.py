def thickness(external_radius:float, internal_radius:float)->float:
    """
    This function calculates the rocket motor thickness using the external and internal radius

    Args:
        external_radius (float): motor external radius
        internal_radius (float): motor internal radius

    Returns:
        thickness (float): motor thickness
    """
    return external_radius - internal_radius