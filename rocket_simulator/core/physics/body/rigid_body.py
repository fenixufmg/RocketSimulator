from core.physics.forces.force import Force
from core.physics.vector import Vector
from core.physics.body.application_point import ApplicationPoint
from core.physics.body.body_coordinate_system import BodyCoordinateSystem

class RigidBody:
    def __init__(self, delimitation_points:list, mass:float, volume:float, moment_of_inertia_function, cg:Vector, cp:Vector):
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
            angular_velocity (Vector): Velocidade angular.
            cordinate_system (BodyCoordinateSystem): Sistema de coordenadas relativo (do corpo).
        """
        # variaveis que são definidas fora do escopo do classe
        self.delimitation_points = delimitation_points # lista de vetores que limitam o corpo (apenas 2, topo e base)
        self.volume = volume
        self.mass = mass # também é variável de estado
        self.moment_of_inertia = None # também é variável de estado
        self.moment_of_inertia_function = moment_of_inertia_function
        self.cp = cp # também é variável de estado, mas tem tratamento diferente (estruturas)
        self.cg = cg # também é variável de estado, mas tem tratamento diferente (estruturas)

        # variaveis de estado
        self.velocity = Vector(0,0,0)
        self.total_acceleration = Vector(0,0,0)
        self.total_displacement = Vector(0,0,0)
        self.angular_velocity = Vector(0,0,0)

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
        if self.delimitation_points[0].magnitudeRelativeTo(Vector(0,0,1)) < 0:
            raise ValueError("Top delimitation point and bottom are inverted")
        if self.delimitation_points[1].magnitudeRelativeTo(Vector(0,0,1)) > 0:
            raise ValueError("Top delimitation point and bottom are inverted")

    def move(self, displacement: float):
        """" Move todos os pontos que representam um corpo com base em um deslocamento.

        Args:
            displacement (float): deslocamento
        """
        self.cg += displacement
        self.cp += displacement

        for index, delimitation_point in enumerate(self.delimitation_points):
            self.delimitation_points[index] += displacement

    def __applyForceOnCg(self, force:Force, duration:float) -> None:
        """Aplica uma força no cg durante uma determinada duração, oque resulta em um translação do corpo.

        Args:
            force (Force): Força que será aplicada.
            duration (float): Duração de tempo no qual a força será aplicada.
        """
        acceleration = force * (1/self.mass)
        self.total_acceleration += acceleration

        displacement = self.velocity*duration + (acceleration * duration**2)*0.5
        velocity = self.velocity + acceleration*duration # velocidade inicial é a velocidade de um estado antes do atual

        self.velocity = velocity
        self.total_displacement += displacement

        # move os pontos
        self.move(displacement)

    def __rotateAroundCg(self, force:Force, duration:float, lever:Vector) -> None:
        """Rotaciona o corpo em torno do CG.

        Args:
            force (Force): Força de rotação que será aplicada.
            duration (float): Duração de aplicação da força.
            lever (Vector): Braço de alavanca usado para calcular o torque, esse vetor DEVE apontar para o CG.

        """
        torque = Vector.crossProduct(force, lever)
        angular_acceleration = torque * (1/self.moment_of_inertia)

        angular_displacement = self.angular_velocity * duration + (angular_acceleration * duration**2) * 0.5
        angular_velocity = self.angular_velocity + angular_acceleration * duration

        self.angular_velocity = angular_velocity

        # rotaciona os pontos
        self.cordinate_system.rotate(angular_displacement)

        self.cp -= self.total_displacement # translada para a origem para rotacionar
        self.cp = Vector.rotateAroundAxis(self.cp, angular_displacement, angular_displacement.magnitude())
        self.cp += self.total_displacement # translada para o ponto antes da rotação
        
        for index, delimitation_point in enumerate(self.delimitation_points):
            delimitation_point -= self.total_displacement  # translada para a origem para rotacionar
            delimitation_point = Vector.rotateAroundAxis(delimitation_point, angular_displacement, angular_displacement.magnitude())
            delimitation_point += self.total_displacement # translada para o ponto antes da rotação

            self.delimitation_points[index] = delimitation_point
            
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
        cg_offset += self.total_displacement

        distance_to_application_point = self.cg - cg_offset 
        self.__applyForceOnCg(force, duration)
        self.__rotateAroundCg(force, duration, distance_to_application_point)

    def __isForceInsideBody(self, force:Force) -> None:
        """Verifica se o ponto de aplicação da força está dentro do corpo.

        Args:
            force (Force): Força que terá seu ponto de aplicação testado.

        Raises:
            ValueError: Levantado se o ponto de aplicação estiver fora do corpo.
        """
        length_up = (self.delimitation_points[0] - self.cg).magnitude()
        length_up = round(length_up, 5)

        length_down = (self.delimitation_points[1] - self.cg).magnitude()
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
            self.moment_of_inertia = self.moment_of_inertia_function(0)
            self.__applyForceOnCg(force, duration)
        
        elif force.applicationPoint() == ApplicationPoint.CP:
            self.moment_of_inertia = self.moment_of_inertia_function(self.getCpCgDistance().magnitude())
            self.__applyForceOnCp(force, duration)
        
        elif force.applicationPoint() == ApplicationPoint.CUSTOM:
            self.moment_of_inertia = self.moment_of_inertia_function(abs(force.cgOffset()))
            # self.__isForceInsideBody(force)
            self.__applyForceOnPoint(force, duration)

        else:
            raise ValueError("Invalid application point")

    def applyForces(self, forces:list, duration:float) -> None:
        """Aplica um conjunto de forças no corpo durante uma determinada duração.

        Args:
            forces (list[Force]): Lista que contém as forças que serão aplicadas.
            duration (float): Duração de aplicação da força.
        """
        self.total_acceleration = Vector(0,0,0) # reseta a aceleracão resultante
        for force in forces:
            self.applyForce(force, duration)

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
    def setCp(self, cp:Vector) -> None:
        """Iguala o Cp ao novo valor do parâmetro.

        Args:
             cp (Vector): Novo valor do Cp.
        """
        self.cp = cp

    def setCg(self, cg:Vector) -> None:
        """Iguala o Cg ao novo valor do parâmetro.

        Args:
             cg (Vector): Novo valor do Cg.
        """
        self.cp = cg
        
    # ========================= setters ========================= #
    