from core.physics.vector import Vector

class BodyCoordinateSystem():
    def __init__(self):
        self.__x_axis = Vector(1,0,0)
        self.__y_axis = Vector(0,1,0)
        self.__z_axis = Vector(0,0,1)
        self.__origin = Vector(0,0,0)

    def getLookingDirection(self):
        return self.__z_axis

    def rotate(self):
        pass

    def move(self, displacement:Vector):
        self.__origin = Vector.sum(self.__origin, displacement)