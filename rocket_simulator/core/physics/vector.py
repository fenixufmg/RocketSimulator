# from __future__ import annotations
from decimal import Decimal
import math
from math import cos, sin
from multiprocessing.sharedctypes import Value
from typing import Type
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

    def magnitudeRelativeTo(self, root:'Vector'):
        magnitude = self.magnitude()
        dot_product = Vector.dotProduct(self, root)
        if dot_product == 0:
            return 0
            
        magnitude *=  dot_product / abs(dot_product)
        return magnitude


    def unitVector(self)-> 'Vector':
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
        
    def __add__(self, vector:'Vector') -> 'Vector':
        x = self.x() + vector.x()
        y = self.y() + vector.y()
        z = self.z() + vector.z()
        return Vector(x,y,z)

    def __sub__(self, vector: 'Vector') -> 'Vector':
        x = self.x() - vector.x()
        y = self.y() - vector.y()
        z = self.z() - vector.z()
        return Vector(x,y,z)

    def __mul__(self, scalar:float) -> 'Vector': # Vector SEMPRE deve vir antes do escalar na multiplicação
        if isinstance(scalar, self.__class__): # produto entre dois vetores
            raise ValueError("Impossible matrix multiplication")

        elif isinstance(scalar, float) or isinstance(scalar, int): # produto escalar
            x = self.x() * scalar
            y = self.y() * scalar
            z = self.z() * scalar
            return Vector(x,y,z)

        else:
            raise TypeError("Unsupported operand type(s) for +: '{}' and '{}'").format(self.__class__, type(scalar))

    @staticmethod
    def crossProduct(vector1: 'Vector', vector2: 'Vector') -> 'Vector':
        result = np.cross(vector1.toList(), vector2.toList())
        return Vector(result[0], result[1], result[2])

    @staticmethod
    def dotProduct(vector1: 'Vector', vector2: 'Vector'):
        return np.dot(vector1.toList(), vector2.toList())

    @staticmethod
    def rotateAroundAxis(vector:'Vector', axis:'Vector', theta:float): # theta em radianos
        axis = axis.unitVector()
        ux = axis.x()
        uy = axis.y()
        uz = axis.z()

        cos_theta = cos(theta)
        sin_theta = sin(theta)
        one_minus_cos_theta = 1 - cos_theta

        a11 = cos_theta + ux**2*one_minus_cos_theta
        a12 = ux*uy*one_minus_cos_theta - uz*sin_theta
        a13 = ux*uz*one_minus_cos_theta + uy*sin_theta

        a21 = uy*ux*one_minus_cos_theta + uz*sin_theta
        a22 = cos_theta + uy**2*one_minus_cos_theta
        a23 = uy*uz*one_minus_cos_theta - ux*sin_theta

        a31 = uz*ux*one_minus_cos_theta - uy*sin_theta
        a32 = uz*uy*one_minus_cos_theta + ux*sin_theta
        a33 = cos_theta + uz**2*one_minus_cos_theta

        rotation_matriz = np.matrix([[a11, a12, a13], [a21, a22, a23], [a31, a32, a33]])

        rotated_vector = np.matmul(rotation_matriz, vector.toNumpyVector())
        rotated_vector = Vector(rotated_vector[0,0], rotated_vector[1,0], rotated_vector[2,0])
        return rotated_vector

    @staticmethod
    def projectVector(vector:'Vector', root:'Vector'):
        scalar = Vector.dotProduct(vector, root)/(root.magnitude()**2)
        return root * scalar
        


    