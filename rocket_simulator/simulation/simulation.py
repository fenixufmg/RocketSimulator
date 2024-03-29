from multiprocessing.sharedctypes import Value
import numpy as np
from typing import List

from core.physics.forces.parachute_torque import ParachuteTorque
from core.physics.vector import Vector
from core.physics.forces.force import Force
from core.physics.delta_time_simulation import DeltaTimeSimulation
from models.structure.rocket_model import RocketModel
import collections

from core.physics.resultant_force import ResultantForce
from core.physics.resultant_torque import ResultantTorque
from core.physics.forces.parachute_drag_force import ParachuteDrag
from models.structure.parachute_model import ParachuteModel
from models.structure.parachute_model import EjectionCriteria
from simulation.abstract_ambient import AbstractAmbient
from utils.rocket_parts import RocketParts
from core.physics.forces.impulse_test_force import ImpulseTestForce


class Simulation:
    def __init__(self, rocket: RocketModel, ambient: AbstractAmbient, additional_forces: List[Force] = []):
        """ Classe responsável pela coordenação da simulação física.

        Args:
            rocket (RocketModel): Foguete no qual serão aplicadas as forças e extraídos os dados.
            ambient (AbstractAmbient): Ambiente no qual a simulação está imersa.
            additional_forces (List[Force]): Lista que contem as forças ADICIONAIS que serão usadas ao longo de toda a simulação.

        Fields:
            __DELTA_TIME (float): Tamanho do intervalo de tempo entre duas simulações, quanto menor mais próximo da realidade.
            __rocket (RocketModel) : Foguete.
            __forces (List[Force]): Lista que contem as forças que serão usadas ao longo de toda a simulação.
            __resultant_force (ResultantForce): Força resultante que atua no CG.
            __resultant_torque (ResultantTorque): Torque resultante em torno do CG.
        """
        self.__DELTA_TIME = 0.1
        self.__rocket = rocket

        self.__setupForces(ambient, additional_forces)
        self.__resultant_force: ResultantForce = ResultantForce(self.__forces)
        self.__resultant_torque: ResultantTorque = ResultantTorque(self.__forces)

    def __setupForces(self, ambient: AbstractAmbient, additional_forces: List[Force]):
        """"Adiciona as forças que serão usadas na simulação no campo __forces.

        Args:
            ambient (AbstractAmbient): Ambiente no qual a simulação ocorre.
            additional_forces (List[Force]): Lista que contem as forças ADICIONAIS que serão usadas ao longo de toda a simulação.

        Raises:
             ValueError: Foguete não tem motor, logo, não tem empuxo.

        """
        thrust = None
        try:
            thrust = self.__rocket.getPart(RocketParts.MOTOR).thrust
        except AttributeError:
            raise ValueError("Rocket doesn't have a motor")

        parachute_drag_force = ParachuteDrag()
        self.__forces = [*additional_forces, thrust, *ambient.forces, parachute_drag_force]
        # ordem das forças importa como explicado em resultant_force.py

    def __tryEjection(self, current_state: DeltaTimeSimulation):
        """Verifica constantemente se as condições de ejeção do paraquedas são atendidas, caso positivo ele é ejetado.

        Args:
            current_state (DeltaTimeSimulation): Estado atual.

        Raises:
            ValueError: Critério de ejeção não suportado.
        """
        parachute: ParachuteModel = current_state.parachute
        if parachute is None:  # não tem paraquedas
            return

        if parachute.ejection_criteria == EjectionCriteria.APOGEE:
            if current_state.velocity.z() < 0 and current_state.time > 0:  # ejetar
                parachute.eject()
        else:
            raise ValueError(f"Ejection criteria: {parachute.ejection_criteria} not supported")

    def __correctParachuteOrientation(self, current_state):
        """ Utilizado para setar a orientação do foguete para (0,0,1) quando o paraquedas for inflado.

        Args:
            current_state (DeltaTimeSimulation): estado atual da simulação.
        """
        parachute = current_state.parachute
        if parachute is None:  # não tem paraquedas
            return

        if parachute.inflated:
            self.__rocket.setLookingDirection(Vector(0, 0, 1))

    def simulate(self, time: int) -> dict:
        """Roda a simulação física até o tempo determinado pelo parâmetro time com intervalos de __DELTA_TIME.
        Calcula em toda iteração a força e torque resultante para aplicar no foguete.
        
        Args:
            time (float): Instante de tempo máximo simulado.
        Returns:
            delta_time_simulations (dict(float: DeltaTimeSimulation)): Dicionário contendo os instantes simulados nas 
            chaves e seus respectivos DeltaTimeSimulation's nos valores
        """
        delta_time_simulations = dict()

        for total_elapsed_time in np.arange(0, time + self.__DELTA_TIME,
                                            self.__DELTA_TIME):  # 0, 0.1, 0.2, 0.3, 0.4, 0.5, ... , time

            current_state = DeltaTimeSimulation(self.__rocket, total_elapsed_time)
            delta_time_simulations[total_elapsed_time] = current_state  # salva as informações do estado atual

            self.__tryEjection(current_state) # tenta ejetar
            self.__applyResultantForce(current_state)  # atualiza o estado para o futuro
            self.__applyResultantTorque(current_state)  # atualiza o estado para o futuro
            self.__rocket.updateState() # atualiza o estado (estrutural) do foguete
            self.__correctParachuteOrientation(current_state) # corrige orientação se paraquedas estiver inflado

        delta_time_simulations = collections.OrderedDict(sorted(delta_time_simulations.items())) # ordena pelo tempo
        return delta_time_simulations

    def __applyResultantForce(self, current_state: DeltaTimeSimulation):
        """Calcula e aplica a força resultante no foguete.

        Args:
            current_state (DeltaTimeSimulation): estado atual da simulação.
        """
        self.__resultant_force.calculate(current_state)
        self.__rocket.applyForce(self.__resultant_force, self.__DELTA_TIME)

    def __applyResultantTorque(self, current_state: DeltaTimeSimulation):
        """Calcula e aplica o torque resultante no foguete.

        Args:
            current_state (DeltaTimeSimulation): estado atual da simulação.
        """
        self.__resultant_torque.calculate(current_state)
        self.__rocket.applyTorque(self.__resultant_torque, self.__DELTA_TIME)
