class Vector2d:
    def __init__(self, x, y, orientation):
        self.__x = x
        self.__y = y
        self.__orientation = orientation
        self.__magnitude = self.__calculateMagnitude()

    def __calculateMagnitude(self):
        pass

    def x(self):
        return self.__x
    
    def y(self):
        return self.__y

    def orientation(self):
        return self.__orientation

    def magnitude(self):
        return self.__magnitude