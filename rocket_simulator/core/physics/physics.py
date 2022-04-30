from email.mime import application

from core.physics.body.rigid_body import RigidBody
from core.physics.vector import Vector
from core.physics.forces.force import Force
from core.physics.delta_time_simulation import DeltaTimeSimulation
import collections

class Physics:
    def __init__(self, rigid_body:RigidBody):
        self.__DELTA_TIME = 1
        self.__rigid_body = rigid_body
        self.__forces = [] 

    def simulate(self, time:int) -> dict:
        # delta_time_simulations = {0: DeltaTimeSimulation(self.__rigid_body, 0)}
        delta_time_simulations = dict()

        for total_elapsed_time in range(0, time+1, self.__DELTA_TIME): # 0, 1, 2, 3, 4, 5, ... , time
            
            current_state = DeltaTimeSimulation(self.__rigid_body, total_elapsed_time)
            delta_time_simulations[total_elapsed_time] = current_state # salva as informações do estado atual

            self.__applyForces(current_state) # atualiza o estado para o futuro
            
            

        delta_time_simulations = collections.OrderedDict(sorted(delta_time_simulations.items()))
        return delta_time_simulations 

    def __applyForces(self, current_state):
        for force in self.__forces:
            force.calculate(current_state) 
            self.__rigid_body.applyForce(force, self.__DELTA_TIME)

    def addForce(self, force:Force) -> None:
        self.__forces.append(force)




