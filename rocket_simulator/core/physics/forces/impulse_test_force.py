from core.physics.forces.force import Force
from core.physics.delta_time_simulation import DeltaTimeSimulation
from core.physics.body.application_point import ApplicationPoint
from utils.constants import Constants


class ImpulseTestForce(Force):
    def __init__(self, thrust, cg_offset=None):
        self.thrust = thrust
        super().__init__(0,0,0, ApplicationPoint.CG, cg_offset)

    def calculate(self, current_state: DeltaTimeSimulation):
        if current_state.time <= 2:
            thrust_force = current_state.looking_direction.unitVector() * self.thrust
            self.setX(thrust_force.x())
            self.setY(thrust_force.y())
            self.setZ(thrust_force.z())
        else:
            self.setX(0)
            self.setY(0)
            self.setZ(0)

