import math 

def propellant_volume(D, d, lenght, number):
  #D: external diameter (users' input)
  #d: internal diameter (users' input)
  #lenght = users' input
  #number: number of segments (users' input)
  volume = (math.pi/4)*(D**2 - d**2)*lenght*number
  return volume 
