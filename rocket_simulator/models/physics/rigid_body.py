from models.physics.point import Point
from rocket_simulator.models.physics.vector import Vector


class RigidBody:
    def __init__(self, delimitation_points):
        self.__delimitation_points = delimitation_points
        self.__velocity = Vector(0,0,0)

    def cg(self) -> float:
        pass

    def cp(self) -> float:
        pass

    def volume(self) ->float:
        pass

    def move(self, destination:Point):
        pass

    def applyForceOnCg(self, force:Vector):
        pass

    def applyForceOnCp(self, force:Vector):
        pass
    
    def __rotateAroundCg(self, force:Vector):
        pass

    