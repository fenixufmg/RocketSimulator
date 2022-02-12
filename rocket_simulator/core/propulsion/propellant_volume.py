"""
@author marina
@email [marinasalesr@gmail.com]
@create date 2022-02-11 22:36:47
""" 

from math import pi

def propellant_volume(D:float, d:float, L:float, N:int)->float:
  '''propellant_volume 
    Args:
        D: external diameter (users' input)
        d: internal diameter (users' input)
        L: segment's lenght (users' input)
        N: number of segments (users' input)
    Returns:
        Vg: propellant's volume
    '''    
  Vg = (math.pi/4)*(D**2 - d**2)*L*N
  return Vg 
