from enum import Enum

class ApplicationPoint(Enum):
    """Enum which represents the application point of a force.
    """
    CG = 1
    CP = 2
    CUSTOM = 3
