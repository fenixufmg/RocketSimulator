"""
@author [diego]
@email [dmgp1302@gmail.com]
@create date 2022-02-11 18:09:50
@modify date 2022-02-11 18:18:14
""" 
from math import sqrt

def parameter_a(external_radius: float = None, internal_radius: float = None,vessel_maximum_pressure:float=None,von_Mises_stress:float=None) -> float:
    '''parameter_a -> defining the ratio between a mortor's external radius and internal radius

    Args:
        external_radius (float, optional): Motor external radius. Defaults to None. # NEEDS ATTENTION LATER!
        internal_radius (float, optional): Motor internal radius. Defaults to None.

    Returns:
        float: parameter a
    '''    
    if external_radius:
        return external_radius / internal_radius
    else:
        return (vessel_maximum_pressure*sqrt(3)/(2*von_Mises_stress)+1)
    