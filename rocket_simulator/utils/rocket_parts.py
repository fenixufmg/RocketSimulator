from enum import Enum


class RocketParts(Enum):
    """ Partes do foguete.
    """
    PARACHUTE = "parachute"
    NOSE = "nose"
    CYLINDRICAL_BODY = "cylidrical body"
    TRANSITION = "transition"
    FIN = "fin"
    MOTOR = "motor"
    ROCKET = "rocket"