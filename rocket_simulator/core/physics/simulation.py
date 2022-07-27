import numpy as np
from typing import List

from core.physics.body.rigid_body import RigidBody
from core.physics.vector import Vector
from core.physics.forces.force import Force
from core.physics.delta_time_simulation import DeltaTimeSimulation
from models.structure.rocket_model import RocketModel
import collections

from core.physics.resultant_force import ResultantForce
from core.physics.resultant_torque import ResultantTorque

class Simulation:
    def __init__(self, rocket: RocketModel, forces: List[Force]):
        """ Classe responsável pela coordenação da simulação física.

        Args:
            rocket (RocketModel): Foguete no qual serão aplicadas as forças e extraídos os dados.
            forces (List[Force]): Lista que contem as forças que serão usadas ao longo de toda a simulação.

        Fields:
            __DELTA_TIME (float): Tamanho do intervalo de tempo entre duas simulações, quanto menor mais próximo da realidade.
            __forces (List[Force]): Lista que contem as forças que serão usadas ao longo de toda a simulação.
            __resultant_force (ResultantForce): Força resultante que atua no cg.
            __resultant_torque (ResultantTorque): Torque resultante.
        """
        self.__DELTA_TIME = 0.1
        self.__rocket = rocket
        self.__forces = forces
        self.__resultant_force:ResultantForce = ResultantForce(forces)
        self.__resultant_torque:ResultantTorque = ResultantTorque(forces)

    def simulate(self, time:int) -> dict:
        """Roda a simulação física até o tempo determinado pelo parâmetro time com intervalos de __DELTA_TIME.
        
        Args:
            time (float): Instante de tempo máximo simulado.
        Returns:
            delta_time_simulations (dict(float: DeltaTimeSimulation)): Dicionário contendo os instantes simulados nas 
            chaves e seus respectivos DeltaTimeSimulation's nos valores
        """
        delta_time_simulations = dict()

        for total_elapsed_time in np.arange(0, time+self.__DELTA_TIME, self.__DELTA_TIME): # 0, 1, 2, 3, 4, 5, ... , time
            
            current_state = DeltaTimeSimulation(self.__rocket, total_elapsed_time)
            delta_time_simulations[total_elapsed_time] = current_state # salva as informações do estado atual

            # self.__applyForces(current_state) # atualiza o estado para o futuro
            self.__applyResultantForce(current_state) # atualiza o estado para o futuro
            self.__applyResultantTorque(current_state) # atualiza o estado para o futuro
            # self.__rocket.cp = self.__rocket.cg
            self.__rocket.updateState()
            # self.__rocket.cp = self.__rocket.cg

        delta_time_simulations = collections.OrderedDict(sorted(delta_time_simulations.items()))
        return delta_time_simulations 

    # def __applyForces(self, current_state):
    #     """Diz as forças que foram denifidas em __foces para calcular seus valores com base no estado atual 
    #     e depois aplica todas elas no corpo rígido.

    #     Args:
    #         current_state (DeltaTimeSimulation): Estado atual do corpo.
    #     """
    #     for force in self.__forces:
    #         force.calculate(current_state) 
            
    #     self.__rocket.applyForces(self.__forces, self.__DELTA_TIME)

    # def addForce(self, force:Force) -> None:
    #     """Adiciona uma força no campo __forces.

    #     Args:
    #         force (Force): Força a ser adicionada.
    #     """
    #     self.__forces.append(force)

    def __applyResultantForce(self, current_state):
        """Aplica a força resultante no corpo
        """
        self.__resultant_force.calculate(current_state)
        self.__rocket.applyForce(self.__resultant_force, self.__DELTA_TIME)

    def __applyResultantTorque(self, current_state):
        """Aplica o torque resultante no corpo.
        """
        self.__resultant_torque.calculate(current_state)
        self.__rocket.applyTorque(self.__resultant_torque, self.__DELTA_TIME)




