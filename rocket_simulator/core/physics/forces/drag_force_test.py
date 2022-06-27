from core.physics.forces.force import Force
from core.physics.delta_time_simulation import DeltaTimeSimulation
from core.physics.body.application_point import ApplicationPoint
from core.physics.vector import Vector
from utils.constants import Constants
from models.structure.nose_model import NoseModel
from math import pi


class DragForceTest(Force):
    def __init__(self):
        super().__init__(0, 0, 0, ApplicationPoint.CP, None)

    def calculate(self, current_state: DeltaTimeSimulation):
        dragCoefficient = 2

        # referenceArea = pi * NoseModel().__base_radius ** 2  # original
        referenceArea = pi * current_state.nose.base_radius ** 2  # certo

        airDensity = Constants.AIR_DENSITY.value

        # velocity = Vector.__calculateMagnitude(current_state.velocity)  # original
        velocity = current_state.velocity.magnitude()  # certo

        dragForce = 0.5 * airDensity * dragCoefficient * referenceArea * velocity ** 2

        self.setX(0)
        self.setY(0)
        self.setZ(dragForce)
