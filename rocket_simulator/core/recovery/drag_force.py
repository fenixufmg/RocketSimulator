from math import *
from data.parachutes import *
from core.recovery.velocity import Velocity

"""
*@author Izabella de Oliveira Silva
*@email deoliveirasilvaizabella@gmail.com
*@ the drag force is calculated with the use of many variables such as the drag coefficient
"""

def parachute_drag_force(drag_force,air_density,transversal_section_area,drag_coefficient,velocity):
    return (1/2*air_density*velocity^2*transversal_section_area*drag_coefficient)