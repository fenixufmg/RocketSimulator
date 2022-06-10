from utils.rocket_parts import RocketParts
from core.physics.body.rigid_body import RigidBody
from other.material_model import MaterialModel
from models.structure.abstract_model import AbstractModel


class FinModel(AbstractModel):
    def __init__(self, root_chord, tip_chord, span, max_thickness, sweep_angle, material: MaterialModel, position_order: int, distance_to_base):
        self.__root_chord = root_chord
        self.__tip_chord = tip_chord
        self.__span = span
        self.__max_thickness = max_thickness
        self.__sweep_angle = sweep_angle
        self.__distance_to_base = distance_to_base
        self.__material = material
        super().__init__(RocketParts.FIN, position_order)

    def getDistanceToBase(self):
        return self.__distance_to_base

    def calculateVolume(self) -> float:
        area = (self.__span * (self.__tip_chord + self.__root_chord)) / 2
        volume = area * self.__max_thickness
        return volume

    def calculateMass(self) -> float:
        mass = self.__material.density * self.calculateVolume
        return mass
