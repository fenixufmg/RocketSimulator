from typing import List
from core.physics.forces.drag_force import DragForce
from core.physics.forces.normal_force import NormalForce
from core.physics.forces.weight_force import WeightForce
from core.physics.forces.weight_force import CelestialBody
from core.physics.forces.wind_force import WindForce
from utils.wind_direction import WindDirection
from simulation.abstract_ambient import AbstractAmbient


class EarthAmbient(AbstractAmbient):
    def __init__(self, wind_velocity:float, wind_direction:WindDirection) -> None:
        """ Representa o ambiente da terra.

        Args:
            wind_velocity (float): Velocidade do vento.
            wind_direction (WindDirection): Direção cardeal do vento.
        """
        self.wind_direction:float = wind_direction.value 
        self.wind_velocity = wind_velocity

        weight = WeightForce(CelestialBody.EARTH)
        drag_force = DragForce()
        wind_force = WindForce(wind_velocity, wind_direction)
        normal_force = NormalForce()  # FORÇA NORMAL NÃO ESTÁ 100% TESTADA
        forces = [weight, wind_force, drag_force]  # FORÇA NORMAL NÃO ESTÁ 100% TESTADA
        super().__init__(forces)