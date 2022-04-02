"""
/**
 * @author [author]
 * @email [example@mail.com]
 * @create date 2022-02-24 14:56:52
 * @modify date 2022-04-01 21:35:19
 * @desc [description]
 */
 """

def mean_aerodynamic_chord_length(root_chord: float, tip_chord: float):
    return 2 * (root_chord + tip_chord - (root_chord * tip_chord) / (root_chord + tip_chord)) / 3
    #Only for trapezoidal fins (Need to include for free form fins and elliptical fins)


