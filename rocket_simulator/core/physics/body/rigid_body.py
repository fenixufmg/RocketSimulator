from core.physics.forces.force import Force
from core.physics.vector import Vector
from core.physics.body.application_point import ApplicationPoint
from core.physics.body.body_coordinate_system import BodyCoordinateSystem
import numpy as np

class RigidBody:
    def __init__(self, delimitation_points:list, mass:float, volume:float, moment_of_inertia:float, cg:Vector, cp:Vector):
        # variaveis que são definidas fora do escopo do classe
        self.__delimitation_points = delimitation_points # lista de vetores que limitam o corpo
        self.__volume = volume
        self.__mass = mass
        self.__moment_of_inertia = moment_of_inertia
        self.__cp = cp
        self.__cg = cg

        # variaveis de estado
        self.__velocity = Vector(0,0,0)
        self.__total_acceleration = Vector(0,0,0)
        self.__total_displacement = Vector(0,0,0)
        self.__angular_velocity = Vector(0,0,0)
        self.__total_angular_displacement = Vector(0,0,0)

        # sistema de coordenadas local
        self.__coordinate_system = BodyCoordinateSystem()

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

        distance_to_application_point = self.__cg - cg_offset 
        self.__applyForceOnCg(force, duration)
        self.__rotateAroundCg(force, duration, distance_to_application_point)

    def applyForce(self, force:Force, duration:int):
        if force.applicationPoint() == ApplicationPoint.CG:
            self.__applyForceOnCg(force, duration)
        
        elif force.applicationPoint() == ApplicationPoint.CP:
            self.__applyForceOnCp(force, duration)
        
        elif force.applicationPoint() == ApplicationPoint.CUSTOM:
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
    