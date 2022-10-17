from abc import ABC
from core.physics.forces.force import Force
from typing import List


class AbstractAmbient(ABC):
    def __init__(self, forces:List[Force]) -> None:
        """ Uma classe que extende essa representa um conjunto de forças comuns que o foguete vai sofrer naquele
         ambiente, como drag, lift, weight e etc.

         Args:
             forces (List[Force]): Lista de forças comuns daquele ambiente.
        """
        self.forces = forces
