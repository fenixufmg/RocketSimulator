from utils.constants import Constants


class Utils():
    """ Classe utilitária que contem qualquer função repetitiva que pode ser usada em vários lugares.
    """
    @staticmethod
    def radiansToDegrees(radians:float) -> float:
        return radians * 180/Constants.PI.value

    @staticmethod
    def degreesToRadians(degrees:float) -> float:
        return degrees * Constants.PI.value / 180