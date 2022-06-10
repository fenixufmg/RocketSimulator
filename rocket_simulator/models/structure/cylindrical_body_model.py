from dataclasses import dataclass
from utils.rocket_parts import RocketParts
from math import pi
from core.physics.vector import Vector
from core.physics.body.rigid_body import RigidBody
from other.material_model import MaterialModel
from models.structure.abstract_model import AbstractModel


class CylindricalBodyModel(AbstractModel):
    def __init__(self, height, diameter, thickness, material: MaterialModel, position_order: int):
        self.__verify(diameter, thickness)

        self.__height = height
        self.__diameter = diameter  # Outer diameter
        self.__thickness = thickness
        self.__material = material

        super().__init__(RocketParts.CYLINDRICAL_BODY, position_order)

    def __verify(self, diameter, thickness):
        if thickness >= diameter / 2:
            raise ValueError("Value of thickness is bigger than half of outer diameter")

    def calculateVolume(self) -> float:
        inner_diameter = self.__diameter - 2 * self.__thickness
        volume = pi * self.__height * ((self.__diameter / 2) ^ 2 - (inner_diameter / 2) ^ 2)
        return volume

    def calculateMass(self) -> float:
        mass = self.__material.density * self.calculateVolume
        return mass

    def calculateMomentOfInertia(self, distance_to_cg: float) -> float:
        raise NotImplementedError("Function not implemented")  # IMPLEMENTAR ESTA FUNÇÃO FUTURAMENTE

    def calculateCg(self) -> Vector:  # Feito amigo
        # Primeiro pega o vetor de altura da peça, a sua direção varia com a orientação do foguete, mas o módulo é
        # constante. getTipToBaseDistance() retorna o vetor que sai da ponta superior e vai até à ponta inferior
        height = self.getTipToBaseDistance()
        cg_local = height * 0.5  # produto por escalar
        return self.toGroundCoordinates(cg_local)
