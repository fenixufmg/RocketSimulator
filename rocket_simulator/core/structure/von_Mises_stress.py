"""
@author [diego]
@email [dmgp1302@gmail.com]
@create date 2022-02-11 17:43:55
@modify date 2022-02-17 18:05:03
""" 
 
from math import sqrt
from rocket_simulator.models.material_model import MaterialModel

def von_Mises_stress (parameter_a:float = None, vessel_maximum_pressure:float = None, safety_margin:float = None, material:MaterialModel =None)->float:
    '''von_Mises_stress_

    Args:
        first flow: defining safety margin of a built motor
            parameter_a (float): relation between external radius and internal radius
            vessel_maximum_pressure (float): maximum pressure inside motor due to ignition of fuel grain

        second flow: defining von Mises stress through material yield strength and safety margin to build a new motor
            SM (float): safety margin desired
            material (MaterialModel): material used to build the motor

    Returns:
        float: Von Mises Stress
    
    '''    
    if parameter_a&vessel_maximum_pressure&safety_margin&material:
        von_mises_1= vessel_maximum_pressure*sqrt(3)/(2*(parameter_a-1))
        von_mises_2= material.yield_strength/safety_margin
        assert von_mises_1 == von_mises_2, 'von Mises error (parameter_a,vessel_maximum_pressure,safety_margin,material): von mises does not match according to parameters'
        return von_mises_1

    elif parameter_a&vessel_maximum_pressure:
        assert safety_margin is None and material is None, 'von Mises error (safety_margin,material): excessive number of parameters'
        return vessel_maximum_pressure*sqrt(3)/(2*(parameter_a-1)) # For first work flow

    else:
        assert parameter_a is None and vessel_maximum_pressure is None, 'von Mises error (parameter_a,vessel_maximum_pressure): excessive number of parameters'
        return material.yield_strength/safety_margin
