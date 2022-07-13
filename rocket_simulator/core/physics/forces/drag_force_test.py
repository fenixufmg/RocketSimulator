import imp
from core.physics.forces.force import Force
from core.physics.delta_time_simulation import DeltaTimeSimulation
from core.physics.body.application_point import ApplicationPoint
from core.physics.vector import Vector
from core.aerodynamic.drag import drag
from utils.constants import Constants
from models.structure.nose_model import NoseModel
from math import pi


class DragForceTest(Force):
    def __init__(self):
        super().__init__(0, 0, 0, ApplicationPoint.CP, None)

    def calculate(self, current_state: DeltaTimeSimulation):
        dragCoefficient = 0.5
        referenceArea = pi * current_state.nose.base_radius ** 2  # certo
        # a secção transversal no calculo do arrasto é so a do nariz? se não for fala cmg pra gente ver como fazer
        velocity = current_state.velocity.magnitudeRelativeTo(current_state.velocity)
        print(velocity)
        magnitude = drag(referenceArea, dragCoefficient, velocity)
        dragForce = current_state.velocity * -1
        dragForce = dragForce.unitVector() * magnitude
        print(dragForce.magnitudeRelativeTo(current_state.velocity))
        print("====================")

        self.setX(dragForce.x())
        self.setY(dragForce.y())
        self.setZ(dragForce.z())
