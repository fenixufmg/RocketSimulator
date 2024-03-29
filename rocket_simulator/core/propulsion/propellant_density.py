"""
@author marina
@email [marinasalesr@gmail.com]
@create date 2022-02-11 22:23:58
""" 

def propellant_density(mg:float, Vg:float)->float:
  '''This fuction calculates propellant's specif mass (density) based on a tubular geometry (may be changed by changing volume calculations).
    Args:
        mg: propellant's mass (users' input) 
        Vg: volume = previously calculated
    Returns:
        rop: propellant's density
    '''   
  rop = mg/Vg
  return rop
