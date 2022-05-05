from dataclasses import dataclass

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
