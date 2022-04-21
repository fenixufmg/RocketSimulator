from __future__ import annotations
import math
import numpy as np

class Vector:
    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z
        self.__magnitude = self.__calculateMagnitude()

    def __calculateMagnitude(self) -> float: 
        return math.sqrt(self.__x**2 + self.__y**2 + self.__z**2)

    def x(self):
        return self.__x

    def setX(self, x):
        self.__x = x
    
    def y(self):
        return self.__y

    def setY(self, y):
        self.__y = y

    def z(self):
        return self.__z

    def setZ(self, z):
        self.__z = z

    def magnitude(self):
        return self.__calculateMagnitude()

    def unitVector(self)-> Vector:
        if self.__magnitude == 0:
            return Vector(0,0,0)

        x = self.__x / self.__magnitude
        y = self.__y / self.__magnitude
        z = self.__z / self.__magnitude
        return Vector(x,y,z)

    def toList(self) -> str:
        return [self.__x, self.__y, self.__z]

    def toNumpyVector(self) -> np.matrix:
        return np.matrix([self.toList()]).transpose()
        
    @staticmethod
    def sum(vector1: Vector, vector2: Vector) -> Vector:
        x = vector1.x() + vector2.x()
        y = vector1.y() + vector2.y()
        z = vector1.z() + vector2.z()
        return Vector(x,y,z)

    @staticmethod
    def subtraction(vector1: Vector, vector2: Vector) -> Vector:
        x = vector1.x() - vector2.x()
        y = vector1.y() - vector2.y()
        z = vector1.z() - vector2.z()
        return Vector(x,y,z)

    @staticmethod
    def scalarMultiplication(vector: Vector, scalar) -> Vector:
        x = vector.x() * scalar
        y = vector.y() * scalar
        z = vector.z() * scalar
        return Vector(x,y,z)

    @staticmethod
    def rotateAroundXAxis(vector:Vector, radians): # rotaciona no plano yz
        x = vector.x()
        y = vector.magnitude() * math.cos(radians)
        z = vector.magnitude() * math.sin(radians)
        
        return Vector(x,y,z)

    @staticmethod
    def rotateAroundYAxis(vector:Vector, radians): # rotaciona no plano xz
        radians *= -1 # eixo y é positivo para dentro do monitor
        x = vector.magnitude() * math.cos(radians)
        y = vector.y()
        z = vector.magnitude() * math.sin(radians)

        return Vector(x,y,z)
    
    @staticmethod
    def rotateAroundZAxis(vector: Vector, radians) -> Vector: # rotaciona no plano xy
        x = vector.magnitude() * math.cos(radians)
        y = vector.magnitude() * math.sin(radians)
        z = vector.z()

        return Vector(x,y,z)

    @staticmethod
    def crossProduct(vector1: Vector, vector2: Vector) -> Vector:
        return np.cross(vector1.toList(), vector2.toList())

    @staticmethod
    def dotProduct(vector1: Vector, vector2: Vector):
        return np.dot(vector1.toList(), vector2.toList())

    @staticmethod
    def rotate(vector:Vector): # completar argumentos
        pass 
    