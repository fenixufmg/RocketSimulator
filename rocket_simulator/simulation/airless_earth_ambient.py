from core.physics.forces.force import Force
from typing import List
from core.physics.forces.drag_force import DragForce
from core.physics.forces.weight_force import WeightForce
from models.structure.rocket_model import RocketModel
from simulation.abstract_ambient import AbstractAmbient

class AirlessEarthAmbient(AbstractAmbient):
    def __init__(self, rocket:RocketModel) -> None:
        weight = WeightForce()
        forces = [weight]
        super().__init__(rocket, forces)