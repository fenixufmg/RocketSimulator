from core.physics.forces.force import Force
from core.physics.delta_time_simulation import DeltaTimeSimulation
from core.physics.body.application_point import ApplicationPoint

class WeightForce(Force):
    def __init__(self):
        super().__init__(0, 0, -1, ApplicationPoint.CG)

    def calculate(self, current_state: DeltaTimeSimulation):
        weight_magnitude = current_state.mass * -9.8
        self.setZ(weight_magnitude)
        