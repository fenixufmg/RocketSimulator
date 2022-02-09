import math 

def propellant_volume(D, d, L, number):
  #D: external diameter (users' input)
  #d: internal diameter (users' input)
  #L: segment's lenght (users' input)
  #N: number of segments (users' input)
  volume = (math.pi/4)*(D**2 - d**2)*L*N
  return volume 
