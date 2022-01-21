from dataclasses import dataclass

from abstract_component import AbstractComponent
from material_model import MaterialModel

@dataclass
class CylindricalBodyModel(AbstractComponent):
    index: int
    position: float
    height: float
    diameter: float
    thickness: float
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