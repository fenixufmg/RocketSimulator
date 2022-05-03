from math import sin, radians
"""
/**
 * @author João Lucas Gomes Alencar
 * @email alencarj2021@mail.com
 * @create date 2022-04-13 20:48:45
 * @modify date 2022-05-03 13:22:46
 * @desc returns the angular velocity
 */
 """

def angular_velocity(v: float, alpha: float) -> float:
    """
    Args:
        v: Velocity of the rocket
        alpha: Angle of attack
    Returns:
        w: Angular velocity
    """
    return v * sin(radians(alpha))
    # Angle of attack in degrees
