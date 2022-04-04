from math import *

"""
*@author Caio Bertolato Pereira
*@ maximum force is basically the maximum force that the system is going to be exposed during the flight
"""

def maximum_force(drag_Force:float, opening_shock:float) -> float:
    return drag_Force* opening_shock