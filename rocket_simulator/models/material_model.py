from dataclasses import dataclass
from enum import Enum

class MaterialType(Enum):
    none = 1
    aluminum = 2
    titanium = 3

@dataclass
class MaterialModel:
    type: MaterialType

    def density(self) -> float:
        if self.type == MaterialType.titanium:
            return 1
        elif self.type == MaterialType.aluminum:
            return 1
        else:
            return None
