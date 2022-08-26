from typing import List
from core.physics.forces.drag_force import DragForce
from core.physics.forces.weight_force import WeightForce
from core.physics.forces.weight_force import CelestialBody
from core.physics.forces.wind_force import WindForce
from utils.wind_direction import WindDirection
from simulation.abstract_ambient import AbstractAmbient


class EarthAmbient(AbstractAmbient):
    def __init__(self, wind_velocity:float, wind_direction:WindDirection) -> None:
        self.wind_direction:float = wind_direction.value 
        self.wind_velocity = wind_velocity

        weight = WeightForce(CelestialBody.EARTH)
        drag_force = DragForce()
        wind_force = WindForce(wind_velocity, wind_direction)
        forces = [weight, wind_force, drag_force]
        super().__init__(forces)