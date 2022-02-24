"""/**
 * @author João Lucas Gomes Alencar
 * @email alencarj2021@mail.com
 * @create date 2022-02-24 14:36:44
 * @modify date 2022-02-24 14:36:44
 * @desc Returns mach number
 */
"""

def mach_number(rocket_velocity: float, local_sound_speed:float) -> float:
    return rocket_velocity / local_sound_speed