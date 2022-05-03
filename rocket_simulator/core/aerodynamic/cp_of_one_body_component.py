"""/**
 * @author João Lucas Gomes Alencar
 * @email alencarj2021@mail.com
 * @create date 2022-04-15 20:03:19
 * @modify date 2022-05-03 13:28:31
 * @desc returns the center of pressure of a body component(nose, boattail, shoulder)
 */
"""

def cp_of_one_body_component(l: float, Abase: float, Atop: float, V: float) -> float:
    """
    Args:
        l: The component length
        Abase: Area of the base of the body
        Atop: Area of the top of the body
        V: Volume of the component
    Returns:
        Xb: Center os pressure position of the body component
    """
    return  (l * Abase - V) / (Abase - Atop)

