from core.physics.forces.force import Force
from core.physics.delta_time_simulation import DeltaTimeSimulation
from core.physics.body.application_point import ApplicationPoint
from core.physics.vector import Vector

class TestForce(Force):
    def __init__(self, x, y, z, application_point: ApplicationPoint, cg_offset=None):
        super().__init__(x, y, z, application_point, cg_offset)

    def calculate(self, current_state:DeltaTimeSimulation):
        
        if current_state.time == 5:
            pass
            self.setX(self.x()*-1)
            self.setY(0)

        # print(self.toString())