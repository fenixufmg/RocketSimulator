from email.mime import application

from core.physics.body.rigid_body import RigidBody
from core.physics.vector import Vector
from core.physics.forces.force import Force
from core.physics.delta_time_simulation import DeltaTimeSimulation
from models.structure.rocket_model import RocketModel
import collections

class Simulation:
    def __init__(self, rocket: RocketModel):
        """ Classe responsável pela coordenação da simulação física.

        Args:
            rocket (RocketModel): Foguete no qual serão aplicadas as forças e extraídos os dados.

        Fields:
            __DELTA_TIME (float): Tamanho do intervalo de tempo entre duas simulações, quanto menor mais próximo da realidade.
            __forces (List[Force]): Lista que contem as forças que serão usadas ao longo de toda a simulação.
        """
        self.__DELTA_TIME = 1
        self.__rocket = rocket
        self.__forces = [] 

    def simulate(self, time:int) -> dict:
        """Roda a simulação física até o tempo determinado pelo parâmetro time com intervalos de __DELTA_TIME.
        
        Args:
            time (float): Instante de tempo máximo simulado.
        Returns:
            delta_time_simulations (dict(float: DeltaTimeSimulation)): Dicionário contendo os instantes simulados nas 
            chaves e seus respectivos DeltaTimeSimulation's nos valores
        """
        delta_time_simulations = dict()

        for total_elapsed_time in range(0, time+1, self.__DELTA_TIME): # 0, 1, 2, 3, 4, 5, ... , time
            
            current_state = DeltaTimeSimulation(self.__rocket, total_elapsed_time)
            delta_time_simulations[total_elapsed_time] = current_state # salva as informações do estado atual

            self.__applyForces(current_state) # atualiza o estado para o futuro
            self.__rocket.updateState()

        delta_time_simulations = collections.OrderedDict(sorted(delta_time_simulations.items()))
        return delta_time_simulations 

    def __applyForces(self, current_state):
        """Diz as forças que foram denifidas em __foces para calcular seus valores com base no estado atual 
        e depois aplica todas elas no corpo rígido.

        Args:
            current_state (DeltaTimeSimulation): Estado atual do corpo.
        """
        for force in self.__forces:
            force.calculate(current_state) 
            
        self.__rocket.applyForces(self.__forces, self.__DELTA_TIME)

    def addForce(self, force:Force) -> None:
        """Adiciona uma força no campo __forces.

        Args:
            force (Force): Força a ser adicionada.
        """
        self.__forces.append(force)




