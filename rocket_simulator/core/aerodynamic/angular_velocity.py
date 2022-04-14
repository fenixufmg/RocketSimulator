from math import sin, radians
"""
/**
 * @author João Lucas Gomes Alencar
 * @email alencarj2021@mail.com
 * @create date 2022-04-13 20:48:45
 * @modify date 2022-04-13 20:48:45
 * @desc returns the angular velocity
 */
 """

def angular_velocity(rocket_velocity: float, attack_angle: float) -> float:
    return rocket_velocity * sin(radians(attack_angle))
    # Angle of attack in degrees
