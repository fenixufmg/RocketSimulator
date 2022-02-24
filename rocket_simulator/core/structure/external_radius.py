"""
@author [diego]
@email [dmgp1302@gmail.com]
@create date 2022-02-17 18:24:02
@modify date 2022-02-17 18:26:42
""" 

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