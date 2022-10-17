from typing import List

from core.physics.forces.force import Force
from core.physics.delta_time_simulation import DeltaTimeSimulation
from core.physics.body.application_point import ApplicationPoint
from math import pi

from core.physics.vector import Vector
from models.structure.rocket_model import RocketModel


class ResultantForce(Force):
    def __init__(self, forces: List[Force]):
        """ Recebe uma lista de forças e usa elas para calcular a força resultante no tempo t. A lista DEVE ser ordenada
        em ordem de dependência com as forças menos dependentes primeiro, ou seja, se uma força depende de por exemplo
        a velocidade do foguete (como o arrasto) então ela deve vir por ultimo, porque todas as outras forças podem
        alterar a velocidade do foguete e gerar resultados diferentes. Esse erro deve atenuar ao se diminuir
        DELTA_TIME_SIMULATION.
        """
        self.__forces = forces # DEVE ser ordenado de mais independente para menos independente
        super().__init__(0, 0, 0, ApplicationPoint.CG)

    def calculate(self, current_state: DeltaTimeSimulation):
        """ Calcula a força resultante respeitando todas as peculiaridades e dependências das outras forças.

        Args:
            current_state (DeltaTimeSimulation): Estado atual do foguete.
        """
        for force in self.__forces: # seguindo a ordem de dependência
            force.calculate(current_state)

        resultant_force = Vector(0, 0, 0)
        for force in self.__forces:
            resultant_force += force

        self.setX(resultant_force.x())
        self.setY(resultant_force.y())
        self.setZ(resultant_force.z())



