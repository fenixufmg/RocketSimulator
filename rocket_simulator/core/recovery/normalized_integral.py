import math
from parachute_area import *

"""
* @author Caio Bertolato Pereira
* @email bertolatopereiracaio@gmail.com
"""

def If(Rm):
    if Rm> 0.1:
        return 0.5
    else:
        pass
    if Rm<0.01:
        return 0.2
    else:
        pass
    if 0.01 <= Rm <= 0.10:
        return 0.35