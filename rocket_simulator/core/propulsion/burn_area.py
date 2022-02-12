from math import pi 

def burn_area(d):
  #d: intern diameter (user's input)
  #Ab: burn area of the propellant grain 
  Ab = pi*(d**2)
  return Ab
