"""/**
 * @author João Lucas Gomes Alencar
 * @email alencarj2021@mail.com
 * @create date 2022-04-15 20:03:19
 * @modify date 2022-04-19 16:20:30
 * @desc returns the center of pressure of a single fin
 */
"""

def cp_of_one_fin(c: float, XmacLe: float, XleY: float, cY: float, Afin: float) -> float:
    """
    Args:
        c: Mean aerodynamic chord length
        XmacLe: Effective leading edge location
        XleY: Leading edge position at spanwise position Y
        cY: chord length of one fin
        Afin: Area of one side of the fin
    Returns:
        Xf: Center os pressure position of the fin 
    """
    return XmacLe + 0.25 * c
    #OBS: obter XmacLe
