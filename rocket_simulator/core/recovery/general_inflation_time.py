from math import *

"""
*@author Caio Bertolato Pereira
*@ the general inflation time is an arbitrary adimensional value based on inflation time

"""

def general_Inflationtime(inflation_time, nominal_diameter, impulse, drag_area ) -> float:
    return inflation_time*(nominal_diameter/(drag_area)^(1/2))*impulse