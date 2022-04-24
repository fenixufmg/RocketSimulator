from math import *
"""
*@author Izabella de Oliveira Silva
*@email deoliveirasilvaizabella@gmail.com
*@ the drag force is calculated with the use of many variables such as the drag coefficient
"""

def F_D(F_D, ρar, AST, CD, V ):
    return (1 / 2*ρar * V ^ 2 * AST * CD)