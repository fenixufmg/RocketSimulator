from core.physics.forces.force import Force
from core.physics.delta_time_simulation import DeltaTimeSimulation
from core.physics.body.application_point import ApplicationPoint
from math import pi
from core.recovery.drag_force import drag_force


class ThrustTest(Force):
    def __init__(self):
        super().__init__(0,0,0, ApplicationPoint.CG, None)
    
    def calculate(self, current_state:DeltaTimeSimulation):
        magnitude = drag_force
        direction = current_state.looking_direction 
        thrust = direction * magnitude

        self.setX(thrust.x())
        self.setY(thrust.y())
        self.setZ(thrust.z())
