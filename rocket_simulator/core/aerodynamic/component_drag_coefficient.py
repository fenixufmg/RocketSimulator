"""
/**
 * @author João Lucas Gomes Alencar
 * @email alencarj2021@mail.com
 * @create date 2022-04-09 13:55:30
 * @modify date 2022-04-09 14:12:56
 * @desc returns the sum of drag coefficients of each component
 */
 """
 
def components_drag_coefficient(drag_coefficient_T: float, reference_area_T: float, reference_area: float) -> float:
    CDc += reference_area_T * drag_coefficient_T / reference_area
    return CDc
    