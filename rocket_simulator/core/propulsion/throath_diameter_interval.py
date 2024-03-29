"""
@author marina
@email [marinasalesr@gmail.com]
@create date 2022-02-11 22:48:31
""" 
from math import pi

def throath_diameter_interval(Ap:float)->float:
  '''This function calculates the minimum and maximum throat diameters, as well as the avarage diameter, and returns only the avarage diameter. It's based on Robert Nakka's documentation. 
     The chosen interval is based on studies of the erosive propellant's burning. 
    Args:
        Ap: area of combustion products flow
        
    Intermidiary:
      d_max: maximum diameter 
      d_min: minimum diameter
      
    Returns:
        d_: medium diameter
    '''    
  d_max = (2*Ap/pi)**(1/2)
  d_min = (4*Ap/3*pi)**(1/2)
  d_ = (d_max + d_min)/2
  return d_
