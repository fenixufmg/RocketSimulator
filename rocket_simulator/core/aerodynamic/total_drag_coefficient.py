import component_drag_coefficient as CDc
"""
/**
 * @author João Lucas Gomes Alencar
 * @email alencarj2021@mail.com
 * @create date 2022-04-09 13:21:56
 * @modify date 2022-04-09 13:22:29
 * @desc returns the total drag coefficient
 */
"""

def total_drag_coefficient(components_number: float, CDc: float, CDf: float) -> float:
    return CDc + CDf
    """
    Parameters:
        CDc: Component drag coefficient
        CDf: Skin friction drag coefficient
    """