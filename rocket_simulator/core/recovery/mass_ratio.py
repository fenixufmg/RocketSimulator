from math import *

"""
*@author Caio Bertolato Pereira
*@ the general inflation time is an arbitrary adimensional value based on inflation time
* p is the atmospheric density at deployment altitude
* Rm is the inverted mass ratio
* m refers to the total payload and parachute mass
"""
def Rm(p,transversal_section_area:float,m:float):
    return (p*(transversal_section_area)**(3/2))/m
