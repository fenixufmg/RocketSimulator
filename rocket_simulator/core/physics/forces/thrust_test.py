from core.physics.forces.force import Force
from core.physics.delta_time_simulation import DeltaTimeSimulation
from core.physics.body.application_point import ApplicationPoint

class ThrustTest(Force):
    def __init__(self):
        super().__init__(0,0,0, ApplicationPoint.CG, None)
    
    def calculate(self, current_state:DeltaTimeSimulation):
        direction = current_state.looking_direction 
        magnitude = 120
        thrust = direction * magnitude

        self.setX(thrust.x())
        self.setY(thrust.y())
        self.setZ(thrust.z())

