from ctypes import pointer

from models.physics.vector import Vector
from models.physics.rigid_body import RigidBody


class Physics2dInfo:
    def __init__(self, position:RigidBody, velocity:Vector, mass:float, time:int): # velocidade angular?
        self.__position = position
        self.__velocity = velocity
        self.__mass = mass
        self.__time = time