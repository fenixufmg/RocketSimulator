from core.physics.forces.force import Force
from core.physics.vector import Vector
from core.physics.body.application_point import ApplicationPoint
from core.physics.body.body_coordinate_system import BodyCoordinateSystem


class RigidBody:
    def __init__(self, delimitation_points: list, mass: float, volume: float, moment_of_inertia_function, cg: Vector,
                 cp: Vector):
        """Classse que representa um corpo rígido, seu estado é alterável. O corpo é entendido como o conjunto de pontos
        que o representa, que no caso são o CG, CP, o ponto de limitação superior e o ponto de limitação inferior

        Args:
            delimitation_points (list): Lista que contem o ponto que limita o corpo superiormente e o ponto que limita
            o corpo inferiormente (nessa ordem).
            mass (float): Massa do corpo.
            volume (float): Volume do corpo.
            moment_of_inertia_function (function): Função que calcula o momento de inércia do corpo.
            cp (Vector): Centro de pressão do corpo.
            cg (Vector): Centro de massa do corpo.

        Fields:
            cg (Vector): Centro de massa do corpo, o valor inicial é sempre na origem.
            velocity (Vector): Velocidade de translação do corpo.
            total_displacement (Vector): Posição do corpo em relação a origem.
            total_acceleration (Vector): Aceleração resultante.
            total_angular_acceleration (Vector): Aceleração angular resultante.
            angular_velocity (Vector): Velocidade angular.
            cordinate_system (BodyCoordinateSystem): Sistema de coordenadas relativo (do corpo).
        """
        # variaveis que são definidas fora do escopo do classe
        self.delimitation_points = delimitation_points  # lista de vetores que limitam o corpo (apenas 2, topo e base)
        self.volume = volume
        self.mass = mass  # também é variável de estado
        self.moment_of_inertia = None  # também é variável de estado
        self.moment_of_inertia_function = moment_of_inertia_function
        self.cp = cp  # também é variável de estado, mas tem tratamento diferente (estruturas)
        self.cg = cg  # também é variável de estado, mas tem tratamento diferente (estruturas)

        # variaveis de estado
        self.velocity = Vector(0, 0, 0)
        self.total_acceleration = Vector(0, 0, 0)
        self.total_angular_acceleration = Vector(0, 0, 0)
        self.total_displacement = Vector(0, 0, 0)
        self.angular_velocity = Vector(0, 0, 0)
        self.is_on_ground = False

        # sistema de coordenadas local
        self.cordinate_system = BodyCoordinateSystem()
        self.__validate()

    def __validate(self) -> None:
        """Valida as entradas do construtor.

        Raises:
            ValueError: Levantado se os pontos estão na ordem errada ou se estão em número errado.
        """
        if len(self.delimitation_points) != 2:
            raise ValueError("2 delimitation points should be specified")
        if self.delimitation_points[0].magnitudeRelativeTo(Vector(0, 0, 1)) < 0:
            raise ValueError("Top delimitation point and bottom are inverted")
        if self.delimitation_points[1].magnitudeRelativeTo(Vector(0, 0, 1)) > 0:
            raise ValueError("Top delimitation point and bottom are inverted")

    def _isOnGround(self) -> bool:
        """Verifica se o corpo está no chão

        Returns:
            (bool): True se está no chão
        """
        if self.cg.z() < 0:
            self.is_on_ground = True
            return True
        self.is_on_ground = False
        return False

    def centerOnOrigin(self):
        """Centraliza o cg do corpo na origem (0,0,0).
        """
        displacement = Vector(-self.cg.x(), - self.cg.y(), -self.cg.z())
        self.move(displacement, ignore_ground=True)

    def move(self, displacement: Vector, ignore_ground=False):
        """" Move todos os pontos que representam um corpo com base em um deslocamento se o corpo não estiver no chão

        Args:
            displacement (Vector): Vetor deslocamento
            ignore_ground (bool): Se verdadeiro pode mover corpo para baixo do solo
        """
        # if ignore_ground is False and self._isOnGround():
        #     self.velocity = Vector(0,0,0)
        #     self.total_acceleration = Vector(0,0,0)
        #     self.angular_velocity = Vector(0,0,0)
        #     self.cg.setZ(0.1)
        #     return

        self.cg += displacement
        self.cp += displacement

        for index, delimitation_point in enumerate(self.delimitation_points):
            self.delimitation_points[index] += displacement

    def rotate(self, angular_displacement: Vector, axis_displacement: Vector = Vector(0, 0, 0)):
        """Rotaciona o corpo.

        Args:
            angular_displacement (Vector): Vetor que representa a rotação.
            axis_displacement (Vector): Vetor que desloca o eixo de rotação padrão (cg).
        """
        initial_position = self.cg
        self.centerOnOrigin()

        if axis_displacement != Vector(0, 0, 0):
            self.move(axis_displacement)
            self.cg = Vector.rotateAroundAxis(self.cg, angular_displacement, angular_displacement.magnitude())

        self.cordinate_system.rotate(angular_displacement)
        self.cp = Vector.rotateAroundAxis(self.cp, angular_displacement, angular_displacement.magnitude())
        for index, delimitation_point in enumerate(self.delimitation_points):
            delimitation_point = Vector.rotateAroundAxis(delimitation_point, angular_displacement,
                                                         angular_displacement.magnitude())
            self.delimitation_points[index] = delimitation_point

        self.move(initial_position - axis_displacement)

    def applyForce(self, force: Force, duration: float):
        """Aplica uma força no cg durante uma determinada duração, oque resulta em um translação do corpo.

        Args:
            force (Force): Força que será aplicada.
            duration (float): Duração de tempo no qual a força será aplicada.
        """
        self.total_acceleration = force * (1 / self.mass)

        displacement = self.velocity * duration + (self.total_acceleration * duration ** 2) * 0.5
        self.velocity += self.total_acceleration * duration  # velocidade inicial é a velocidade de um estado antes do atual

        self.total_displacement += displacement

        # move os pontos
        self.move(displacement)

    def applyTorque(self, torque: Vector, duration: float):
        """Aplica torque ao corpo durante uma determinada duração. Somente deslocalmento angular
        é gerado ao se utilizar esse método. É subentendido que todas as forças que geram torque atuam no CP.

        Args:
            torque (Vector): Torque que será aplicado.
            duration (float): Duração de aplicação da força.
        """
        
        self.moment_of_inertia = self.moment_of_inertia_function(self.getCpCgDistance().magnitude()) # momento de inercia no cp
        self.total_angular_acceleration = torque * (1 / self.moment_of_inertia)

        angular_displacement = self.angular_velocity * duration + (self.total_angular_acceleration * duration ** 2) * 0.5
        self.angular_velocity += self.total_angular_acceleration * duration

        # rotaciona os pontos
        self.rotate(angular_displacement)

    # ========================= getters ========================= #
    def getLookingDirection(self) -> Vector:
        """Retorna o vetor que representa a orientação do corpo.

        Returns:
             Vector: Orientação do corpo.
        """
        return self.cordinate_system.getLookingDirection()

    def getCpCgDistance(self) -> Vector:
        """Retorna o vetor que representa a distância entre o CP e o CG (apontando para o CG), 
        sua direção acompanha a direção (orientação) do corpo.

        Returns:
             Vector: Distância entre CP e CG.
        """
        return self.cg - self.cp

    def getTipDistanceToCp(self) -> Vector:
        """Retorna o vetor que representa a distância entre a ponta superior e o CP (apontando para o CP), 
        sua direção acompanha a direção (orientação) do corpo.

        Returns:
             Vector: Distância entre a ponta superior e o CP.
        """
        return self.cp - self.delimitation_points[0]

    def getTipDistanceToCg(self) -> Vector:
        """Retorna o vetor que representa a distância entre a ponta superior e o CG (apontando para o CG),
         sua direção acompanha a direção (orientação) do corpo.

        Returns:
             Vector: Distância entre a ponta superior e o CG.
        """
        return self.cg - self.delimitation_points[0]

    def getTipToBaseDistance(self) -> Vector:
        """Retorna o vetor que representa a distância entre a ponta superior e a ponta inferior (apontando
         para a ponta inferior), sua direção acompanha a direção (orientação) do corpo.

        Returns:
            Vector: Distância entre a ponta superior e a ponta inferior.
        """
        return self.delimitation_points[1] - self.delimitation_points[0]

    def getTip(self) -> Vector:
        """Retorna o vetor posição da ponta do corpo.

        Returns:
            Vector: Vetor posição.
        """
        return self.delimitation_points[0]

    def getBase(self) -> Vector:
        """Retorna o vetor posição da base do corpo.

        Returns:
            Vector: Vetor posição.
        """
        return self.delimitation_points[1]

    # ========================= getters ========================= #

    # ========================= setters ========================= #
    def setCp(self, cp: Vector) -> None:
        """Iguala o Cp ao novo valor do parâmetro.

        Args:
             cp (Vector): Novo valor do Cp.
        """
        self.cp = cp

    def setCg(self, cg: Vector) -> None:
        """Iguala o Cg ao novo valor do parâmetro.

        Args:
             cg (Vector): Novo valor do Cg.
        """
        self.cp = cg

    # ========================= setters ========================= #
