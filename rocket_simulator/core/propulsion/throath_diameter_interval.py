from math import pi

def throath_diameter_interval(Ap):
  #Ap: area of combustion products flow
  #d_max: maximum diameter 
  #d_min: minimum diameter
  #d_: medium diameter
  d_max = (2*Ap/pi)**(1/2)
  d_min = (4*Ap/3*pi)**(1/2)
  d_ = (d_max + d_min)/2
  return d_
