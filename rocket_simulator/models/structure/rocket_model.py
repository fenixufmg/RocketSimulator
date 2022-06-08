from dataclasses import dataclass
from typing import List
from models.structure.abstract_model import AbstractModel

from nose_model import NoseModel
from cylindrical_body_model import CylindricalBodyModel
from core.physics.body.rigid_body import RigidBody
from core.physics.vector import Vector
from transition_model import TransitionModel
from fin_model import FinModel
from models.structure.abstract_model import AbstractModel

class RocketModel(AbstractModel):
    def __init__(self, nose:NoseModel, cylindrical_bodies:List[CylindricalBodyModel], transitions:List[TransitionModel], fin:FinModel):
        self.__nose = nose
        self.__cylindrical_bodies = cylindrical_bodies
        self.__transitions = transitions
        self.__fin = fin
        super().__init__()

    def calculateVolume(self) -> float:
        raise NotImplementedError("Function not implemented")

    def calculateMass(self)-> float:
        raise NotImplementedError("Function not implemented")

    def calculateMomentOfInertia(self, distance_to_cg:float) -> float:
        raise NotImplementedError("Function not implemented")

    def calculateCg(self) -> Vector:
        raise NotImplementedError("Function not implemented")

    def calculateCp(self) -> Vector: 
        raise NotImplementedError("Function not implemented")

    def createDelimitationPoints(self) -> list:
        raise NotImplementedError("Function not implemented")

    def __refresh(self):
        pass

    def addPart(self, part:AbstractModel):
        pass
    
    def removePart(self, part:AbstractModel):
        pass

  

