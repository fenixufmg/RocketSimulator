"""
@author marina
@email [marinasalesr@gmail.com]
@create date 2022-02-11 22:57:04
""" 

def volumetric_loading_fraction(Vg:float, Vc:float)->float:
  '''volumetric_loading_fraction
    Args:
        Vg: propellant's volume
        Vc: combustion chamber volume
    Returns:
        Vl: volumetric loading fraction
    '''    
  Vl = Vg/Vc
  return Vl
