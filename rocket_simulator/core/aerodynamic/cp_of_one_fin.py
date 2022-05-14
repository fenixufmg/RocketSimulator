"""/**
 * @author João Lucas Gomes Alencar
 * @email alencarj2021@mail.com
 * @create date 2022-04-15 20:03:19
 * @modify date 2022-04-19 16:20:30
 * @desc returns the center of pressure of a single fin
 */
"""

def cp_of_one_fin(fin_geometry: str, xt: float, rc: float, rt: float):
    """
    Args:
        xt: position x of the fin tip measured from the (0,0) point
        rc: root_chord
        rt: tip_chord
        fin_geometry: Geometry of the fin
        
        c: Mean aerodynamic chord length
        XmacLe: Effective leading edge location
        XleY: Leading edge position at spanwise position Y
        cY: chord length of one fin
        Afin: Area of one side of the fin
    Returns:
        Xf: Center os pressure position of the fin 
    """
    if fin_geometry == "trapezoidal":
        return xt / 3 * (rc + 2 * rt) / (rc + rt) + (rc**2 + rt**2 + rc * rt) / (6 * rc + rt)
    
    if fin_geometry == "elliptical":
        return rc * 0.288


