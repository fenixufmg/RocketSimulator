"""
/**
 * @author Arthur Rodrigues de Freitas
 * @email lerytripgo@gmail.com
 * @create date 2022-02-23 16:56:34
 * @modify date 2022-02-23 16:56:34
 * @desc [description]
 */
"""
import math

def combustion_temperature(Te, k, Me):
    """
    This function calculates the temperature of combustion for the grain.


    Parameters:
        Te(num): temperature at the exit.
        k(num): isetropic exponent.
        Me(num): Mach number of flow at the exit.

    Returns:
        num(T0): a real number that indicates the temperature of combustion.
    """
    T0=Te*(1+((k-1)/2)*(Me^2))
    return T0