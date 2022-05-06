from core.physics.forces.force import Force
from core.physics.delta_time_simulation import DeltaTimeSimulation
from core.physics.body.application_point import ApplicationPoint
from utils.constants import Constants

class TranslationTestForce(Force):
    def __init__(self, x, y, z, application_point: ApplicationPoint, cg_offset=None):
        super().__init__(x, y, z, application_point, cg_offset)

    def calculate(self, current_state:DeltaTimeSimulation):
        if current_state.time == 10:
            self.setX(0)
            self.setY(0)
            self.setZ(0)
        
        if current_state.time == 29:
            self.setX(0)
            self.setY(0)
            self.setZ(current_state.mass * -Constants.GRAVITY.value)

        # print(self.toString())