from abc import ABC, abstractmethod
from core.physics.forces.force import Force
from typing import List
from core.physics.body.rigid_body import RigidBody
from core.physics.forces.impulse_test_force import ImpulseTestForce
from simulation.simulation import Simulation
from models.structure.rocket_model import RocketModel

class AbstractAmbient(ABC):
    def __init__(self, rocket:RocketModel, forces:List[Force]) -> None:
        thrust_test = ImpulseTestForce(200) # provisório
        self.__forces = forces
        self.__forces.append(thrust_test)
        self.__rocket = rocket

    def addForce(self, force:Force):
        self.__forces.append(force)

    def simulate(self, simulation_time:int) -> dict:
        simulation = Simulation(self.__rocket, self.__forces)
        return simulation.simulate(simulation_time)