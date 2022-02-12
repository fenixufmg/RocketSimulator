"""
@author marina
@email [marinasalesr@gmail.com]
@create date 2022-02-11 22:23:58
""" 

def propellant_density(mg, Vg):
  '''burn_area 
    Args:
        mg: propellant's mass (users' input) 
        Vg: volume = previously calculated
    Returns:
        rop: propellant's density
    '''    
  rop = mg/Vg
  return rop
