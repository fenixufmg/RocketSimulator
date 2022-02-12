from math import pi

def combustion_chamber_volume(Dc, Lc):
  #Dc: combustion chamber diameter 
  #Lc: combustion chamber lenght
  Vc = (pi/4)*(Dc**2)*Lc
  return Vc
  
