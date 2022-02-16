"""
@author [diego]
@email [dmgp1302@gmail.com]
@create date 2022-02-11 18:08:07
@modify date 2022-02-11 18:09:42
""" 

def radial_tension(parameter_a:float, vessel_maximum_pressure:float)->float:
    '''radial_tension 

    Args:
        parameter_a (float): relation between motor external and internal radius
        vessel_maximum_pressure (float): maximum pressure inside motor due to ignition of fuel grain

    Returns:
        float: radial tension in motor considered to have thin walls is always zero
    '''    
    return 0