from abc import ABC
from core.physics.forces.force import Force
from typing import List

class AbstractAmbient(ABC):
    def __init__(self, forces:List[Force]) -> None:
        self.forces = forces
