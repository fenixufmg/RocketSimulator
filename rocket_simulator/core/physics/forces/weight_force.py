from core.physics.forces.force import Force
from core.physics.delta_time_simulation import DeltaTimeSimulation
from core.physics.application_point import ApplicationPoint

class WeightForce(Force):
    def __init__(self, x, y, z, application_point: ApplicationPoint, cg_offset=None):
        super().__init__(x, y, z, application_point, cg_offset)

    def calculate(self, current_state: DeltaTimeSimulation):
        weight_magnitude = current_state.mass * 9.8
        weight_direction = 0