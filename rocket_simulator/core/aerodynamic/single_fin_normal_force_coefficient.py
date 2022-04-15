from math import sqrt, cos, radians, pi 
"""
/**
 * @author João Lucas Gomes Alencar
 * @email alencarj2021@mail.com
 * @create date 2022-04-14 21:02:18
 * @modify date 2022-04-14 21:23:12
 * @desc Returns the normal force coefficient of one fin
 */
"""

def single_fin_normal_force_coefficient(s: float, Aref: float, M: float, Afin: float, T: float) -> float:
    """
    Args:
        s: Spanwise length of one fin
        Aref: Reference area
        M: Mach number
        Afin: Area of one side of a fin
        T: Midchord sweep angle
    Returns:
        CNa1: Normal force coefficient of one fin
    """
    return (2 * pi * (s ** 2) / Aref) / (1 + sqrt(1 + ((sqrt(abs((M ** 2) - 1)) * s ** 2) / Afin * cos(radians(T))) ** 2))



