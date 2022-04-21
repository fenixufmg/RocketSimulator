from dataclasses import dataclass

from models.physics.rigid_body import RigidBody
from material_model import MaterialModel

class CylindricalBodyModel:
    def __init__(self, height, diameter, thickness, material:MaterialModel):
        self.__height = height
        self.__diameter = diameter
        self.__thickness = thickness
        self.__material = material
        self.__rigid_body = self.__createRigidBody()

    def __createRigidBody():
        pass