from math import sin, radians
from single_fin_normal_force_coefficient import single_fin_normal_force_coefficient as CNa1
"""/**
 * @author João Lucas Gomes Alencar
 * @email alencarj2021@mail.com
 * @create date 2022-04-15 20:03:19
 * @modify date 2022-05-03 12:53:47
 * @desc returns the normal force coefficient derivative for all the fins
 */
"""

def normal_force_coefficient_derivative(CNa1: float, D: float, N: int, Ntot: int):
    """
    Args:
        CNa1: Normal force coefficient of one fin
        D:  Dihedral angle between a fin and the direction of airflow
        N: Number of fins
        Ntot:  total number of parallel fins that have an interference effect
        sumOfD: Sum of the squared sin of Dihedral angles
    Returns:
        CNan: Normal force coefficient derivative
    """
    sumOfD = 0
    for value in range(N):
        sumOfD += (sin(radians(D))) ** 2

    CNan = sumOfD * CNa1 
    
    if Ntot > 0 and Ntot <= 4:
        return CNan

    elif Ntot == 5:
        return CNan * 0.948

    elif Ntot == 6:
        return CNan * 0.913

    elif Ntot == 7:
        return CNan * 0.854

    elif Ntot == 8:
        return CNan * 0.810
    
    elif Ntot > 8:
        return CNan * 0.750

print(normal_force_coefficient_derivative(4, 90, 5, 40))
