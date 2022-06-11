from math import pi
"""
/**
 * @author João Lucas Gomes Alencar
 * @email alencarj2021@mail.com
 * @create date 2022-04-09 14:36:50
 * @modify date 2022-06-10 23:39:53
 * @desc returns the parasitic drag due to launch guides on the rocket
 */
 """

def parasitc_drag(l, d, CDstag) -> float:
    """
    Args:
        l: length of the launch lug
        d: diameter of the launch lug
        CDstag: Stagnation drag coefficient
    Returns:
        CDparasitic: Parasitic drag coefficient
    """
    
    return max(1.3 - 1.3 * l / d, 1) * CDstag

def parasitic_drag_reference_area(l, d, Rext, Rint) -> float:
    """
    Args:
        l: length of the launch lug
        d: diameter of the launch lug
        Rext: External radius of the lug
        Rint: Internal radius of the lug
    Returns:
        ArefP: Reference area of the lug
    """

    return pi * Rext ** 2 - pi * Rint ** 2 * max(1 - l / d, 0)
    
    