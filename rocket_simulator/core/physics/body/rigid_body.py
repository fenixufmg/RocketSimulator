from core.physics.forces.force import Force
from core.physics.vector import Vector
from core.physics.body.application_point import ApplicationPoint
from core.physics.body.body_coordinate_system import BodyCoordinateSystem

class RigidBody:
    def __init__(self, delimitation_points:list, mass:float, volume:float, moment_of_inertia:float, cg:Vector, cp:Vector):
        """Classse que representa um corpo rígido, seu estado é alterável. O corpo é entendido como o conjunto de pontos
        que o representa, que no caso são o CG, CP, o ponto de limitação superior e o ponto de limitação inferior

        Args:
            delimitation_points (list): Lista que contem o ponto que limita o corpo superiormente e o ponto que limita
            o corpo inferiormente (nessa ordem).
            mass (float): Massa do corpo.
            volume (float): Volume do corpo.
            moment_of_inertia (float): Momento de inércia do corpo.
            cp (Vector): Centro de pressão do corpo.
            cg (Vector): Centro de massa do corpo.

        Fields:
            __cg (Vector): Centro de massa do corpo, o valor inicial é sempre na origem.
            __velocity (Vector): Velocidade de translação do corpo.
            __total_displacement (Vector): Posição do corpo em relação a origem.
            __total_acceleration (Vector): Aceleração resultante.
            __angular_velocity (Vector): Velocidade angular.
            __cordinate_system (BodyCoordinateSystem): Sistema de coordenadas relativo (do corpo).
        """
        # variaveis que são definidas fora do escopo do classe
        self.__delimitation_points = delimitation_points # lista de vetores que limitam o corpo (apenas 2, topo e base)
        self.__volume = volume
        self.__mass = mass # também é variável de estado
        self.__moment_of_inertia = moment_of_inertia # também é variável de estado
        self.__cp = cp # também é variável de estado, mas tem tratamento diferente (estruturas)
        self.__cg = cg # também é variável de estado, mas tem tratamento diferente (estruturas)

        # variaveis de estado
        self.__velocity = Vector(0,0,0)
        self.__total_acceleration = Vector(0,0,0)
        self.__total_displacement = Vector(0,0,0)
        self.__angular_velocity = Vector(0,0,0)

        # sistema de coordenadas local
        self.__coordinate_system = BodyCoordinateSystem()
        self.__validate()

    def __validate(self) -> None:
        """Valida as entradas do construtor.

        Raises:
            ValueError: Levantado se os pontos estão na ordem errada ou se estão em número errado.
        """
        if len(self.__delimitation_points) != 2:
            raise ValueError("2 delimitation points should be specified") 
        if self.__delimitation_points[0].magnitudeRelativeTo(Vector(0,0,1)) < 0:
            raise ValueError("Top delimitation point and bottom are inverted")
        if self.__delimitation_points[1].magnitudeRelativeTo(Vector(0,0,1)) > 0:
            raise ValueError("Top delimitation point and bottom are inverted")

    def __applyForceOnCg(self, force:Force, duration:float) -> None:
        """Aplica uma força no cg durante uma determinada duração, oque resulta em um translação do corpo.

        Args:
            force (Force): Força que será aplicada.
            duration (float): Duração de tempo no qual a força será aplicada.
        """
        acceleration = force * (1/self.__mass)
        self.__total_acceleration += acceleration

        displacement = self.__velocity*duration + (acceleration * duration**2)*0.5
        velocity = self.__velocity + acceleration*duration # velocidade inicial é a velocidade de um estado antes do atual

        self.__velocity = velocity
        self.__total_displacement += displacement

        # move os pontos
        self.__cg += displacement
        self.__cp += displacement

        for index, delimitation_point in enumerate(self.__delimitation_points):
            self.__delimitation_points[index] += displacement 

    def __rotateAroundCg(self, force:Force, duration:float, lever:Vector) -> None:
        """Rotaciona o corpo em torno do CG.

        Args:
            force (Force): Força de rotação que será aplicada.
            duration (float): Duração de aplicação da força.
            lever (Vector): Braço de alavanca usado para calcular o torque, esse vetor DEVE apontar para o CG.

        """
        torque = Vector.crossProduct(force, lever)
        angular_acceleration = torque * (1/self.__moment_of_inertia)

        angular_displacement = self.__angular_velocity * duration + (angular_acceleration * duration**2) * 0.5
        angular_velocity = self.__angular_velocity + angular_acceleration * duration

        self.__angular_velocity = angular_velocity

        # rotaciona os pontos
        self.__coordinate_system.rotate(angular_displacement)

        self.__cp -= self.__total_displacement # translada para a origem para rotacionar
        self.__cp = Vector.rotateAroundAxis(self.__cp, angular_displacement, angular_displacement.magnitude())
        self.__cp += self.__total_displacement # translada para o ponto antes da rotação
        
        for index, delimitation_point in enumerate(self.__delimitation_points):
            delimitation_point -= self.__total_displacement  # translada para a origem para rotacionar
            delimitation_point = Vector.rotateAroundAxis(delimitation_point, angular_displacement, angular_displacement.magnitude())
            delimitation_point += self.__total_displacement # translada para o ponto antes da rotação

            self.__delimitation_points[index] = delimitation_point
            
    def __applyForceOnCp(self, force:Force, duration:float) -> None:
        """Aplica uma força no CP durante uma determinada duração, oque resulta em uma translação e em uma rotação.

        Args:
            force (Force): Força que será aplicada no CP.
            duration (float): Duração de aplicação da força.
        """
        distance_to_cp = self.getCpCgDistance() # aponta para o cg
        self.__applyForceOnCg(force, duration)
        self.__rotateAroundCg(force, duration, distance_to_cp)

    def __applyForceOnPoint(self, force:Force ,duration:float):
        """Aplica uma força em um ponto durante uma determinada duração, oque resulta em uma translação e em uma rotação.

        Args:
            force (Force): Força que será aplicada.
            duration (float): Duração de aplicação da força.
        """
        cg_offset = self.getCpCgDistance().unitVector() * force.cgOffset() # transforma o cgoffset em vetor
        cg_offset += self.__total_displacement

        distance_to_application_point = self.__cg - cg_offset 
        self.__applyForceOnCg(force, duration)
        self.__rotateAroundCg(force, duration, distance_to_application_point)

    def __isForceInsideBody(self, force:Force) -> None:
        """Verifica se o ponto de aplicação da força está dentro do corpo.

        Args:
            force (Force): Força que terá seu ponto de aplicação testado.

        Raises:
            ValueError: Levantado se o ponto de aplicação estiver fora do corpo.
        """
        length_up = (self.__delimitation_points[0] - self.__cg).magnitude()
        length_up = round(length_up, 5)

        length_down = (self.__delimitation_points[1] - self.__cg).magnitude()
        length_down = round(length_down, 5)
        
        cg_offset = force.cgOffset()

        if(cg_offset < 0 and abs(cg_offset) > length_down):
            raise ValueError(f"Force applied bellow body, cg_offset: {force.cgOffset()}, length down: {length_down}")
        if(cg_offset > 0 and abs(cg_offset) > length_up):
            raise ValueError(f"Force applied above body, cg_offset: {force.cgOffset()}, length up: {length_up}")

    def applyForce(self, force:Force, duration:float) -> None:
        """Aplica uma força no corpo durante uma determinada duração, seu ponto de aplicação será processado dentro
        do método.

        Args:
            force (Force): Força a ser aplicada.
            duration (float): Duração de aplicação da força.

        Raises:
            ValueError: Levantado se o ponto de aplicação não for um dos campos do Enum ApplicationPoint.
        """
        if force.applicationPoint() == ApplicationPoint.CG:
            self.__applyForceOnCg(force, duration)
        
        elif force.applicationPoint() == ApplicationPoint.CP:
            self.__applyForceOnCp(force, duration)
        
        elif force.applicationPoint() == ApplicationPoint.CUSTOM:
            self.__isForceInsideBody(force)
            self.__applyForceOnPoint(force, duration)

        else:
            raise ValueError("Invalid application point")

    def applyForces(self, forces:list, duration:float) -> None:
        """Aplica um conjunto de forças no corpo durante uma determinada duração.

        Args:
            forces (list[Force]): Lista que contém as forças que serão aplicadas.
            duration (float): Duração de aplicação da força.
        """
        self.__total_acceleration = Vector(0,0,0) # reseta a aceleracão resultante
        for force in forces:
            self.applyForce(force, duration)

    # ========================= getters ========================= #
    def cg(self) -> Vector:
        """Retorna o CG.

        Returns:
             Vector: CG.
        """
        return self.__cg

    def cp(self) -> Vector:
        """Retorna o CP.

        Returns:
             Vector: CP.
        """
        return self.__cp

    def velocity(self) -> Vector:
        """Retorna a velocidade.

        Returns:
             Vector: Velocidade.
        """
        return self.__velocity

    def acceleration(self) -> Vector:
        """Retorna a aceleração.

        Returns:
             Vector: Aceleração.
        """
        return self.__total_acceleration

    def angularVelocity(self) -> Vector:
        """Retorna a velocidade angular.

        Returns:
             Vector: Velocidade angular.
        """
        return self.__angular_velocity

    def volume(self) -> float:
        """Retorna o volume.

        Returns:
             float: Volume.
        """
        return self.__volume

    def mass(self) -> float:
        """Retorna a massa.

        Returns:
             float: Massa.
        """
        return self.__mass

    def getLookingDirection(self) -> Vector:
        """Retorna o vetor que representa a orientação do foguete.

        Returns:
             Vector: Orientação do foguete.
        """
        return self.__coordinate_system.getLookingDirection()

    def getCpCgDistance(self) -> Vector:
        """Retorna o vetor que representa a distância entre o CP e o CG (apontando para o CG)

        Returns:
             Vector: Distância entre CP e CG.
        """
        return self.__cg - self.__cp  
    # ========================= getters ========================= #

    # ========================= setters ========================= #
    def setMass(self, mass:float)-> None:
        """Iguala a massa ao novo valor do parâmetro.

        Args:
             mass (float): Novo valor de massa.
        """
        self.__mass = mass

    def setCp(self, cp:Vector) -> None:
        """Iguala o Cp ao novo valor do parâmetro.

        Args:
             cp (Vector): Novo valor do Cp.
        """
        self.__cp = cp

    def setCg(self, cg:Vector) -> None:
        """Iguala o Cg ao novo valor do parâmetro.

        Args:
             cg (Vector): Novo valor do Cg.
        """
        self.__cp = cg
        
    # ========================= setters ========================= #
    