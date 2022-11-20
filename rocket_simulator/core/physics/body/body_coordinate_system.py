from core.physics.vector import Vector

class BodyCoordinateSystem():
    def __init__(self):
        """Class that represents rocket's coordinate system (local system). Its Z axis is always in 
        the direction and way of rocket's orientation.

        Fields:
        __x_axis (Vector): Eixo x.
        __y_axis (Vector): Eixo y.
        __z_axis (Vector): Eixo z.
        """
        self.__x_axis = Vector(1,0,0)
        self.__y_axis = Vector(0,1,0)
        self.__z_axis = Vector(0,0,1)

    def getLookingDirection(self) -> Vector:
        """Returns Z axis (rocket's orientation).

        Returns:
            Vector: Rocket's orientation.
        """
        return self.__z_axis # já é unitario

    def setLookingDirection(self, looking_direction:Vector):
        """Returns Z axis (rocket's orientation).

        Returns:
            Vector: Rocket's orientation.
        """
        angle = Vector.angleBetweenVectors(self.__z_axis, looking_direction)
        axis = Vector.crossProduct(self.__z_axis, looking_direction)

        self.__x_axis = Vector.rotateAroundAxis(self.__x_axis, axis, angle)
        self.__y_axis = Vector.rotateAroundAxis(self.__y_axis, axis, angle)
        self.__z_axis = Vector.rotateAroundAxis(self.__z_axis, axis, angle)

    def rotate(self, angular_displacement:Vector) -> None:
        """Rotates the coordinate system based on a gives angular shift. 

        Args:
             angular_displacement (Vector): Deslocamento angular.
        """
        self.__x_axis = Vector.rotateAroundAxis(self.__x_axis, angular_displacement, angular_displacement.magnitude())
        self.__y_axis = Vector.rotateAroundAxis(self.__y_axis, angular_displacement, angular_displacement.magnitude())
        self.__z_axis = Vector.rotateAroundAxis(self.__z_axis, angular_displacement, angular_displacement.magnitude())
