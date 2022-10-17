from core.physics.forces.weight_force import WeightForce
from core.physics.forces.weight_force import CelestialBody
from simulation.abstract_ambient import AbstractAmbient

class AirlessEarthAmbient(AbstractAmbient):
    def __init__(self) -> None:
        """ Representa o ambiente da terra sem atmosfera.
        """
        weight = WeightForce(CelestialBody.EARTH)
        forces = [weight]
        super().__init__(forces)