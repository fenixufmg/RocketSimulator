# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 17:49:46 2022

@author: victo
"""

def circumferential_tension(parameter_a:float, vessel_maximum_pressure:float)->float:
    '''circumferential_tension -> circumferetial tension acting on motor thin walls

    Args:
        parameter_a (float): relation between motor external and internal radius
        vessel_maximum_pressure (float): maximum pressure inside motor due to ignition of fuel grain

    Returns:
        float: circumferential_tension
    '''    
    return vessel_maximum_pressure / (parameter_a - 1)

