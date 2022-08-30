"""/**
 * @author João Lucas Gomes Alencar
 * @email alencarj2021@mail.com
 * @create date 2022-04-15 20:03:19
 * @modify date 2022-05-06 08:49:04
 * @desc returns the pitch damping moment, which prevents the rocket from oscillating.
 */
"""
def pitch_damping_moment_coefficient(N: float, Afin: float, Aref: float, d: float, w: float, v: float, E: float) -> float:
    """
    Args:
        N: Number of fins
        Afin: Area of one side of a fin
        Aref: Reference area
        d: Reference length(The rocket diameter)
        w: Angular velocity
        v: Rocket velocity
        E: Distance from the rotating axis
    Returns:
        Cdamp: Pitch damping moment coefficient
    """
    return 0.6 * (N * Afin * pow(E, 3) * pow(w, 2)) / (Aref * d * pow(v, 2))