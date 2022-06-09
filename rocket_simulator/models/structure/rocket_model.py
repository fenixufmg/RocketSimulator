from typing import List
from models.structure.abstract_model import AbstractModel

from nose_model import NoseModel
from cylindrical_body_model import CylindricalBodyModel
from core.physics.body.rigid_body import RigidBody
from core.physics.vector import Vector
from transition_model import TransitionModel
from fin_model import FinModel
from motor_model import MotorModel
from models.structure.abstract_model import AbstractModel
from utils.rocket_parts import RocketParts


class RocketModel(AbstractModel):
    def __init__(self):
        self.__parts = {RocketParts.NOSE: None, RocketParts.CYLINDRICAL_BODY: [], RocketParts.TRANSITION: [],
                        RocketParts.FIN: None, RocketParts.MOTOR: None}

        super().__init__(RocketParts.ROCKET)

    def calculateVolume(self) -> float:
        raise NotImplementedError("Function not implemented")

    def calculateMass(self) -> float:
        raise NotImplementedError("Function not implemented")

    def calculateMomentOfInertia(self, distance_to_cg: float) -> float:
        raise NotImplementedError("Function not implemented")

    def calculateCg(self) -> Vector:
        raise NotImplementedError("Function not implemented")

    def calculateCp(self) -> Vector:
        raise NotImplementedError("Function not implemented")

    def createDelimitationPoints(self) -> list:
        raise NotImplementedError("Function not implemented")

    def addPart(self, part: AbstractModel):  # adiciona instâncias
        if part.getPartType() == RocketParts.CYLINDRICAL_BODY or part.getPartType() == RocketParts.TRANSITION:  #
            # adiciona na lista
            part_list = self.__parts[part.getPartType()]
            part_list.append(part)
            self.__parts[part.getPartType()] = part_list
            return

        if self.__parts[part.getPartType()] is not None:  # parte já existe
            raise ValueError(f"Cant have two parts of type {part.getPartType()}")

        self.__parts[part.getPartType()] = part  # adiciona parte única

    def removePart(self, part: AbstractModel):  # remove instâncias
        if part.getPartType() == RocketParts.CYLINDRICAL_BODY or part.getPartType() == RocketParts.TRANSITION:  #
            # remove da lista
            part_list = self.__parts[part.getPartType()]
            part_list.remove(part)
            self.__parts[part.getPartType()] = part_list
            return

        if self.__parts[part.getPartType()] is None:  # parte não existe
            raise ValueError(f"Part type {part.getPartType()} doesnt exist")

        if self.__parts[part.getPartType()] == part:  # condicionado pela INSTÂNCIA
            self.__parts[part.getPartType()] = None  # remove parte única
        else:  # INSTÂNCIA não encontrada
            raise ValueError("Part instance doesnt exist")



