from core.physics.forces.force import Force
from core.physics.delta_time_simulation import DeltaTimeSimulation
from core.physics.body.application_point import ApplicationPoint

class RotationTestForce(Force):
    def __init__(self, x, y, z, application_point: ApplicationPoint, cg_offset=None):
        super().__init__(x, y, z, application_point, cg_offset)

    def calculate(self, current_state:DeltaTimeSimulation):
        pass
        if current_state.time < 5:
            self.setX(0)
            self.setY(0)
            self.setZ(0)
            
        if current_state.time >= 5:
            self.setX(0)
            self.setY(0.2)
            self.setZ(0)

        if current_state.time >= 6:
            self.setX(0)
            self.setY(0)
            self.setZ(0)