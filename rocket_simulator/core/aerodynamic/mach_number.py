# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 19:04:30 2022
@author: Alexandre L Barbosa
"""

def mach_number(rocket_velocity: float, local_sound_speed:float) -> float:
    return rocket_velocity / local_sound_speed