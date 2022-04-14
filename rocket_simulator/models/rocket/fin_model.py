from dataclasses import dataclass

from abstract_component import AbstractComponent
from material_model import MaterialModel

@dataclass
class FinModel(AbstractComponent):
    body_index: int
    root_chord: float
    tip_chord: float
    span: float
    max_thickness: float
    sweep_angle: float
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