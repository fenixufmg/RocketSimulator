# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 17:49:46 2022

@author: victo
"""
def circumferential_tension(parameter_a:float, vessel_maximum_pressure:float)->float:
    return vessel_maximum_pressure / (parameter_a - 1)

