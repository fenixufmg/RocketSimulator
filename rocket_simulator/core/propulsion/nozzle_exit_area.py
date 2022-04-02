"""
/**
 * @author Arthur Rodrigues de Freitas
 * @email lerytripgo@gmail.com
 * @create date 2022-02-23 16:54:57
 * @modify date 2022-02-23 16:54:57
 * @desc [description]
 */
 """
import math

def nozzle_exit_area(de):
    """
    This function returns the nozzle exit area.

    Args:
        de (num): diameter of nozzle's exit.

    Returns:
        num(Ae): nozzle's exit area. 
    """
    Ae=(math.pi/4)*(de^2)
    return Ae