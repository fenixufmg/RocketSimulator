from math import *
"""
*@author Izabella de Oliveira Silva
*@email deoliveirasilvaizabella@gmail.com
*@ the acceleration that affects the rocket is described by the Second Newton's Law 
"""

def acceleration(acceleration, F_W, F_D, mass):
    return (F_W - F_D / mass)