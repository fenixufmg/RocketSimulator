from dataclasses import dataclass
from email.mime import base
from enum import Enum

from models.physics.rigid_body import RigidBody
from material_model import MaterialModel

class NoseType(Enum):
    none = 1
    parabolic = 2
    cubic = 3

class NoseModel:
    def __init__(self, height, base_diameter, thickness, nose_type:NoseType, material:MaterialModel):
        self.__height = height
        self.__base_diameter = base_diameter
        self.__thickness = thickness
        self.__nose_type = nose_type
        self.__material = material
        self.__rigid_body = self.__createRigidBody()

    def __createRigidBody():
        pass