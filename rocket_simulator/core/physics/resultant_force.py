from typing import List

from core.physics.forces.force import Force
from core.physics.delta_time_simulation import DeltaTimeSimulation
from core.physics.body.application_point import ApplicationPoint
from math import pi

from core.physics.vector import Vector
from models.structure.rocket_model import RocketModel


class ResultantForce(Force):
    def __init__(self, forces: List[Force]):
        self.__forces = forces # DEVE ser ordenado de mais independente para menos independente
        super().__init__(0, 0, 0, ApplicationPoint.CG)

    def calculate(self, current_state: DeltaTimeSimulation):
        for force in self.__forces: # seguindo a ordem de dependência
            force.calculate(current_state)

        resultant_force = Vector(0, 0, 0)
        for force in self.__forces:
            resultant_force += force

        self.setX(resultant_force.x())
        self.setY(resultant_force.y())
        self.setZ(resultant_force.z())



