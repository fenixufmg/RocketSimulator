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

        self.__initialize()
        super().__init__(RocketParts.ROCKET, -1)

    def __orderAvailablePartsByPosition(self) -> List[AbstractModel]:
        ordered_parts = []
        i = -1
        while True:
            i += 1
            i_found = []
            for part in self.__getAvailableParts():
                if part.getPartPositionOrder() == i:
                    ordered_parts.append(part)
                    i_found.append(True)
                else:
                    i_found.append(False)

            i_found = [found == False for found in i_found]  # inverte os bools para usar o all() do jeito certo
            if all(i_found):  # para se todas as peças já foram ordenadas
                break

        return ordered_parts

    def __getPreviousPart(self, part):
        position_order = part.getPartPositionOrder()
        previous_position_order = position_order - 1 if position_order - 1 >= 0 else None

        for part in self.__getAvailableParts():
            if part.getPartPositionOrder() == previous_position_order:
                return part

    def __movePartsToPositions(self):
            ordered_parts = self.__orderAvailablePartsByPosition()
            for part in ordered_parts:
                part.centerOnOrigin()

                previous_part = self.__getPreviousPart(part)
                displacement = part.getTipDistanceToCg().magnitude() * -1
                if previous_part is not None:  # não é a primeira parte
                    displacement -= previous_part.getHeight()

                part.move(displacement) ## ERRADO trocar para vetor

                if part.getPartType() == RocketParts.FIN:
                    pass
                    continue

    def __initialize(self):
        self.__movePartsToPositions()

    def __getAvailableParts(self) -> List[AbstractModel]:
        available_parts = []
        for key, value in self.__parts.items():
            if value is None:
                continue

            if type(value) == list:
                for part in value:
                    available_parts.append(part)
                continue

            available_parts.append(value)

        return available_parts

    def calculateVolume(self) -> float:
        available_parts = self.__getAvailableParts()
        total_volume = 0

        for part in available_parts:
            total_volume += part.volume

        return total_volume

    def calculateMass(self) -> float:
        available_parts = self.__getAvailableParts()
        total_mass = 0

        for part in available_parts:
            total_mass += part.mass

        return total_mass

    def calculateMomentOfInertia(self, axis_offset_to_cg: float) -> float:  # axis_offset_to_cg pode ser negativo
        axis_offset_to_cg *= -1  # inverter para o sentido da simulação
        available_parts = self.__getAvailableParts()
        total_moment_of_inertia = 0

        for part in available_parts:
            part_distance_to_cg = self.cg - part.cg
            part_distance_to_axis = part_distance_to_cg.magnitude() + axis_offset_to_cg
            total_moment_of_inertia += part.calculateMomentOfInertia(part_distance_to_axis)

        return total_moment_of_inertia

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





