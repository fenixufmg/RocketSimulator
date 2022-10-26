"""
/**
 * @author Arthur Rodrigues de Freitas
 * @email lerytripgo@gmail.com
 * @create date 2022-02-23 16:53:10
 * @modify date 2022-02-23 16:53:10
 * @desc [description]
 */
 """
import math

def burning_time(D, d, r):
    """
    The function returns the burn time of the grain.

    Args:
        D (num): external diameter of the grain.
        d (num): internal diameter of the grain.
        r (num): burn rate of the proppelant.

    Returns:
        num(tb): A real number that indicates the burning time.
    """
    Tb=(D-d)/(2*r)
    return Tb
