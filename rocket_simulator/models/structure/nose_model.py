from dataclasses import dataclass
from email.mime import base
from enum import Enum

from core.physics.body.rigid_body import RigidBody
from other.material_model import MaterialModel
from models.structure.abstract_model import AbstractModel

class NoseType(Enum):
    none = 1
    parabolic = 2
    cubic = 3

class NoseModel(AbstractModel):
    def __init__(self, height, base_diameter, thickness, nose_type:NoseType, material:MaterialModel):
        self.__height = height
        self.__base_diameter = base_diameter
        self.__thickness = thickness
        self.__nose_type = nose_type
        self.__material = material
        super().__init__()