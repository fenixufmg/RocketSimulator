from core.physics.vector import Vector

class BodyCoordinateSystem():
    def __init__(self):
        self.__x_axis = Vector(1,0,0)
        self.__y_axis = Vector(0,1,0)
        self.__z_axis = Vector(0,0,1)

    def getLookingDirection(self):
        return self.__z_axis # já é unitario

    def rotate(self, angular_displacement:Vector):
        self.__x_axis = Vector.rotateAroundAxis(self.__x_axis, angular_displacement, angular_displacement.magnitude())
        self.__y_axis = Vector.rotateAroundAxis(self.__y_axis, angular_displacement, angular_displacement.magnitude())
        self.__z_axis = Vector.rotateAroundAxis(self.__z_axis, angular_displacement, angular_displacement.magnitude())