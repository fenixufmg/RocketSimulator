# from __future__ import annotations
from decimal import Decimal
import math
from math import cos, sin
from multiprocessing.sharedctypes import Value
from typing import Type
import numpy as np
from numpy import ndarray

class Vector:
    def __init__(self, x, y, z):
        """Representa um vetor.

        Args:
            x (float): Valor no eixo x.
            y (float): Valor no eixo y.
            z (float): Valor no eixo z.
        """
        self.__x = x
        self.__y = y
        self.__z = z

    def __calculateMagnitude(self) -> float: 
        """Calcula a magnitude do vetor.

        Returns:
            float: Magnitude do vetor
        """
        return math.sqrt(self.__x**2 + self.__y**2 + self.__z**2)

    def x(self):
        """Retorna o valor no eixo x.

        Returns:
            float: valor no eixo x.
        """
        return self.__x

    def setX(self, x):
        """Altera o valor do eixo x.

        Args:
            x (float): Novo valor do eixo x.
        """
        self.__x = x
    
    def y(self):
        """Retorna o valor do eixo y.

        Returns:
            float: Valor do eixo y.
        """
        return self.__y

    def setY(self, y):
        """Altera o valor do eixo y.

        Args:
            y (float): Novo valor do eixo y.
        """
        self.__y = y

    def z(self):
        """Retorna o valor do eixo z.

        Returns:
            float: Valor do eixo z.
        """
        return self.__z

    def setZ(self, z):
        """Altera o valor do eixo z.

        Args:
            z (float): Novo valor do eixo z.
        """
        self.__z = z

    def magnitude(self):
        """Retorna a magnitude do vetor.

        Returns:
            float: Magnitude do vetor.
        """
        return self.__calculateMagnitude()

    def magnitudeRelativeTo(self, root:'Vector'):
        """Retorna a magnitude do vetor, porém o sinal é negativo se o vetor instanciado tiver sentido
        contrário ao vetor root.

        Args:
            root (Vector): Vetor com o qual o vetor instanciado terá seu sentido comparado.

        Returns:
            float: Magnitude relativa.
        """
        magnitude = self.magnitude()
        dot_product = Vector.dotProduct(self, root)
        if dot_product == 0:
            return 0
            
        magnitude *=  dot_product / abs(dot_product)
        return magnitude


    def unitVector(self)-> 'Vector':
        """Retorna o vetor unitário.

        Returns:
            Vector: Vetor unitário
        """
        if self.__calculateMagnitude() == 0:
            return Vector(0,0,0)

        x = self.__x / self.__calculateMagnitude()
        y = self.__y / self.__calculateMagnitude()
        z = self.__z / self.__calculateMagnitude()
        return Vector(x,y,z)

    def toList(self) -> list:
        """Transforma o vetor em uma lista.

        Returns:
            list: Lista com as os valores dos eixos.
        """
        return [self.__x, self.__y, self.__z]

    def toNumpyVector(self) -> ndarray:
        """Transforma o vetor em uma matrix do numpy.

        Returns:
            np.matrix: Matriz do numpy
        """
        return np.matrix([self.toList()]).transpose()
        
    def __add__(self, vector:'Vector') -> 'Vector':
        """Método sobrescrito que permite a utilização do operador + para a adição de vetores.

        Args:
            vector (Vector): Vetor a ser adicionado.

        Returns:
            Vector: Adição do vetor instanciado pelo vetor parâmetro.
        """
        x = self.x() + vector.x()
        y = self.y() + vector.y()
        z = self.z() + vector.z()
        return Vector(x,y,z)

    def __sub__(self, vector: 'Vector') -> 'Vector':
        """Método sobrescrito que permite a utilização do operador - para a substração de vetores.

        Args:
            vector (Vector): Vetor a ser subtraido.

        Returns:
            Vector: Subtração do vetor instanciado pelo vetor parâmetro.
        """
        x = self.x() - vector.x()
        y = self.y() - vector.y()
        z = self.z() - vector.z()
        return Vector(x,y,z)

    def __mul__(self, scalar:float) -> 'Vector':
        """Método sobrescrito que permite a utilização do operador * para o produto por escalar. O vetor SEMPRE
        deve vir antes do escalar na multiplicação.

        Args:
            scalar (float): Escalar pelo qual o vetor será multiplicado.

        Raises:
            ValueError: Jogado se o argumento passado for um vetor.
            TypeError: Argumento passado é de uma classe imcompatível.

        Returns:
            Vector: Vetor resultante do produto por escalar.
        """
        if isinstance(scalar, self.__class__): # produto entre dois vetores
            raise ValueError("Impossible matrix multiplication")

        elif isinstance(scalar, float) or isinstance(scalar, int): # produto escalar
            x = self.x() * scalar
            y = self.y() * scalar
            z = self.z() * scalar
            return Vector(x,y,z)

        else:
            raise TypeError("Unsupported operand type(s) for +: '{}' and '{}'".format(self.__class__, type(scalar)))

    def __str__(self):
        result = self.toList()
        return f"({result[0]}, {result[1]}, {result[2]})"

    @staticmethod
    def crossProduct(vector1: 'Vector', vector2: 'Vector') -> 'Vector':
        """Método estático que retorna o produto vetorial entre dois vetores.

        Args:
            vector1 (Vector): Vetor 1.
            vector2 (Vector): Vetor 2.

        Returns:
            Vector: Produto vetorial entre vetor 1 e o vetor 2.
        """
        result = np.cross(vector1.toList(), vector2.toList())
        return Vector(result[0], result[1], result[2])

    @staticmethod
    def dotProduct(vector1: 'Vector', vector2: 'Vector'):
        """Método estático que retorna o produto escalar entre dois vetores.

        Args:
            vector1 (Vector): Vetor 1.
            vector2 (Vector): Vetor 2.

        Returns:
            float: Produto escalar entre os dois vetores.
        """
        return np.dot(vector1.toList(), vector2.toList())

    @staticmethod
    def rotateAroundAxis(vector:'Vector', axis:'Vector', theta:float):
        """Método estático que rotaciona um vetor ao redor de um eixo em theta radianos.

        Args:
            vector (Vector): Vetor a ser rotacionado.
            axis (Vector): Vetor unitário que representa o eixo de rotação.
            theta (float): Ângulo de rotação (em radianos).

        Returns:
            Vector: Vetor rotacionado.
        """
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
        """Método estático que projeta o vetor do argumento no vetor root.

        Args:
            vector (Vector): Vetor que vai ser projetado.
            root (Vector): Base para a projeção ortogonal.

        Returns:
            Vector: Vetor projetado.
        """
        scalar = Vector.dotProduct(vector, root)/(root.magnitude()**2)
        return root * scalar
        


    