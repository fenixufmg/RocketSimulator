from math import *

"""
*@author Caio Bertolato Pereira
*@ maximum force is basically the maximum force that the system is going to be exposed during the flight
"""

def maximum_force(parachute_drag_force:float, opening_shock:float) -> float:
    return parachute_drag_force* opening_shock