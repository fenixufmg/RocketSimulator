from __future__ import annotations
from dataclasses import dataclass
from typing import Dict

@dataclass
class MaterialModel:
    name: str
    density: float
    yield_strength: float

    @staticmethod
    def from_json(dict: Dict) -> MaterialModel:
        return MaterialModel(name=dict['name'], density=dict['density'], yield_strength=dict['yield_strength'])