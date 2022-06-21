from core.physics.forces.force import Force
from core.physics.delta_time_simulation import DeltaTimeSimulation
from core.physics.body.application_point import ApplicationPoint
from utils.constants import Constants
from models.structure.nose_model import NoseModel
from math import pi

class DragForceTest(Force):
    def __init__(self):
        super().__init__(0,0,0, ApplicationPoint.CP, None)
    
    def calculate(self, current_state: DeltaTimeSimulation):
        dragCoefficient = 2
        referenceArea = pi * NoseModel().__base_radius ** 2
        airDensity = Constants.AIR_DENSITY.value
        velocity = current_state.velocity
        dragForce = 0.5 * airDensity * dragCoefficient * referenceArea * velocity ** 2

        self.setX(0)
        self.setY(0)
        self.setZ(dragForce)