from core.physics.forces.force import Force
from core.physics.delta_time_simulation import DeltaTimeSimulation
from core.physics.body.application_point import ApplicationPoint
from utils.constants import Constants
import enum

class CelestialBody(enum.Enum):
    EARTH = 1

class WeightForce(Force):
    def __init__(self, celestial_body:CelestialBody):
        super().__init__(0, 0, -1, ApplicationPoint.CG)
        self.__celestial_body = celestial_body

    def __getGravityValue(self):
        if self.__celestial_body == CelestialBody.EARTH:
            return Constants.GRAVITY.value

    def calculate(self, current_state: DeltaTimeSimulation):
        weight_magnitude = current_state.mass * self.__getGravityValue()
        self.setZ(weight_magnitude)
        self.setX(0)
        self.setY(0)
