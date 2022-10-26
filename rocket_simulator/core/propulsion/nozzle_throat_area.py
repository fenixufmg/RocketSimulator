"""
/**
 * @author Arthur Rodrigues de Freitas
 * @email lerytripgo@gmail.com
 * @create date 2022-02-23 16:51:48
 * @modify date 2022-02-23 16:51:48
 */
"""
import math

def nozzle_throat_area(d_):
    """
    This funcion calculates the nozzle throat area based on the nozzle's diameter.

    Args:
        d_ (num): diameter of nozzle.

    Returns:
        num(A_): nozzle throat area.
    """
    A_=(math.pi/4)*(d_)^2
    return A_
