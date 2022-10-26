from math import sqrt

"""
@author marina
@email [marinasalesr@gmail.com]
@create date 2022-02-22 15:48:46
""" 

def nozzle_escape_diameter(d_:float, k:float, Pe:float, Po:float)->float:
   '''This function calculates the nozzle escape (exit) diameter. It's based on its relation with the throat diameter. 
   consider Pe = local atmospheric pressure
   If Pe is different from atmospheric pressure, it must be calculated. 
    Args:
        d_: medium throat diameter
        k: isentropic exponent (depends on user's propellant choice)
        Pe: gas escape pressure
        Po: chamber pressure
    Returns:
        de: nozzle escape diameter 
    '''    
    de = d_/((((k+1)/2)**(1/(k-1)))*((Pe/Po)**(1/k))*sqrt(((k+1)/(k-1))*((1-(Pe/Po))**((k-1)/k))))
    return de
  
