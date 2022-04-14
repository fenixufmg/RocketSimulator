from dataclasses import dataclass
from typing import List

from nose_model import NoseModel
from cylindrical_body_model import CylindricalBodyModel
from models.physics.rigid_body import RigidBody
from transition_model import TransitionModel
from fin_model import FinModel

class RocketModel:
    def __init__(self, nose:NoseModel, cylindrical_bodies:List[CylindricalBodyModel], transitions:List[TransitionModel], fin:FinModel):
        self.__nose = nose
        self.__cylindrical_bodies = cylindrical_bodies
        self.__transitions = transitions
        self.__fin = fin
        self.__rigid_body = self.__createRigidBody()

    def __createRigidBody():
        pass
