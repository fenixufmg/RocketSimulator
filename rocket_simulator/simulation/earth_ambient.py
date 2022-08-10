from core.physics.forces.force import Force
from typing import List
from core.physics.forces.drag_force import DragForce
from core.physics.forces.weight_force import WeightForce
from core.physics.forces.weight_force import CelestialBody
from simulation.abstract_ambient import AbstractAmbient

class EarthAmbient(AbstractAmbient):
    def __init__(self) -> None:
        weight = WeightForce(CelestialBody.EARTH)
        dragForce = DragForce()
        forces = [weight, dragForce]
        super().__init__(forces)