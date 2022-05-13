from math import *
"""
*@author Izabella de Oliveira Silva
*@email deoliveirasilvaizabella@gmail.com
*@ the acceleration that affects the rocket is described by the Second Newton's Law 
"""

def acceleration(acceleration, Weight_force, Drag_force, mass):
    return (Weight_force - Drag_force / mass)