from utils.rocket_parts import RocketParts
from math import pi
from other.material_model import MaterialModel
from core.physics.body.rigid_body import RigidBody
from models.structure.abstract_model import AbstractModel


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

    def __verify(self, bottom_diameter, top_diameter, thickness):
        if bottom_diameter < top_diameter:  # bottom part is thinner
            if thickness >= bottom_diameter / 2:
                raise ValueError("Value of thickness is bigger than half of bottom outer diameter")
        else:
            if thickness >= top_diameter / 2:
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
