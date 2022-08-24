from core.physics.forces.force import Force
from core.physics.delta_time_simulation import DeltaTimeSimulation
from core.physics.body.application_point import ApplicationPoint
from math import pi
from utils.constants import Constants


class ParachuteDrag(Force):
    def __init__(self):
        super().__init__(0,0,0, ApplicationPoint.CP, None)

    def __calculateDrag(self, transversal_section_area:float, drag_coefficient:float, velocity:float):
        air_density = Constants.AIR_DENSITY.value
        return ((1/2)*air_density*velocity**2*transversal_section_area*drag_coefficient)
    
    def calculate(self, current_state:DeltaTimeSimulation):
        parachute = current_state.parachute
        if parachute is None or parachute.inflated is False: # não tem paraquedas ou ainda não foi inflado
            self.setX(0)
            self.setY(0)
            self.setZ(0) 
            return

        transversal_section_area = parachute.transversal_area
        drag_coefficient = parachute.drag_coefficient
        magnitude = self.__calculateDrag(transversal_section_area, drag_coefficient, current_state.velocity.magnitude())

        direction = current_state.velocity.unitVector() * -1 
        thrust = direction * magnitude

        self.setX(thrust.x())
        self.setY(thrust.y())
        self.setZ(thrust.z())
