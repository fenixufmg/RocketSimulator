"""
/**
 * @author João Lucas Gomes Alencar
 * @email alencarj2021@mail.com
 * @create date 2022-02-24 14:56:52
 * @modify date 2022-04-01 21:35:19
 * @desc returns the mean aerodynamic chord of trapezoidal fin
 */
 """

def mean_aerodynamic_chord_length(root_chord: float, tip_chord: float):
    return 2 * (root_chord + tip_chord - (root_chord * tip_chord) / (root_chord + tip_chord)) / 3
    #Only for trapezoidal fins (It is necessary to include for free form fins and elliptical fins)


