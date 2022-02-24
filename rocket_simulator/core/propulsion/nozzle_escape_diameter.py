from math import sqrt

"""
@author marina
@email [marinasalesr@gmail.com]
@create date 2022-02-22 15:48:46
""" 

def nozzle_escape_diameter(d_:float, k:float, Pe:float, Po:float)->float:
   '''nozzle_escape_diameter
   consider Pe = local atmospheric pressure
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
  
