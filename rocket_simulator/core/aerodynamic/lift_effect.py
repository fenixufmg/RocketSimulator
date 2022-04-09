from math import sin, radians
"""
/**
 * @author João Lucas Gomes Alencar
 * @email alencarj2021@mail.com
 * @create date 2022-04-09 14:51:59
 * @modify date 2022-04-09 14:52:28
 * @desc [description]
 */
 """

def lift_effect(cilinder_length: float, cilinder_diameter: float, 
                    reference_area: float, attack_angle: float) -> float:
    return (1.1 * cilinder_diameter * cilinder_length / reference_area) * (sin(radians(attack_angle))) ** 2
    # Angle of attack in degrees
