from utils.rocket_parts import RocketParts
from math import pi
from core.physics.vector import Vector
from models.other.material_model import MaterialModel
from core.physics.body.rigid_body import RigidBody
from models.structure.abstract_model import AbstractModel
from dataclasses import dataclass
from typing import List


class TransitionModel(AbstractModel):
    def __init__(self, position, height, bottom_diameter, top_diameter, thickness, material: MaterialModel, position_order: int):
        self.__verify(bottom_diameter, top_diameter, thickness)

        self.__position = position
        self.__height = height
        self.__bottom_diameter = bottom_diameter
        self.__top_diameter = top_diameter
        self.__thickness = thickness
        self.__material = material
        super().__init__(RocketParts.TRANSITION, position_order)

    def __verify(self):
        if self.__bottom_diameter < self.__top_diameter:  # bottom part is thinner
            if self.__thickness >= self.__bottom_diameter / 2:
                raise ValueError("Value of thickness is bigger than half of bottom outer diameter")
        else:
            if self.__thickness >= self.__top_diameter / 2:
                raise ValueError("Value of thickness is bigger than half of top outer diameter")

    def calculateVolume(self) -> float:
        top_inner_diameter = self.__top_diameter - 2 * self.__thickness
        bottom_inner_diameter = self.__bottom_diameter - 2 * self.__thickness

        outer_trunk_volume = (pi / 3) * self.__height * (
                    self.__bottom_diameter ^ 2 + self.__bottom_diameter * self.__top_diameter + self.__top_diameter ^ 2)
        inner_trunk_volume = (pi / 3) * self.__height * (
                    bottom_inner_diameter ^ 2 + bottom_inner_diameter * top_inner_diameter + top_inner_diameter ^ 2)

        total_volume = outer_trunk_volume - inner_trunk_volume
        return total_volume

    def calculateMass(self) -> float:
        mass = self.__material.density * self.calculateVolume
        return mass

    def calculateMomentOfInertia(self, distance_to_cg: float) -> float: # https://en.wikipedia.org/wiki/List_of_moments_of_inertia
        raise NotImplementedError("Function not implemented")

    def calculateCg(self) -> Vector:  # aproximando por um tronco cheio https://www.passeidireto.com/pergunta/17392987/como-achar-um-centro-de-gravidade-em-um-tronco-de-cone 
        height = self.getTipToBaseDistance()

        if self.__bottom_diameter < self.__top_diameter:  # bottom part is thinner
            z = Vector(0,0, self.__height/4*((self.__top_diameter^2 +2*self.__top_diameter*self.__bottom_diameter + 3*self.__bottom_diameter^2)/(
                self.__top_diameter^2 + self.__top_diameter*self.__bottom_diameter + self.__bottom_diameter^2)) )
            cg_local = height - z 
            
        else:
            z = Vector(0,0, self.__height/4*((self.__bottom_diameter^2 +2*self.__bottom_diameter*self.__top_diameter + 3*self.__top_diameter^2)/(
                self.__bottom_diameter^2 + self.__bottom_diameter*self.__top_diameter + self.__top_diameter^2)) )
            cg_local = height - z 
            
        return self.toGroundCoordinates(cg_local)

    def calculateCp(self) -> Vector: 
        raise NotImplementedError("Function not implemented")

    def createDelimitationPoints(self) -> List[Vector]:
        upper_delimitation = Vector(0, 0, self.height)
        lower_delimitation = Vector(0, 0, 0)
        return [upper_delimitation, lower_delimitation]