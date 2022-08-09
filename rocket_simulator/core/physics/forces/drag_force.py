import imp
from core.physics.forces.force import Force
from core.physics.delta_time_simulation import DeltaTimeSimulation
from core.physics.body.application_point import ApplicationPoint
from core.physics.vector import Vector
from utils.constants import Constants
from models.structure.nose_model import NoseModel
from math import pi

class DragForce(Force):
    def __init__(self):
        super().__init__(0, 0, 0, ApplicationPoint.CP, None)
        self.__drag_coefficient = None

    def __calculateDrag(self, transversal_section_area:float, drag_coefficient:float, velocity:float):
        air_density = Constants.AIR_DENSITY.value
        return ((1/2)*air_density*velocity**2*transversal_section_area*drag_coefficient)

    def __calculateSkinDragCoefficient(self,  current_state: DeltaTimeSimulation) -> float: # coef. arrasto de pele
        pass

    def __calculateDragCoefficient(self, current_state: DeltaTimeSimulation) -> float: # coef. arrasto final usado no calculo do arrasto
        pass

    def calculate(self, current_state: DeltaTimeSimulation):
        if self.__drag_coefficient is None: # otimização, calcula apenas uma vez
            self.__drag_coefficient = self.__calculateDragCoefficient(current_state)

        self.__drag_coefficient = 0.5 # provisório
        referenceArea = pi * current_state.nose.base_radius ** 2 

        velocity = current_state.velocity.magnitudeRelativeTo(current_state.velocity)
        magnitude = self.__calculateDrag(referenceArea, self.__drag_coefficient, velocity)

        dragForce = current_state.velocity * -1
        dragForce = dragForce.unitVector() * magnitude

        self.setX(dragForce.x())
        self.setY(dragForce.y())
        self.setZ(dragForce.z())
