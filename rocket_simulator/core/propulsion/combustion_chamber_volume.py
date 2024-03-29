"""
@author marina
@email [marinasalesr@gmail.com]
@create date 2022-02-11 22:19:15
""" 

from math import pi

def combustion_chamber_volume(Dc:float, Lc:float)->float:
  '''This function calculates the combustion chamber volume, to be used on the calculation of the volumetric load fraction. 
    Args:
        Dc: combustion chamber diameter 
        Lc: combustion chamber lenght
    Returns:
        Vc: combustion chamber volume
    '''    
  Vc = (pi/4)*(Dc**2)*Lc
  return Vc
  
