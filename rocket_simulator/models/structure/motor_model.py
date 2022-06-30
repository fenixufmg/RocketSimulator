from utils.rocket_parts import RocketParts
from models.structure.abstract_model import AbstractModel
from core.physics.vector import Vector
from utils.constants import Constants

class MotorModel(AbstractModel):
    def __init__(self, position_order:int):
        super().__init__(RocketParts.MOTOR, position_order)

    def activate(self):
        pass

