from core.physics.forces.force import Force
from core.physics.delta_time_simulation import DeltaTimeSimulation
from core.physics.body.application_point import ApplicationPoint
from math import pi
from core.recovery.drag_force import drag_force


class ThrustTest(Force):
    def __init__(self):
        super().__init__(0,0,0, ApplicationPoint.CP, None)
    
    def calculate(self, current_state:DeltaTimeSimulation):
        # magnitude = drag_force # antigo
        parachute = current_state.parachute
        transversal_section_area = parachute.transversalSectionArea()
        drag_coefficient = parachute.drag_coefficient
        magnitude = drag_force(transversal_section_area, drag_coefficient, current_state.velocity.magnitude())

        direction = current_state.looking_direction 
        thrust = direction * magnitude

        self.setX(thrust.x())
        self.setY(thrust.y())
        self.setZ(thrust.z())
