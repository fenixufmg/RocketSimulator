"""
    Breve explicação sobre a função

    Created on Mon Feb  7 17:43:30 2022

    @author: victo
"""

def longitudinal_tension(parameter_a:float, vessel_maximum_pressure:float)->float:
    '''longitudinal_tension -> longitudinal tension acting on motor thin walls

    Args:
        parameter_a (float): relation between motor external and internal radius
        vessel_maximum_pressure (float): maximum pressure inside motor due to ignition of fuel grain

    Returns:
        float: longitudional tension
    '''    
    return vessel_maximum_pressure / (2*(parameter_a - 1))

