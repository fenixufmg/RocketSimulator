"""
@author [diego]
@email [dmgp1302@gmail.com]
@create date 2022-02-11 18:03:46
@modify date 2022-02-17 18:22:03
""" 

from rocket_simulator.models.material_model import MaterialModel

def safety_margin(von_Mises_stress:float,material:MaterialModel)->float:

    '''safety_margin -> only used in the first flow, where we want to find out safaty margin (on second flow, SM is given by client)

    Args:
        von_Mises_stress (float): von Mises stress calculated in it's own method
        material (MaterialModel): material used to build the motor

    Returns:
        float: safety_margin of the built motor
    '''    
    return material.yield_strength/von_Mises_stress