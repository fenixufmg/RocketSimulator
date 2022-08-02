from typing import List
from models.structure.abstract_model import AbstractModel

from core.physics.vector import Vector
from models.structure.fin_model import FinModel
from models.structure.abstract_model import AbstractModel
from core.physics.forces.force import Force
from utils.constants import Constants
from utils.rocket_parts import RocketParts


class RocketModel(AbstractModel):  # não está movendo as peças
    def __init__(self):
        self.parts = {RocketParts.NOSE: None, RocketParts.CYLINDRICAL_BODY: [], RocketParts.TRANSITION: [],
                      RocketParts.FIN: None, RocketParts.MOTOR: None}

        self.rocket_height: Vector = Vector(0, 0, 0)
        self.drag_coefficient = self.__calculateDragCoefficient()
        self.transversal_area = self.__calculateTransversalArea()

        super().__init__(RocketParts.ROCKET, -1, None, self.drag_coefficient, self.transversal_area)
        self.__verify()
        self.__initialize()

    def __verify(self):  # fazer
        pass

    def __calculateDragCoefficient(self):  # fazer
        pass

    def __calculateTransversalArea(self):  # fazer
        pass

    def __orderAvailablePartsByPosition(self) -> List[AbstractModel]:
        ordered_parts = []
        i = -1
        while True:
            i += 1
            i_found = []
            available_parts = self.__getAvailableParts()
            for part in available_parts:
                if part.position_order == i:
                    ordered_parts.append(part)
                    i_found.append(True)
                else:
                    i_found.append(False)

            if i < len(available_parts): # certifica que toda a lista de partes é percorrida
                continue

            i_found = [found == False for found in i_found]  # inverte os bools para usar o all() do jeito certo
            if all(i_found):  # para se todas as peças já foram ordenadas
                break
        return ordered_parts

    def getPartWithPositionOrder(self, position_order):
        for part in self.__getAvailableParts():
            if part.position_order == position_order:
                return part

    def __getPreviousPart(self, part):
        position_order = part.position_order
        previous_position_order = position_order - 1

        while previous_position_order >= 0: # vai até a primeira parte
            previous_part = self.getPartWithPositionOrder(previous_position_order)
            if previous_part is not None: # parte encontrada
                return previous_part

            previous_position_order -= 1

    def __putRocketOnGround(self):
        for part in self.__getAvailableParts():
            part.move(self.rocket_height, ignore_ground=True)

    def __movePartsToPositions(self):
        ordered_parts = self.__orderAvailablePartsByPosition()
        self.rocket_height = Vector(0, 0, 0)
        for part in ordered_parts:
            part.centerOnOrigin()
            displacement = part.getTipDistanceToCg().magnitude() * -1  # move a própria altura acima do cg
            displacement = Vector(0, 0, displacement)

            previous_part = self.__getPreviousPart(part)
            if previous_part is None:  # primeira parte
                self.rocket_height = Vector(0, 0, part.height)

            if previous_part is not None:  # não é a primeira parte
                current_part_height = Vector(0, 0, part.height)
                self.rocket_height += current_part_height

                displacement -= (self.rocket_height - current_part_height)  # move a altura das peças anteriores
                # print(part.part_type)
                # print(displacement)

            part.move(displacement, ignore_ground=True)

            if part.part_type == RocketParts.FIN:
                part: FinModel = part  # só para tirar o erro do INTELLIJ
                displacement = Vector(0, 0, part.root_chord + part.distance_to_base)
                part.move(displacement, ignore_ground=True)

                print(part.delimitation_points[0])
                print(part.delimitation_points[1])
            #     distance_from_center = Vector(part.distance_from_center, 0, 0)

            #     for degrees in range(0, 361, 360 // part.nb_fins):  # rotaciona as aletas
            #         if degrees == 0:
            #             continue
            #         radians = degrees / 180
            #         radians *= Constants.PI.value
            #         z_axis = Vector(0, 0, 1)
            #         displacement = Vector.rotateAroundAxis(distance_from_center, z_axis, radians)
            #         part.move(displacement, ignore_ground=True)

        self.__putRocketOnGround()

    def __initialize(self):
        self.__movePartsToPositions()

    def __getAvailableParts(self) -> List[AbstractModel]:
        available_parts = []
        for key, value in self.parts.items():
            if value is None:
                continue

            if type(value) == list:
                for part in value:
                    available_parts.append(part)
                continue

            available_parts.append(value)

        return available_parts

    def updateState(self) -> None:
        self.volume = self.calculateVolume()
        self.mass = self.calculateMass()
        # self.moment_of_inertia = self.calculateMomentOfInertia()
        self.cg = self.calculateCg()
        self.cp = self.calculateCp()
        self.delimitation_points = self.createDelimitationPoints()

        for part in self.__getAvailableParts():
            part.updateState()

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
        if len(available_parts) == 0:
            return

        total_moment_of_inertia = 0

        for part in available_parts:
            part_distance_to_cg = self.cg - part.cg
            part_distance_to_axis = part_distance_to_cg.magnitude() + axis_offset_to_cg
            total_moment_of_inertia += part.calculateMomentOfInertia(part_distance_to_axis)

        return total_moment_of_inertia

    def calculateCg(self) -> Vector:
        total_mass = 0
        cg = Vector(0, 0, 0)
        available_parts = self.__getAvailableParts()

        if len(available_parts) == 0:
            return

        for part in available_parts:
            total_mass += part.mass
            # print(f"Part cg: {part.cg}")
            cg += part.cg * part.mass

        cg = cg * (1 / total_mass)
        # print("===================")
        # print(f"Calculating cg")
        # print(f"    Old: {self.cg}")
        # print(f"    New: {cg}")
        return cg

    def calculateCp(self) -> Vector:
        total_shape_coefficient = 0
        cp = Vector(0, 0, 0)
        available_parts = self.__getAvailableParts()

        if len(available_parts) == 0:
            return

        for part in available_parts:
            cp += part.cp * part.shape_coefficient
            total_shape_coefficient += part.shape_coefficient

        cp = cp * (1 / total_shape_coefficient)
        # print(f"Calculating cp")
        # print(f"    Old: {self.cp}")
        # print(f"    New: {cp}")
        return cp

    def createDelimitationPoints(self) -> list:
        ordered_parts = self.__orderAvailablePartsByPosition()
        if len(ordered_parts) == 0:
            return [Vector(0, 0, 0), Vector(0, 0, 0)]

        first_part: AbstractModel = ordered_parts[0]
        last_part: AbstractModel = ordered_parts[-1]

        delimitation_points = [first_part.delimitation_points[0], last_part.delimitation_points[1]]
        return delimitation_points

    def addPart(self, part: AbstractModel):  # adiciona instâncias
        if part.part_type == RocketParts.CYLINDRICAL_BODY or part.part_type == RocketParts.TRANSITION:  #
            # adiciona na lista
            part_list = self.parts[part.part_type]
            part_list.append(part)
            self.parts[part.part_type] = part_list
            self.__movePartsToPositions()
            self.updateState()
            return

        if self.parts[part.part_type] is not None:  # parte já existe
            raise ValueError(f"Cant have two parts of type {part.part_type}")

        self.parts[part.part_type] = part  # adiciona parte única
        self.__movePartsToPositions()
        self.updateState()

    def removePart(self, part: AbstractModel):  # remove instâncias
        if part.part_type == RocketParts.CYLINDRICAL_BODY or part.part_type == RocketParts.TRANSITION:  #
            # remove da lista
            part_list = self.parts[part.part_type]
            part_list.remove(part)
            self.parts[part.part_type] = part_list
            self.__movePartsToPositions()
            self.updateState()
            return

        if self.parts[part.part_type] is None:  # parte não existe
            raise ValueError(f"Part type {part.part_type} doesnt exist")

        if self.parts[part.part_type] == part:  # condicionado pela INSTÂNCIA
            self.parts[part.part_type] = None  # remove parte única
            self.__movePartsToPositions()
            self.updateState()
        else:  # INSTÂNCIA não encontrada
            raise ValueError("Part instance doesnt exist")

    def getPart(self, part_type: RocketParts):
        for part in self.__getAvailableParts():
            if part.part_type == part_type:
                return part

        # print(f"Part type {part_type.value} doesnt exist")

    def getParts(self) -> List[AbstractModel]:
        return self.__getAvailableParts()

    def move(self, displacement: Vector, ignore_ground=False):
        super().move(displacement, ignore_ground=ignore_ground)

        for part in self.__getAvailableParts():
            part.move(displacement, ignore_ground=ignore_ground)

    def rotate(self, angular_displacement: Vector, axis_displacement: Vector = Vector(0, 0, 0)):
        super().rotate(angular_displacement)

        for part in self.__getAvailableParts():
            axis_displacement = part.cg - self.cg
            part.rotate(angular_displacement, axis_displacement=axis_displacement)
