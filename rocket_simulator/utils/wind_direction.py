import enum


class WindDirection(enum.Enum): # angles in radians
    """ Enum que tem os valores para a transformação de direções cardeais em radianos, com o norte sendo o angulo 0.
    """
    N = 0
    NE = 0.785

    E = 1.57
    SE = 2.355

    S = 3.14
    SO = 3.925

    W = 4.71
    NW = 5.495