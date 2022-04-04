from math import *

"""
*@the opening shock is the factor that determines the maximum force that affects the parachute
*@to get the opening shock we demand the mass ratio, inflation time and other experimental data

"""
def opening_shock(mass_ratio:float, inflation_time:float, Integral:float) -> float:
    return ((2*Integral)/mass_ratio*inflation_time)