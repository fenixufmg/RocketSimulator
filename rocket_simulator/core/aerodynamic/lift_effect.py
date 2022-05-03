from math import sin, radians
"""
/**
 * @author João Lucas Gomes Alencar
 * @email alencarj2021@mail.com
 * @create date 2022-04-09 14:51:59
 * @modify date 2022-05-03 13:39:44
 * @desc [description]
 */
 """

def lift_effect(cl: float, cd: float, Aref: float, alpha: float) -> float:
    """
    Args:
        cl: Cilinder length
        cd: Cilinder diameter
        Aref: Reference area
        alpha: Angle of attack
    Returns:
        CN: Normal force coefficient
    """
    return (1.1 * cd * cl / Aref) * (sin(radians(alpha))) ** 2
    # Angle of attack in degrees
