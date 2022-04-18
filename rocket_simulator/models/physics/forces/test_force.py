from models.physics.force import Force
from models.physics.delta_time_simulation import DeltaTimeSimulation
from models.physics.application_point import ApplicationPoint

class TestForce(Force):
    def __init__(self, x, y, z, application_point: ApplicationPoint, cg_offset=None):
        super().__init__(x, y, z, application_point, cg_offset)

    def calculate(self, current_state:DeltaTimeSimulation):
        pass