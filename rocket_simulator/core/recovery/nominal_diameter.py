from math import *
from math import pi
"""
*@author Caio Bertolato Pereira
*@ Nominal diameter is the diameter that a circle would be if it had the transversal section area that we are going to use
"""

def nominal_Diameter (transversal_section_area):
    return 2*((transversal_section_area)/pi)**(1/2)