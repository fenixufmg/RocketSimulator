from multiprocessing.sharedctypes import Value
from core.physics.point import Point
from core.physics.forces.force import Force
from core.physics.vector import Vector
from core.physics.body.application_point import ApplicationPoint
from core.physics.body.body_coordinate_system import BodyCoordinateSystem
import numpy as np

class RigidBody:
    def __init__(self, delimitation_points, material):
        self.__delimitation_points = delimitation_points
        self.__material = material
        self.__volume = self.__calculateVolume()
        self.__mass = self.__calculateMass()
        self.__moment_of_inertia = self.__calculateMomementOfInertia()

        self.__velocity = Vector(0,0,0)
        self.__angular_velocity = Vector(0,0,0)

        self.__cp = self.__calculateCp()
        self.__cg = self.__calculateCg()

        self.__total_displacement = Vector(0,0,0)
        self.__total_angular_displacement = Vector(0,0,0)

        self.__coordinate_system = BodyCoordinateSystem()

    def __calculateVolume(self):
        pass

    def __calculateMass(self):
        # return self.__material.density() * self.__volume
        return 2

    def __calculateMomementOfInertia(self):
        return 1

    def __calculateCp(self) -> Vector: # mudar
        return Vector(0,0,-1)

    def __calculateCg(self) -> Vector: # mudar
        return Vector(0,0,0)

    def __applyDisplacement(self, point:Vector): # desnecessario?
        point = Vector.rotateAroundAxis(point, self.__total_angular_displacement, self.__total_angular_displacement.magnitude())
        return point + self.__total_displacement

    def cg(self) -> Vector:
        # return self.__applyDisplacement(self.__cg)
        return self.__cg

    def cp(self) -> Vector:
        # return self.__applyDisplacement(self.__cp)
        return self.__cp

    def velocity(self) -> Vector:
        return self.__velocity

    def angularVelocity(self) -> Vector:
        return self.__angular_velocity

    def volume(self) -> float:
        return self.__volume

    def setMass(self, mass):
        self.__mass = mass

    def mass(self) ->float:
        return self.__mass

    def test(self):
        self.__total_displacement += Vector(1,0,0)
        self.__cg += self.__total_displacement
        self.__cp += self.__total_displacement

    def getCpCgDistance(self): # aponta para o cg
        return self.__cg - self.__cp  

    def __applyForceOnCg(self, force:Force, duration:int):
        acceleration = force * (1/self.__mass)

        displacement = self.__velocity*duration + (acceleration * duration**2)*0.5
        velocity = self.__velocity + acceleration*duration # velocidade inicial é a velocidade de um estado antes do atual

        self.__velocity = velocity
        self.__total_displacement += displacement

        self.__cg += displacement
        self.__cp += displacement
        # mover os delimitation points tambem 

    def rotateAroundCg(self, force:Force, duration:int, lever:Vector): # lever deve apontar para o cg
        torque = Vector.crossProduct(force, lever)
        angular_acceleration = torque * (1/self.__moment_of_inertia)

        angular_displacement = self.__angular_velocity * duration + (angular_acceleration * duration**2) * 0.5
        angular_velocity = self.__angular_velocity + angular_acceleration * duration

        self.__angular_velocity = angular_velocity
        self.__total_angular_displacement = angular_displacement
        
        print(angular_displacement.toList())
        self.__coordinate_system.rotate(angular_displacement)

        self.__cp -= self.__total_displacement # bring to origin to rotate 
        self.__cp = Vector.rotateAroundAxis(self.__cp, angular_displacement, angular_displacement.magnitude())
        self.__cp += self.__total_displacement # translate to original position after rotation
        # mover os delimitation points tambem 

    def __applyForceOnCp(self, force:Force, duration:int): # chama o move()
        distance_to_cp = self.getCpCgDistance() # aponta para o cg
        # self.__applyForceOnCg(force, duration)
        self.__rotateAroundCg(force, duration, distance_to_cp)

    def __applyForceOnPoint(self, force:Force ,duration:int): 
        distance_to_application_point = self.__cg - force.applicationPoint() # aponta para o cg
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

    