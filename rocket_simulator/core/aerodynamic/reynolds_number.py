"""
/**
 * @author João Lucas Gomes Alencar
 * @email alencarj2021@mail.com
 * @create date 2022-02-24 14:39:14
 * @modify date 2022-02-24 14:39:14
 * @desc Returns Reynolds number
 */
"""

def reynolds_number(rocket_velocity: float, rocket_length: float, kinematic_viscosity: float) -> float:
    return (rocket_velocity * rocket_length) / kinematic_viscosity