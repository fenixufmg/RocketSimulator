from dataclasses import dataclass

from core.physics.body.rigid_body import RigidBody
from other.material_model import MaterialModel
from models.structure.abstract_model import AbstractModel

class FinModel(AbstractModel):
    def __init__(self, root_chord, tip_chord, span, max_thickness, sweep_angle, material:MaterialModel):
        self.__root_chord = root_chord
        self.__tip_chord = tip_chord
        self.__span = span
        self.__max_thickness = max_thickness
        self.__sweep_angle = sweep_angle
        self.__material = material
        super().__init__()
