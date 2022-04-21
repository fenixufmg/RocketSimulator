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

        self.__velocity = Vector(0,0,0)
        self.__angular_velocity = Vector(0,0,0) # errado, corrigir

        self.__cp = self.__calculateCp()
        self.__cg = self.__calculateCg()

        self.__coordinate_system = BodyCoordinateSystem()

    def __calculateVolume(self):
        pass

    def __calculateMass(self):
        # return self.__material.density() * self.__volume
        return 2

    def __calculateCp(self) -> Vector: # mudar
        return Vector(0,0,0)

    def __calculateCg(self) -> Vector: # mudar
        return Vector(0,0,0)

    def cg(self) -> float:
        return self.__cp

    def cp(self) -> float:
        return self.__cg

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

    def move(self, displacement:Vector):
        self.__cg = Vector.sum(self.__cg, displacement)
        self.__cp = Vector.sum(self.__cp, displacement)
        self.__coordinate_system.move(displacement)

        for index, delimitation_point in enumerate(self.__delimitation_points):
            new_delimitation_point = Vector.sum(delimitation_point, displacement)
            self.__delimitation_points[index] = new_delimitation_point

    def __applyForceOnCg(self, force:Force, duration:int):
        acceleration = Vector.scalarMultiplication(force, 1/self.__mass)

        velocity = Vector.sum(self.__velocity, Vector.scalarMultiplication(acceleration, duration)) # velocidade inicial é a velocidade de um estado antes do atual
        v0t = Vector.scalarMultiplication(self.__velocity, duration)

        at2 = Vector.scalarMultiplication(acceleration, duration**2)
        half_at2 = Vector.scalarMultiplication(at2, 1/2)
        displacement =  Vector.sum(v0t, half_at2)

        self.__velocity = velocity
        self.move(displacement)

    def __applyForceOnCp(self, force:Force, duration:int): # chama o move()
        pass

    def __applyForceOnPoint(self, force:Force ,duration:int): # chama o move()
        pass

    def __rotateAroundCg(self, force:Force, lever:Vector):
        # lever deve apontar para o ponto de aplicação
        torque = Vector.crossProduct(force, lever)
        ortho_basis = np.matrix([force.unitVector().toList(), lever.unitVector().toList(), torque.unitVector().toList()]).transpose()

        b1 = force.unitVector()
        b2 = lever.unitVector()
        b3 = torque.unitVector()

        x_b = Vector.dotProduct(self.__cg, b1)
        y_b = Vector.dotProduct(self.__cg, b2)
        z_b = Vector.dotProduct(self.__cg, b3)

        x_b = Vector(x_b, y_b, z_b)

    
    def applyForce(self, force:Force, duration:int):
        if force.applicationPoint() == ApplicationPoint.CG:
            self.__applyForceOnCg(force, duration)
        
        elif force.applicationPoint() == ApplicationPoint.CP:
            self.__applyForceOnCp(force, duration)
        
        elif force.applicationPoint() == ApplicationPoint.CUSTOM:
            self.__applyForceOnPoint(force, duration)

        else:
            raise ValueError("Invalid application point")

    