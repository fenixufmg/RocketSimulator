from math import *
from operator import truediv
from data.Cables import *
from rocket_simulator.core.recovery.normalized_integral import If

"""
*@author Caio Bertolato Pereira
*@ the general inflation time is an arbitrary adimensional value based on inflation time

"""
def cable_tension(cable_number:float,cable_area:float,maximum_force:float):
    return maximum_force / (cable_number * cable_area)

def cable_break(cable_tension,safe_load):
    load = safe_load
    if cable_tension > safe_load:
        return True
    else:
        return False