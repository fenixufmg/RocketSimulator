"""
/**
 * @author João Lucas Gomes Alencar
 * @email alencarj2021@mail.com
 * @create date 2022-02-24 14:56:52
 * @modify date 2022-05-03 13:47:31
 * @desc returns the mean aerodynamic chord of trapezoidal fin
 */
 """

def mean_aerodynamic_chord_length(fin_geometry: str, rc: float, rt: float):
    """
    Args:
        fin_geometry: Geometry of the fin
        rc: root_chord
        rt: tip_chord
    Returns:
        C: Mean aerodynamic chord
    """
    if fin_geometry == "trapezoidal":
        return 2 * (rc + rt - (rc * rt) / (rc + rt)) / 3

    elif fin_geometry == "elliptical":
        return rc * 0.85

    


