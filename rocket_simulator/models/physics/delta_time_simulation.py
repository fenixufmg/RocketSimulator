from ctypes import pointer

from models.physics.vector import Vector
from models.physics.rigid_body import RigidBody


class DeltaTimeSimulation:
    def __init__(self, rigid_body:RigidBody):
        self.__position = rigid_body.cg()
        self.__velocity = rigid_body.velocity()
        self.__angular_velocity = rigid_body.angularVelocity()
        self.__mass = rigid_body.mass()