from dataclasses import dataclass
from typing import List

from nose_model import NoseModel
from cylindrical_body_model import CylindricalBodyModel
from core.physics.body.rigid_body import RigidBody
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
