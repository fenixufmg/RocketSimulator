# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 21:07:30 2022
@author: João Lucas
"""

def reynolds_number(rocket_velocity: float, rocket_length: float, kinematic_viscosity: float) -> float:
    return (rocket_velocity * rocket_length) / kinematic_viscosity

