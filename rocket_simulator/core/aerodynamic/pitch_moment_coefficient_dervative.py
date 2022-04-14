from math import sin, radians
"""
/**
 * @author João Lucas Gomes Alencar
 * @email alencarj2021@mail.com
 * @create date 2022-04-13 21:23:00
 * @modify date 2022-04-13 21:23:00
 * @desc Calculates the pitch moment of a component of the rocket
 */
 """

def pitch_moment_coefficient_derivative(reference_area: float, reference_diameter: float, body_base_area: float, 
                                            body_volume: float, attack_angle: float, length: float) -> float:
    return 2 * (length * body_base_area - body_volume) / (reference_area * reference_diameter) * sin(radians(attack_angle)) / attack_angle
