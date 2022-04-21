from multiprocessing.sharedctypes import Value
from core.physics.point import Point
from core.physics.forces.force import Force
from core.physics.vector import Vector
from core.physics.body.application_point import ApplicationPoint
from core.physics.body.body_coordinate_system import BodyCoordinateSystem

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

    # def __applyForceOnCg(self, force:Force, duration:int):
    #     acceleration_magnitude = force.magnitude() / self.__mass
    #     acceleration_direction = force.unitVector()

    #     velocity_magnitude = self.__velocity.magnitude() + acceleration_magnitude * duration # velocidade inicial é a velocidade de um estado antes do atual
    #     print(velocity_magnitude)
    #     displacement_magnitude = (self.__velocity.magnitude() * duration) + (acceleration_magnitude * duration**2)/2 

    #     if self.__velocity.magnitude() == 0: # quando começa a simulação
    #         velocity_direction = force.unitVector()
    #     else:
    #         acceleration = Vector.scalarMultiplication(acceleration_direction, acceleration_magnitude)
    #         velocity_direction = Vector.sum(self.__velocity, acceleration).unitVector()  # já iniciada


    #     displacement_direction = Vector.sum(velocity_direction, acceleration_direction).unitVector()

    #     displacement = Vector.scalarMultiplication(displacement_direction, displacement_magnitude) 
    #     self.__velocity = Vector.scalarMultiplication(velocity_direction, velocity_magnitude) 
     
    #     self.move(displacement)

    def __applyForceOnCg(self, force:Force, duration:int):
        acceleration = Vector.scalarMultiplication(force, 1/self.__mass)

        velocity = Vector.sum(self.__velocity, Vector.scalarMultiplication(acceleration, duration)) # velocidade inicial é a velocidade de um estado antes do atual
        displacement = Vector.scalarMultiplication(self.__velocity, duration)
        displacement = Vector.sum(displacement, Vector.scalarMultiplication(Vector.scalarMultiplication(acceleration, duration**2), 1/2))

        self.__velocity = velocity
        
        self.move(displacement)

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

    