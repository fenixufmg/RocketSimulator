from abc import ABC
from core.physics.forces.force import Force
from typing import List
from core.physics.forces.impulse_test_force import ImpulseTestForce

class AbstractAmbient(ABC):
    def __init__(self, forces:List[Force]) -> None:
        thrust_test = ImpulseTestForce(200) # provisório
        self.forces = forces
        self.forces.append(thrust_test)
