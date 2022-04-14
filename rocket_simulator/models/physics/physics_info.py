from ctypes import pointer

from models.physics.vector_2d import Vector2d
from models.physics.rigid_body_2d import RigidBody2d


class Physics2dInfo:
    def __init__(self, position:RigidBody2d, velocity:Vector2d, mass:float, time:int): # velocidade angular?
        self.__position = position
        self.__velocity = velocity
        self.__mass = mass
        self.__time = time