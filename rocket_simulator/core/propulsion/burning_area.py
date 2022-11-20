"""
@author marina
@email [marinasalesr@gmail.com]
@create date 2022-02-11 22:12:23
""" 

from math import pi 

def burning_area(d: float) -> float:
  '''This function calculates the burning area of the propellant grain. To be corrected including an iterative loop based on time.
    Args:
        d: intern diameter (user's input) 
    Returns:
        Ab: burning area of the propellant grain
    '''    
  Ab = pi*(d**2)
  return Ab
