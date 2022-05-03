from __future__ import annotations
import json
from utils.paths import Paths

class MaterialModel:
    def __init__(self, name:str):
        self.__name = name.lower().strip()
        self.__density = None
        self.__yield_strength = None
        self.__initialize()

    def __initialize(self):
        materials_folder = Paths.MATERIALS.value

        material_file = f"{materials_folder}/{self.__name}.json"
        material_file = json.loads(material_file)

        self.__density = material_file["density"]
        self.__yield_strength = material_file["yield_strength"]

    def name(self):
        return self.__name

    def density(self):
        return self.__density

    def yieldStrength(self):
        return self.__yield_strength