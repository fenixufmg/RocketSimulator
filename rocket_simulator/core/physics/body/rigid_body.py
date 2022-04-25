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

        self.__displacement = Vector(0,0,0)
        self.__angular_displacement = Vector(0,0,0)

        self.__coordinate_system = BodyCoordinateSystem()

    def __calculateVolume(self):
        pass

    def __calculateMass(self):
        # return self.__material.density() * self.__volume
        return 2

    def __calculateMomementOfInertia(self):
        return 1

    def __calculateCp(self) -> Vector: # mudar
        return Vector(0,0,0)

    def __calculateCg(self) -> Vector: # mudar
        return Vector(0,0,0)

    def cg(self) -> float:
        cg = Vector.rotateAroundAxis(self.__cg, self.__angular_displacement, self.__angular_displacement.magnitude())
        return cg + self.__displacement

    def cp(self) -> float:
        cp = Vector.rotateAroundAxis(self.__cp, self.__angular_displacement, self.__angular_displacement.magnitude())
        return cp + self.__displacement

    def velocity(self):
        return self.__velocity

    def angularVelocity(self):
        return self.__angular_velocity

    def volume(self) ->float:
        return self.__volume

    def setMass(self, mass):
        self.__mass = mass

    def mass(self) ->float:
        return self.__mass

    def __move(self, displacement:Vector):
        self.__displacement += displacement
        self.__coordinate_system.move(displacement)

    def __applyForceOnCg(self, force:Force, duration:int):
        acceleration = force * (1/self.__mass)

        velocity = self.__velocity + acceleration*duration # velocidade inicial é a velocidade de um estado antes do atual
        displacement = self.__velocity*duration + (acceleration * duration**2)*0.5

        self.__velocity = velocity
        self.__move(displacement)

    def __applyForceOnCp(self, force:Force, duration:int): # chama o move()
        pass

    def __applyForceOnPoint(self, force:Force ,duration:int): # chama o move()
        pass

    def __rotateAroundCg(self, force:Force, duration:int, lever:Vector): # lever deve apontar para o ponto de aplicação
        torque = Vector.crossProduct(force, lever)
        angular_acceleration = torque * (1/self.__moment_of_inertia)
        angular_velocity = self.__angular_velocity + angular_acceleration * duration
        angular_displacement = self.__angular_velocity * duration + (angular_acceleration * duration**2) * 0.5



    
    def applyForce(self, force:Force, duration:int):
        if force.applicationPoint() == ApplicationPoint.CG:
            self.__applyForceOnCg(force, duration)
        
        elif force.applicationPoint() == ApplicationPoint.CP:
            self.__applyForceOnCp(force, duration)
        
        elif force.applicationPoint() == ApplicationPoint.CUSTOM:
            self.__applyForceOnPoint(force, duration)

        else:
            raise ValueError("Invalid application point")

    