"""
/**
 * @author João Lucas Gomes Alencar
 * @email alencarj2021@mail.com
 * @create date 2022-02-24 14:32:58
 * @modify date 2022-02-24 14:32:58
 * @desc Returns de critical Reynolds number
 */
"""

def critical_reynolds_number(mr: float, L: float) -> float:
    """
    Args:
        mr: Material roughness
        L: The rocket length
    Returns:
        Rcrit: Critical Reynolds Number
    """
    return 51 * (mr / L) ** -1.039

#An average surface roughness for a regular paint is 60 micrometers.