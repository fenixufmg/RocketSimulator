from utils.paths import Paths
from core.physics.body.rigid_body import RigidBody
from other.material_model import MaterialModel
from models.structure.abstract_model import AbstractModel
import json

class ParachuteModel(AbstractModel):
    def __init__(self, name): # ???? definir parametros
        self.__name = name.lower().strip()
        self.__drag_coefficient = None
        self.__rigid_body = self.__createRigidBody()
        self.__initialize()

    def __initialize(self):
        parachutes_folder = Paths.PARACHUTES.value

        parachutes_folder = f"{parachutes_folder}/{self.__name}.json"
        parachutes_folder = json.loads(parachutes_folder)

        self.__drag_coefficient = parachutes_folder["drag_coefficient"]

    def __createRigidBody():
        pass