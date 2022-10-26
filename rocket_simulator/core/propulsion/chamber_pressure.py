"""
@author marina
@email [marinasalesr@gmail.com]
@create date 2022-02-11 23:10:27
""" 

def chamber_pressure(Ab:float, rop:float, a:float, A_:float, k:float, R:float, T0:float, n:float)->float:
  
  '''This function calculates chamber pressure. Its dependence on time is based on the burn area of the propellant grain (consideration to be used in a derivative in another function).
    Args:
        Ab: burning area of the propellant grain
        rop: popellant's density
        a: burn rate coefficient (determined by the propellant chosen)
        A_: throat area
        k: isentropic exponent (determined by the propellant chosen)
        R: molar gas constant
        T0: combustion temperature
        n: pressure exponent (determined by the propellant chosen)
    Returns:
        P0: chamber pressure
    '''    
  P0 = ((Ab/A_)*(a*rop/((k/R*T0)*(2/(k+1))**((k+1)/(k-1))**(1/2))))**(1/(1-n))
  return P0
