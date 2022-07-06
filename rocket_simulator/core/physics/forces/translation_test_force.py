from core.physics.forces.force import Force
from core.physics.delta_time_simulation import DeltaTimeSimulation
from core.physics.body.application_point import ApplicationPoint
from utils.constants import Constants


class TranslationTestForce(Force):
    def __init__(self, x, y, z, cg_offset=None):
        super().__init__(x, y, z, ApplicationPoint.CG, cg_offset)

    def calculate(self, current_state: DeltaTimeSimulation):
        if current_state.time >= 10:
            self.setX(0)
            self.setY(0)
            self.setZ(0)

        if current_state.time >= 35:
            self.setX(0)
            self.setY(0)
            self.setZ(current_state.mass * -Constants.GRAVITY.value)
