from enum import Enum

class ApplicationPoint(Enum):
    """Enum que representa o ponto de aplicação de uma força.
    """
    CG = 1
    CP = 2
    CUSTOM = 3