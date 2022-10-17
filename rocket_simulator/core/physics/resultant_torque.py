from typing import List

from core.physics.forces.force import Force
from core.physics.delta_time_simulation import DeltaTimeSimulation
from core.physics.body.application_point import ApplicationPoint
from math import pi

from core.physics.vector import Vector
from models.structure.rocket_model import RocketModel


class ResultantTorque(Vector):
    def __init__(self, forces: List[Force], additional_torques=[]):
        """ Recebe uma lista de torques e usa elas para calcular o torque resultante no tempo t. A lista DEVE ser ordenada
        em ordem de dependência com os torques menos dependentes primeiro, ou seja, se um torque depende de por exemplo
        a velocidade angular do foguete então ele deve vir por ultimo, porque todas os outros torques podem
        alterar a velocidade do foguete e gerar resultados diferentes. Esse erro deve atenuar ao se diminuir
        DELTA_TIME_SIMULATION.
        """
        # self.__rocket_length = rocket_length.unitVector()
        self.__forces = forces # DEVE ser ordenado de mais independente para menos independente
        self.__additional_torques = additional_torques
        super().__init__(0, 0, 0)

    def calculate(self, current_state: DeltaTimeSimulation):
        """ Calcula o torque resultante respeitando todas as peculiaridades e dependências dos outros torques.

        Args:
            current_state (DeltaTimeSimulation): Estado atual do foguete.
        """
        for force in self.__forces: # seguindo a ordem de dependência
            force.calculate(current_state)

        resultant_torque = Vector(0, 0, 0)
        for force in self.__forces:
            if force.application_point == ApplicationPoint.CG:
                continue
            
            lever = current_state.cg - current_state.cp
            torque = Vector.crossProduct(force, lever)
            resultant_torque += torque

        for torque in self.__additional_torques:
            torque.calculate(current_state)
            resultant_torque += torque

        self.setX(resultant_torque.x())
        self.setY(resultant_torque.y())
        self.setZ(resultant_torque.z())



