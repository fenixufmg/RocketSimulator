"""
@author marina
@email [marinasalesr@gmail.com]
@create date 2022-02-11 22:12:23
""" 

from math import pi 

def burn_area(d: float) -> float:
  '''burn_area 
    Args:
        d: intern diameter (user's input) 
    Returns:
        Ab: burn area of the propellant grain
    '''    
  Ab = pi*(d**2)
  return Ab
