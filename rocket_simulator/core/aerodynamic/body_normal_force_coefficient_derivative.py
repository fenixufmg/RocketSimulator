from math import sin, radians
"""/**
 * @author João Lucas Gomes Alencar
 * @email alencarj2021@mail.com
 * @create date 2022-04-15 20:03:19
 * @modify date 2022-05-03 13:23:00
 * @desc returns the normal force coefficient derivative for the rocket body components
 */
"""

def body_normal_force_coefficient_derivative(Abase: float, Atop: float, Aref: float, alpha: float) -> float:
    """
    Args:
        Abase: Area of the base of the body
        Atop: Area of the top of the body
        Aref: Reference area
        alpha: Angle of attack
    Returns:
        CNaB: normal force coefficient derivative of the body
    """

    return (2 / Aref) * (Abase - Atop) * sin(radians(alpha)) / alpha