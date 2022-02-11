"""
    Breve explicação sobre a função

    Created on Mon Feb  7 17:43:30 2022

    @author: victo
"""
def longitudinal_tension(parameter_a:float, vessel_maximum_pressure:float)->float:
    return vessel_maximum_pressure / (2*(parameter_a - 1))

