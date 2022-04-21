from __future__ import annotations
from dataclasses import dataclass
from typing import Dict

class MaterialModel:
    def __init__(self, name):
        self.__name = name
        self.__density = None
        self.__yield_strength = None

    def name(self):
        return self.__name

    def density(self):
        return self.__density

    def yieldStrength(self):
        return self.__yield_strength

    @staticmethod
    def from_json(dict: Dict) -> MaterialModel: # mudar
        return MaterialModel(name=dict['name'], density=dict['density'], yield_strength=dict['yield_strength'])