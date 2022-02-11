from math import sqrt

def von_Mises_stress(parameter_a:float, vessel_maximum_pressure:float)->float:
    return vessel_maximum_pressure*sqrt(3)/(2*(parameter_a-1)) # Para o primeiro fluxo