"""
@author [diego]
@email [dmgp1302@gmail.com]
@create date 2022-02-11 18:09:50
@modify date 2022-02-17 18:26:45
""" 
from math import sqrt

def parameter_a(external_radius: float = None, internal_radius: float = None,vessel_maximum_pressure:float=None,von_Mises_stress:float=None) -> float:
    '''parameter_a -> defining the ratio between a mortor's external radius and internal radius

    Args:
        first flow: defining parameter a according to known radius
            external_radius (float, optional): Motor external radius. Defaults to None. 
            internal_radius (float, optional): Motor internal radius. Defaults to None.
            
        second flow: defining parameter a to find external radius later
            vessel_maximum_pressure (float, optional): maximum pressure inside motor due to ignition of fuel grain. Defaults to None.
            von_Mises_stress (float, optional): von Mises stress calculated in it's own method. Defaults to None.

    Returns:
        float: parameter a
    '''    

    if external_radius&internal_radius&vessel_maximum_pressure&von_Mises_stress: # checks if the first flow matches with the second flow
        param_a1= external_radius / internal_radius
        param_a2= (vessel_maximum_pressure*sqrt(3)/(2*von_Mises_stress)+1)
        assert param_a1 == param_a2, 'parameter_a error (external_radius,internal_radius,vessel_maximum_pressure,von_Mises_stress): parameter a does not match between variables given'
        return param_a1

    elif external_radius&internal_radius: # first flow
        assert vessel_maximum_pressure is None and von_Mises_stress is None, 'parameter_a error (vessel_maximum_pressure,von_Mises_stress): excessive number of variables!' 
        # ^ Take this off if needed
        return external_radius / internal_radius

    else: # second flow
        assert external_radius is None and internal_radius is None, 'parameter_a error (external_radius,internal_radius): excessive number of variables!'
        # ^ Take this off if needed
        return (vessel_maximum_pressure*sqrt(3)/(2*von_Mises_stress)+1)
    