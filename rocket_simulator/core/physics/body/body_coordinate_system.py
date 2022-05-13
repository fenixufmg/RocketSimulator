from core.physics.vector import Vector

class BodyCoordinateSystem():
    def __init__(self):
        """Classe que representa o sistema de coordenadas do foguete (sistema local). Seu eixo Z está sempre na
        direção e sentido da orientação do foguete.

        Fields:
        __x_axis (Vector): Eixo x.
        __y_axis (Vector): Eixo y.
        __z_axis (Vector): Eixo z.
        """
        self.__x_axis = Vector(1,0,0)
        self.__y_axis = Vector(0,1,0)
        self.__z_axis = Vector(0,0,1)

    def getLookingDirection(self) -> Vector:
        """Retorna o eixo Z (orientação do foguete).

        Returns:
            Vector: Orientação do foguete.
        """
        return self.__z_axis # já é unitario

    def rotate(self, angular_displacement:Vector) -> None:
        """Rotaciona o sistema de coordenadas dado um deslocamento angular.

        Args:
             angular_displacement (Vector): Deslocamento angular.
        """
        self.__x_axis = Vector.rotateAroundAxis(self.__x_axis, angular_displacement, angular_displacement.magnitude())
        self.__y_axis = Vector.rotateAroundAxis(self.__y_axis, angular_displacement, angular_displacement.magnitude())
        self.__z_axis = Vector.rotateAroundAxis(self.__z_axis, angular_displacement, angular_displacement.magnitude())