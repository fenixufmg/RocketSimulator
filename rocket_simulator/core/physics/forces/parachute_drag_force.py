from core.physics.forces.force import Force
from core.physics.delta_time_simulation import DeltaTimeSimulation
from core.physics.body.application_point import ApplicationPoint
from math import pi
from core.aerodynamic.drag import drag


class ParachuteDrag(Force):
    def __init__(self):
        super().__init__(0,0,0, ApplicationPoint.CP, None)
    
    def calculate(self, current_state:DeltaTimeSimulation):
        parachute = current_state.parachute
        if parachute.inflated is False: # ainda não foi inflado
            self.setX(0)
            self.setY(0)
            self.setZ(0) 
            return

        transversal_section_area = parachute.transversalSectionArea()
        drag_coefficient = parachute.drag_coefficient
        magnitude = drag(transversal_section_area, drag_coefficient, current_state.velocity.magnitude())

        direction = current_state.velocity.unitVector() * -1 
        thrust = direction * magnitude

        self.setX(thrust.x())
        self.setY(thrust.y())
        self.setZ(thrust.z())
