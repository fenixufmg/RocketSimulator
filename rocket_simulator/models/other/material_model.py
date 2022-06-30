import json
from utils.paths import Paths
import os

class MaterialModel:
    def __init__(self, name:str):
        self.name = name.lower().strip() # arrumar para usar enums
        self.density = None
        self.yield_strength = None
        self.__initialize()

    def __initialize(self):
        materials_folder = Paths.MATERIALS.value

        material_file = f"{materials_folder}/{self.name}.json"
        with open(material_file) as material_file:
            data = json.load(material_file)

            self.density = data["density"]
            self.yield_strength = data["yield_strength"]