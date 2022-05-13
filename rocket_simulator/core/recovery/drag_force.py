from math import *
"""
*@author Izabella de Oliveira Silva
*@email deoliveirasilvaizabella@gmail.com
*@ the drag force is calculated with the use of many variables such as the drag coefficient
"""

def Drag_force(Drag_force, air_density, Transversal_section_area, Drag_coefficient, Velocity ):
    return (1 / 2*air_density * Velocity ^ 2 * Transversal_section_area  * Drag_coefficient)