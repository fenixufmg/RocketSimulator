from typing import List

from core.physics.forces.force import Force
from core.physics.delta_time_simulation import DeltaTimeSimulation
from core.physics.body.application_point import ApplicationPoint
from math import pi

from core.physics.vector import Vector
from models.structure.rocket_model import RocketModel


class ResultantTorque(Vector):
    def __init__(self, rocket_length: Vector, forces: List[Force]):
        self.__rocket_length = rocket_length.unitVector()
        self.__forces = forces # DEVE ser ordenado de mais independente para menos independente
        super().__init__(0, 0, 0)

    def calculate(self, current_state: DeltaTimeSimulation):
        for force in self.__forces: # seguindo a ordem de dependência
            force.calculate(current_state)

        resultant_torque = Vector(0, 0, 0)
        for force in self.__forces:
            if force.cg_offset is None or force.cg_offset == 0:
                continue
            
            print("a")
            lever = self.__rocket_length * -force.cg_offset # negativo para apontar para o cg
            torque = Vector.crossProduct(force, lever)
            resultant_torque += torque

        print(resultant_torque)
        self.setX(resultant_torque.x())
        self.setY(resultant_torque.y())
        self.setZ(resultant_torque.z())



