import component_drag_coefficient as CDc
"""
/**
 * @author João Lucas Gomes Alencar
 * @email alencarj2021@mail.com
 * @create date 2022-04-09 13:21:56
 * @modify date 2022-06-07 22:33:02
 * @desc returns the total drag coefficient
 */
"""

def total_drag_coefficient(components_number: float, CDc: float, CDf: float) -> float:
    """
    Args:
        CDc: Pressure drag coefficient of the component
        CDf: Total skin friction drag coefficient
        Aref: Reference area
    Returns:
        CD: Total drag coefficient
    """
    CD = CDc + CDf

    return CD
    