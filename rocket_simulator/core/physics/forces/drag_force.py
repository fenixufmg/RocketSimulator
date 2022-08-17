from asyncio import constants
import imp
from core.physics.forces.force import Force
from core.physics.delta_time_simulation import DeltaTimeSimulation
from core.physics.body.application_point import ApplicationPoint
from core.physics.vector import Vector
from utils.constants import Constants
from models.structure.nose_model import NoseModel
from core.aerodynamic.reynolds_number import reynolds_number
from core.aerodynamic.mach_number import mach_number
from core.aerodynamic.mean_aerodynamic_chord import mean_aerodynamic_chord_length
from core.aerodynamic.rocket_fineness_ratio import rocket_fineness_ratio
from core.aerodynamic.critical_reynolds_number import critical_reynolds_number
from core.aerodynamic.skin_friction_drag import skin_friction_drag
from core.aerodynamic.total_skin_friction_drag_coefficient import total_skin_friction_drag_coefficient 
from math import pi

class DragForce(Force):
    def __init__(self):
        super().__init__(0, 0, 0, ApplicationPoint.CP, None)
        self.__drag_coefficient = None
    
    def __calculateDrag(self, transversal_section_area:float, drag_coefficient:float, velocity:float):
        air_density = Constants.AIR_DENSITY.value
        return ((1/2)*air_density*velocity**2*transversal_section_area*drag_coefficient)

    def __calculateSkinDragCoefficient(self,  current_state: DeltaTimeSimulation) -> float: # coef. arrasto de pele
        meanChord = mean_aerodynamic_chord_length('trapezoidal', current_state.fin.root_chord, current_state.fin.tip_chord)
        rocketLength = current_state.rocket.rocket_height.magnitudeRelativeTo(current_state.rocket.rocket_height)
        rocketSurfaceArea = 0.5 #Fazer
        reynoldsNumber = reynolds_number(rocketLength, Constants.KINEMATIC_VISCOSITY.value)
        mach = mach_number(velocity, 340)
        rocketFinenessRatio = rocket_fineness_ratio(rocketLength ,current_state.nose.base_diameter)
        criticalReynoldsNumber = critical_reynolds_number(0.0000005, rocketLength)
        skingFrictionDrag = skin_friction_drag(reynoldsNumber, criticalReynoldsNumber, 0.0000005, rocketLength, mach)
        skinDragCoefficient = total_skin_friction_drag_coefficient(skingFrictionDrag, rocketFinenessRatio, rocketSurfaceArea, current_state.fin.max_thickness, meanChord, current_state.fin.superficial_area, reference_area)

    def __calculatePressureDragCoefficient(self, current_state: DeltaTimeSimulation) -> float:
        pass

    def __calculateDragCoefficient(self, current_state: DeltaTimeSimulation) -> float: # coef. arrasto final usado no calculo do arrasto
        pass

    def calculate(self, current_state: DeltaTimeSimulation):
        velocity = current_state.velocity.magnitudeRelativeTo(current_state.velocity)
        referenceArea = pi * current_state.nose.base_radius ** 2 
        if self.__drag_coefficient is None: # otimização, calcula apenas uma vez
            self.__drag_coefficient = self.__calculateDragCoefficient(current_state)

        self.__drag_coefficient = 0.5 # provisório

        magnitude = self.__calculateDrag(referenceArea, self.__drag_coefficient, velocity)

        dragForce = current_state.velocity * -1
        dragForce = dragForce.unitVector() * magnitude

        self.setX(dragForce.x())
        self.setY(dragForce.y())
        self.setZ(dragForce.z())
