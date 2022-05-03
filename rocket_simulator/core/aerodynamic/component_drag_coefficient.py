"""
/**
 * @author João Lucas Gomes Alencar
 * @email alencarj2021@mail.com
 * @create date 2022-04-09 13:55:30
 * @modify date 2022-05-03 13:31:28
 * @desc returns the sum of drag coefficients of each component
 */
 """
 
def components_drag_coefficient(CDt: float, At: float, Aref: float) -> float:
    """
    Args:
        At: Refence area of T
        CDt: Drag coefficient of T
        Aref: Reference area
    Returns:
        CDc: Pressure drag coefficient of the component
    """
    CDc += At * CDt / Aref
    return CDc
    