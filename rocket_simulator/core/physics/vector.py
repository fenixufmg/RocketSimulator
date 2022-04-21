from __future__ import annotations
import math

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

    def toString(self) -> str:
        return [self.__x, self.__y, self.__z]
        
    @staticmethod
    def sum(vector1, vector2) -> Vector:
        x = vector1.x() + vector2.x()
        y = vector1.y() + vector2.y()
        z = vector1.z() + vector2.z()
        return Vector(x,y,z)

    @staticmethod
    def subtraction(vector1, vector2) -> Vector:
        x = vector1.x() - vector2.x()
        y = vector1.y() - vector2.y()
        z = vector1.z() - vector2.z()
        return Vector(x,y,z)

    @staticmethod
    def scalarMultiplication(vector, scalar) -> Vector:
        x = vector.x() * scalar
        y = vector.y() * scalar
        z = vector.z() * scalar
        return Vector(x,y,z)

    @staticmethod
    def scaleToMagnitude(vector, magnitude) -> Vector:
        pass