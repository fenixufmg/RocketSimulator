from multiprocessing.sharedctypes import Value
from models.physics.point import Point
from models.physics.force import Force
from models.physics.vector import Vector
from models.physics.application_point import ApplicationPoint

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

    def __calculateVolume(self):
        pass

    def __calculateMass(self):
        return self.__material.density() * self.__volume

    def __calculateCp(self):
        pass

    def __calculateCg(self):
        pass

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

    def move(self, destination:Point):
        pass

    def __applyForceOnCg(self, force:Force, duration:int): # chama o move()
        pass

    def __applyForceOnCp(self, force:Force, duration:int): # chama o move()
        pass

    def __applyForceOnPoint(self, force:Force ,duration:int): # chama o move()
        pass
    
    def applyForce(self, force:Force, duration:int):
        if force.applicationPoint() == ApplicationPoint.CG:
            self.__applyForceOnCg(force, duration)
        
        elif force.applicationPoint() == ApplicationPoint.CP:
            self.__applyForceOnCp(force, duration)
        
        elif force.applicationPoint() == ApplicationPoint.CUSTOM:
            self.__applyForceOnPoint(force, duration)

        else:
            raise ValueError("Invalid application point")

    