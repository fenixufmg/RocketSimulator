"""
/**
 * @author João Lucas Gomes Alencar
 * @email alencarj2021@mail.com
 * @create date 2022-08-30 08:26:00
 * @modify date 2022-08-30 08:30:34
 * @desc returns the damping force applied on the cg
 */
 """

def damping_force(pitch_damping_coefficient, air_density, velocity, reference_area, reference_diameter, cp_to_nosetip) -> float:
    return 0.5 * pitch_damping_coefficient * air_density * velocity ** 2 * reference_area * reference_diameter / cp_to_nosetip