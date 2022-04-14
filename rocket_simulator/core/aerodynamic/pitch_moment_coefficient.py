"""
/**
 * @author João Lucas Gomes Alencar
 * @email alencarj2021@mail.com
 * @create date 2022-04-13 20:33:46
 * @modify date 2022-04-13 20:34:17
 * @desc returns the pitch moment coefficient
 */
 """

def pitch_moment_coefficient(pitch_moment: float, air_density: float, rocket_velocity: float, 
                                reference_area: float, reference_diameter: float, attack_angle) -> float:
    return pitch_moment / (0.5 * air_density * rocket_velocity * reference_area * reference_diameter * attack_angle)                         
    
