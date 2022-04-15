from email.mime import application
from models.physics.point import Point
from models.physics.rigid_body import RigidBody
from models.physics.vector import Vector
from models.physics.force import Force
from models.physics.delta_time_simulation import DeltaTimeSimulation
import collections

class Physics:
    def __init__(self, rigid_body:RigidBody):
        self.__DELTA_TIME = 1
        self.__rigid_body = rigid_body
        self.__forces = [] 

    def simulate(self, time:int) -> dict:
        delta_time_simulations = {0: DeltaTimeSimulation(self.__rigid_body)}
        total_elapsed_time = 0

        for elapsed_time in range(1, time+1, self.__DELTA_TIME): # 1, 2, 3, 4, 5, ... , time
            total_elapsed_time += elapsed_time
            self.__applyForces(delta_time_simulations[-1])
            
            current_simulation = DeltaTimeSimulation(self.__rigid_body)
            delta_time_simulations[total_elapsed_time] = current_simulation

        delta_time_simulations = collections.OrderedDict(sorted(delta_time_simulations.items()))
        return delta_time_simulations 

    def __applyForces(self, last_simulation):
        for force in self.__forces:
            force.calculate(last_simulation) 
            self.__rigid_body.applyForce(force, self.__DELTA_TIME)

    def addForce(self, force:Force) -> None:
        self.__forces.append(force)




