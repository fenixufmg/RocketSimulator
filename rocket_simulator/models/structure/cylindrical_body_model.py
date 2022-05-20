from dataclasses import dataclass

from math import pi
from core.physics.body.rigid_body import RigidBody
from other.material_model import MaterialModel
from models.structure.abstract_model import AbstractModel

class CylindricalBodyModel(AbstractModel):
    def __init__(self, height, diameter, thickness, material:MaterialModel):
        self.__height = height
        self.__diameter = diameter
        self.__thickness = thickness
        self.__material = material
        super().__init__()

    def calculateVolume(self) -> float:
        inner_diameter = self.__diameter -2*self.__thickness
        volume = pi*self.__height*((self.__diameter/2)^2-(inner_diameter/2)^2)
        return volume
    
    def calculateMass(self)-> float:
        mass = self.__material.density*self.calculateVolume
        return mass

