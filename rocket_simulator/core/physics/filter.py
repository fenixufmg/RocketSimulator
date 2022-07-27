from typing import List
from core.physics.delta_time_simulation import DeltaTimeSimulation

class Filter:
    def __init__(self, step=None) -> None:
        self.__step = step

    def filter(delta_time_simulations: List[DeltaTimeSimulation]) -> List[DeltaTimeSimulation]:
        pass

