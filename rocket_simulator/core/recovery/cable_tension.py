from math import *

"""
*@author Caio Bertolato Pereira
*@ the general inflation time is an arbitrary adimensional value based on inflation time

"""
def cable_tension(cable_number:float,cable_area:float,maximum_force:float):
    return maximum_force / (cable_number * cable_area)