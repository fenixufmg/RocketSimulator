from dataclasses import dataclass
from enum import Enum

from abstract_component import AbstractComponent
from material_model import MaterialModel

class NoseType(Enum):
    none = 1
    parabolic = 2
    cubic = 3

@dataclass
class NoseModel(AbstractComponent):
    index: int
    height: float
    base_diameter: float
    thickness: float
    type: NoseType
    material: MaterialModel

    # Override abstract method
    def mass(self) -> float:
        return 1

    # Override abstract method
    def cg(self) -> float:
        return 1
    
    # Override abstract method
    def cp(self) -> float:
        return 1