from dataclasses import dataclass

from models.physics.rigid_body import RigidBody
from material_model import MaterialModel

class FinModel:
    def __init__(self, root_chord, tip_chord, span, max_thickness, sweep_angle, material:MaterialModel):
        self.__root_chord = root_chord
        self.__tip_chord = tip_chord
        self.__span = span
        self.__max_thickness = max_thickness
        self.__sweep_angle = sweep_angle
        self.__material = material
        self.__rigid_body = self.__createRigidBody()

    def __createRigidBody():
        pass