from math import *
from math import pi
"""
*@author Caio Bertolato Pereira
*@ the momentum of the parachute has two states, one for the angle in horizontal, and one in vertical
* tfill is the stretching time of the parachute, the basis for the inflation time
"""
def momentum(vi,vf,g,tfill):

    return 1 -(vf-vi)-(g/vi)*tfill
