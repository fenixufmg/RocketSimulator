"""
/**
 * @author Arthur Rodrigues de Freitas
 * @email lerytripgo@gmail.com
 * @create date 2022-02-23 16:53:40
 * @modify date 2022-02-23 16:53:40
 * @desc [description]
 */
 """
import math

def area_of_flow(d, Vl):
    """
    This function calculates the area of flow for the combustion products based on the volumetric load. 

    Args:
        d (num): internal diameter of the grain.
        Vl (num): volumetric loading fraction.

    Returns:
        num(Ap): area of flow for the products of combustion.
    """
    Ap=(math.pi/4)*(d^2)*(1-Vl)
    return Ap
