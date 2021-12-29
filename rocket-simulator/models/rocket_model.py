from dataclasses import dataclass
from typing import List

from nose_model import NoseModel
from cylindrical_body_model import CylindricalBodyModel
from transition_model import TransitionModel
from fin_model import FinModel

@dataclass
class RocketModel:
    nose: NoseModel
    cylindrical_body: List[CylindricalBodyModel]
    transition: List[TransitionModel]
    fin: FinModel