"""
/**
 * @author Arthur Rodrigues de Freitas
 * @email lerytripgo@gmail.com
 * @create date 2022-02-23 16:52:47
 * @modify date 2022-02-23 16:52:47
 * @desc [description]
 */
"""
import math

def flow_speed(k, T0, R, M, Pe, Po):
    """
      This function returns the flow speed at the exit of the nozzle.

    Args:
        k (num): isentropic exponent.
        T0 (num): combustion temperature of the proppelant.
        R (num): universal gas constant.
        M (num): effective molar mass of the products.
        Pe (num): atmosferic pressure.
        Po (nu,): pressure inside the chamber.

    Returns:
        num(ve): flow speed at the exit of the nozzle.
    """
    ve=math.sqrt(((2*k*T0)/k-1)*(R/M)*(1-((Pe/Po)^((k-1)/k))))
    return ve