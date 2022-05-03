"""
/**
 * @author João Lucas Gomes Alencar
 * @email alencarj2021@mail.com
 * @create date 2022-04-19 16:09:31
 * @modify date 2022-05-02 22:45:50
 * @desc returns the value of the final normal force coefficient derivative of the fins
*/
"""

def final_normal_force_coefficient_derivative(CNan: float, s: float, rt: float) -> float:
    """
    Args:
        CNan: Normal force coefficient derivative
        s: Spanwise length of one fin
        rt: Body radius at the fins position
    Returns:
        CNaTb: final normal force coefficient derivative of the fins
    """
    return (1 + (rt / (s + rt))) * CNan
