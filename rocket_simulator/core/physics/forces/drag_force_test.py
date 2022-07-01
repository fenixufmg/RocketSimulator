import imp
from core.physics.forces.force import Force
from core.physics.delta_time_simulation import DeltaTimeSimulation
from core.physics.body.application_point import ApplicationPoint
from core.physics.vector import Vector
from core.aerodynamic.drag import drag
from utils.constants import Constants
from models.structure.nose_model import NoseModel
from math import pi
# from core.aerodynamic.drag import drag


class DragForceTest(Force):
    def __init__(self):
        super().__init__(0, 0, 0, ApplicationPoint.CP, None)

    def calculate(self, current_state: DeltaTimeSimulation):
        dragCoefficient = 2

        # referenceArea = pi * NoseModel().__base_radius ** 2  # original
        referenceArea = pi * current_state.nose.base_radius ** 2  # certo
        # a secção transversal no calculo do arrasto é so a do nariz? se não for fala cmg pra gente ver como fazer

        # velocity = Vector.__calculateMagnitude(current_state.velocity)  # original
        print(current_state.velocity)
        velocity = current_state.velocity.magnitude()  # certo
        
        magnitude = drag(referenceArea, dragCoefficient, velocity)

        self.setX(0)
        self.setY(0)
        self.setZ(magnitude)
