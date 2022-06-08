"""
/**
 * @author João Lucas Gomes Alencar
 * @email alencarj2021@mail.com
 * @create date 2022-04-09 14:36:50
 * @modify date 2022-04-09 14:52:03
 * @desc [description]
 */
 """

def normal_force(normal_force_coefficient: float, air_density: float, 
                    rocket_velocity: float, reference_area: float, 
                    attack_angle: float) -> float:
    # The normal_force_coefficient is the sum of the normal force coefficient of all the components               
    return (rocket_velocity ** 2) * normal_force_coefficient * air_density * reference_area * attack_angle / 2 
