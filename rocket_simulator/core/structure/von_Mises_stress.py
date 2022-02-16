"""
@author [diego]
@email [dmgp1302@gmail.com]
@create date 2022-02-11 17:43:55
@modify date 2022-02-11 18:28:13
""" 

from math import sqrt
from rocket_simulator.models.material_model import MaterialModel

def von_Mises_stress_1_flow(parameter_a:float, vessel_maximum_pressure:float)->float:
    '''von_Mises_stress_1_flow -> Defining security margin of a built motor

    Args:
        parameter_a (float): relation between external radius and internal radius
        vessel_maximum_pressure (float): maximum pressure inside motor due to ignition of fuel grain

    Returns:
        float: Von Mises Stress
    
    '''    
    return vessel_maximum_pressure*sqrt(3)/(2*(parameter_a-1)) # For first work flow


def von_Mises_stress_2_flow(SM:float, material:MaterialModel)->float: 
    
    '''von_Mises_stress_2_flow -> Defining von Mises stress through material yield strength and security margin to build a new motor

    Args:
        SM (float): security margin desired
        material (MaterialModel): material used to build the motor

    Returns:
        float: Von Mises Stress
    '''
    return  material.yield_strength/SM
