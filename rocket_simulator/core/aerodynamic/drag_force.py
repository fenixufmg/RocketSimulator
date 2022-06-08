"""
/**
 * @author João Lucas Gomes Alencar
 * @email alencarj2021@mail.com
 * @create date 2022-04-09 13:55:30
 * @modify date 2022-06-07 22:33:07
 * @desc returns drag force
 */
 """

def drag_force(rho: float, v: float, CD: float, Aref: float) -> float:
    """
    Args:
        rho: mass density of the air
        v: The rocket velocity
        CD: Total drag coefficient
        Aref: Reference area
    Returns:
        FD: Drag force 
    """
    FD = 0.5 * rho * pow(v, 2) * CD * Aref
    
    return FD