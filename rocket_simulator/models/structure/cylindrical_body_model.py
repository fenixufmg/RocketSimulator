from dataclasses import dataclass
from typing import List
from utils.rocket_parts import RocketParts
from math import pi
from core.physics.vector import Vector
from core.physics.body.rigid_body import RigidBody
from models.other.material_model import MaterialModel
from models.structure.abstract_model import AbstractModel


class CylindricalBodyModel(AbstractModel):
    def __init__(self, height, diameter, thickness, material: MaterialModel, position_order: int):
        self.__verify(diameter, thickness)

        self.height = height
        self.diameter = diameter  # Outer diameter
        self.thickness = thickness
        self.material = material

        super().__init__(RocketParts.CYLINDRICAL_BODY, position_order, 0)

    def __verify(self, diameter, thickness):
        if thickness >= diameter / 2:
            raise ValueError("Value of thickness is bigger than half of outer diameter")

    def calculateVolume(self) -> float:
        inner_diameter = self.diameter - 2 * self.thickness
        volume = pi * self.height * ((self.diameter / 2) ^ 2 - (inner_diameter / 2) ^ 2)
        return volume

    def calculateMass(self) -> float:
        mass = self.material.density * self.calculateVolume
        return mass

    def calculateMomentOfInertia(self, distance_to_cg: float) -> float: # https://en.wikipedia.org/wiki/List_of_moments_of_inertia
        mass = self.calculateMass
        Ixx = 1/12*mass*(3*( (self.diameter^2)/4 +((self.diameter-2*self.thickness)^2)/4 )+self.height^2)
        return Ixx

    def calculateCg(self) -> Vector:  # Feito amigo
        # Primeiro pega o vetor de altura da peça, a sua direção varia com a orientação do foguete, mas o módulo é
        # constante. getTipToBaseDistance() retorna o vetor que sai da ponta superior e vai até à ponta inferior
        height = self.getTipToBaseDistance()
        cg_local = height * 0.5  # produto por escalar
        return self.toGroundCoordinates(cg_local)

    def calculateCp(self) -> Vector: # CONFERIR DEPOIS
        height = self.getTipToBaseDistance()
        cg_local = height * 0.5  
        cp_local = cg_local # Assuming same position as cp
        return self.toGroundCoordinates(cp_local)

    def createDelimitationPoints(self) -> List[Vector]:
        upper_delimitation = Vector(0, 0, self.height)
        lower_delimitation = Vector(0, 0, 0)
        return [upper_delimitation, lower_delimitation]