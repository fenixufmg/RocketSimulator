from utils.constants import Constants

class Utils():
    @staticmethod
    def radiansToDegrees(radians:float) -> float:
        return radians * 180/Constants.PI.value

    @staticmethod
    def degreesToRadians(degrees:float) -> float:
        return degrees * Constants.PI.value / 180