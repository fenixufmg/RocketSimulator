"""/**
 * @author João Lucas Gomes Alencar
 * @email alencarj2021@mail.com
 * @create date 2022-02-24 14:36:44
 * @modify date 2022-05-03 13:42:49
 * @desc Returns mach number
 */
"""

def mach_number(v: float, c: float) -> float:
    """
    Args:
        v: Rocket velocity
        c: Local sound speed
    Returns:
        M: Mach number
    """
    return v / c
