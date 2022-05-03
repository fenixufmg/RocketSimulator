"""
/**
 * @author João Lucas Gomes Alencar
 * @email alencarj2021@mail.com
 * @create date 2022-02-24 14:56:52
 * @modify date 2022-05-03 13:47:31
 * @desc returns the mean aerodynamic chord of trapezoidal fin
 */
 """

def mean_aerodynamic_chord_length(rc: float, rt: float):
    """
    Args:
        rc: root_chord
        rt: tip_chord
    Returns:
        C: Mean aerodynamic chord
    """
    return 2 * (rc + rt - (rc * rt) / (rc + rt)) / 3
    #Only for trapezoidal fins (It is necessary to include for free form fins and elliptical fins)


