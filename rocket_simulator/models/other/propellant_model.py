import json
from utils.paths import Paths
from models.structure.abstract_model import AbstractModel

class PropellantModel(AbstractModel):
    def __init__(self, name): # ???? definir parametros
        """ Classe que representa o propelente utilizado.
        """
        self.__name = name.lower().strip()
        self.__ratio = None
        self.__density = None
        self.__a = None
        self.__n = None
        self.__k = None
        self.__initialize()
        pass

    def __initialize(self):
        propellants_folder = Paths.PROPELLANTS.value

        propellant_file = f"{propellants_folder}/{self.__name}.json"
        propellant_file = json.loads(propellant_file)

        self.__ratio = propellant_file["ratio"]
        self.__density = propellant_file["density"]
        self.__a = propellant_file["a"]
        self.__n = propellant_file["n"]
        self.__k = propellant_file["k"]

    def interpolateThrust(self, time:float):
        pass