from core.physics.forces.force import Force
from core.physics.vector import Vector
from core.physics.body.application_point import ApplicationPoint
from core.physics.body.body_coordinate_system import BodyCoordinateSystem

class RigidBody:
    def __init__(self, delimitation_points:list, mass:float, volume:float, moment_of_inertia:float, cp:Vector):
        """Classse que representa um corpo rígido, seu estado é alterável.

        Args:
            delimitation_points (list): Lista que contem o ponto que limita o corpo superiormente e o ponto que limita
            o corpo inferiormente (nessa ordem).
            mass (float): Massa do corpo.
            volume (float): Volume do corpo.
            moment_of_inertia (float): Momento de inércia do corpo.
            cp (Vector): Centro de pressão do corpo.

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
        self.__cg = Vector(0,0,0) # também é variável de estado, mas tem tratamento diferente (estruturas)

        # variaveis de estado
        self.__velocity = Vector(0,0,0)
        self.__total_acceleration = Vector(0,0,0)
        self.__total_displacement = Vector(0,0,0)
        self.__angular_velocity = Vector(0,0,0)
        self.__total_angular_displacement = Vector(0,0,0)

        # sistema de coordenadas local
        self.__coordinate_system = BodyCoordinateSystem()
        self.__validate()

    def __validate(self):
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

    def test(self):
        self.__total_displacement += Vector(1,0,0)
        self.__cg += self.__total_displacement
        self.__cp += self.__total_displacement

    def __applyForceOnCg(self, force:Force, duration:int):
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

    def __rotateAroundCg(self, force:Force, duration:int, lever:Vector): # lever deve apontar para o cg
        torque = Vector.crossProduct(force, lever)
        angular_acceleration = torque * (1/self.__moment_of_inertia)

        angular_displacement = self.__angular_velocity * duration + (angular_acceleration * duration**2) * 0.5
        angular_velocity = self.__angular_velocity + angular_acceleration * duration

        self.__angular_velocity = angular_velocity
        self.__total_angular_displacement += angular_displacement # possivelmente inutil
        
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
            
    def __applyForceOnCp(self, force:Force, duration:int): # chama o move()
        distance_to_cp = self.getCpCgDistance() # aponta para o cg
        self.__applyForceOnCg(force, duration)
        self.__rotateAroundCg(force, duration, distance_to_cp)

    def __applyForceOnPoint(self, force:Force ,duration:int): 
        cg_offset = self.getCpCgDistance().unitVector() * force.cgOffset() # transforma o cgoffset em vetor
        cg_offset += self.__total_displacement

        distance_to_application_point = self.__cg - cg_offset 
        self.__applyForceOnCg(force, duration)
        self.__rotateAroundCg(force, duration, distance_to_application_point)

    def __isForceInsideBody(self, force:Force):
        length_up = (self.__delimitation_points[0] - self.__cg).magnitude()
        length_up = round(length_up, 5)

        length_down = (self.__delimitation_points[1] - self.__cg).magnitude()
        length_down = round(length_down, 5)
        
        cg_offset = force.cgOffset()

        if(cg_offset < 0 and abs(cg_offset) > length_down):
            raise ValueError(f"Force applied bellow body, cg_offset: {force.cgOffset()}, length down: {length_down}")
        if(cg_offset > 0 and abs(cg_offset) > length_up):
            raise ValueError(f"Force applied above body, cg_offset: {force.cgOffset()}, length up: {length_up}")

    def applyForce(self, force:Force, duration:int):
        if force.applicationPoint() == ApplicationPoint.CG:
            self.__applyForceOnCg(force, duration)
        
        elif force.applicationPoint() == ApplicationPoint.CP:
            self.__applyForceOnCp(force, duration)
        
        elif force.applicationPoint() == ApplicationPoint.CUSTOM:
            self.__isForceInsideBody(force)
            self.__applyForceOnPoint(force, duration)

        else:
            raise ValueError("Invalid application point")

    def applyForces(self, forces:list, duration:int):
        self.__total_acceleration = Vector(0,0,0) # reseta a aceleracão
        for force in forces:
            self.applyForce(force, duration)

    # ========================= getters ========================= #
    def cg(self) -> Vector:
        return self.__cg

    def cp(self) -> Vector:
        return self.__cp

    def velocity(self) -> Vector:
        return self.__velocity

    def acceleration(self) -> Vector:
        return self.__total_acceleration

    def angularVelocity(self) -> Vector:
        return self.__angular_velocity

    def volume(self) -> float:
        return self.__volume

    def mass(self) ->float:
        return self.__mass

    def getLookingDirection(self) -> Vector:
        return self.__coordinate_system.getLookingDirection()

    def getCpCgDistance(self) -> Vector: # aponta para o cg
        return self.__cg - self.__cp  
    # ========================= getters ========================= #

    # ========================= setters ========================= #
    def setMass(self, mass):
        self.__mass = mass
    # ========================= setters ========================= #
    