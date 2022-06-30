from math import *
from data.parachutes import *
from core.recovery.velocity import Velocity
from core.recovery.parachute_area import transversal_section_area
from utils.constants import Constants

"""
*@author Izabella de Oliveira Silva
*@email deoliveirasilvaizabella@gmail.com
*@ the drag force is calculated with the use of many variables such as the drag coefficient
"""

def drag_force(transversal_section_area:float, drag_coefficient:float, velocity:float):
    air_density = Constants.AIR_DENSITY.value
    return ((1/2)*air_density*velocity**2*transversal_section_area*drag_coefficient)