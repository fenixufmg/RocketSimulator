from enum import Enum
from typing import List
from models.structure.abstract_model import AbstractModel

from core.physics.vector import Vector
from models.structure.fin_model import FinModel
from models.structure.abstract_model import AbstractModel
from core.physics.forces.force import Force
from utils.constants import Constants
from utils.rocket_parts import RocketParts
    
class RocketModel(AbstractModel):
    def __init__(self):
        """Representa o foguete, guarda suas peças e é responsável por ordena-las no espaço e juntar suas características
        físicas (como massa e centro de massa) em um único só objeto.

        """
        self.parts = {RocketParts.PARACHUTE: None, RocketParts.NOSE: None, RocketParts.CYLINDRICAL_BODY: [], RocketParts.TRANSITION: [],
                      RocketParts.FIN: None, RocketParts.MOTOR: None}

        self.rocket_height: Vector = Vector(0, 0, 0)
        self.drag_coefficient = self.__calculateDragCoefficient()
        self.transversal_area = self.__calculateTransversalArea()

        super().__init__(RocketParts.ROCKET, -1, None, self.drag_coefficient, self.transversal_area)
        self.__verify()
        self.__movePartsToPositions()

    def __verify(self):  # fazer
        """ Verifica se os valores dos campos são coerentes. Não implementado.
        """
        pass

    def __calculateDragCoefficient(self):  # fazer
        """ Calcula o coeficiente de arrasto do foguete, atualmente esse trabalho está sendo feito em
        drag_force.py
        """
        pass

    def __calculateTransversalArea(self):  # fazer
        """ Escolhe um componente para ser a área transversal do foguete (tambem chamada de área de referência). que é
        utilizada nas forças aerodinâmicas. Atualmente esse trabalho está sendo feito nos arquivos das forças
        aerodinâmicas.
        """
        pass

    def __getMaximumPositionOrder(self):
        """Retorna a maior position order das peças disponíveis.

        Returns:
             (int): position order máxima
        """
        position_orders = [part.position_order for part in self.__getAvailableParts()]
        if len(position_orders) == 0:
            return 0
        return max(position_orders)

    def __orderAvailablePartsByPosition(self) -> List[AbstractModel]:
        """Ordena as partes em uma lista de acordo com sua position order. O algoritmo suporta "furos" nas position order's
        como por exemplo em (1,2,4,5), essa funcionalidade deve ser repensada ao se fazer a UI.

        Returns:
            List[AbstractModel]: Partes ordenadas por position order.
        """
        ordered_parts = []
        max_position_order = self.__getMaximumPositionOrder() # para que toda as partes sejam percorridas.
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

            if i < max_position_order: # certifica que toda a lista de partes é percorrida
                continue

            i_found = [found == False for found in i_found]  # inverte os bools para usar o all() do jeito certo
            if all(i_found):  # para se todas as peças já foram ordenadas
                break
        return ordered_parts

    def getPartWithPositionOrder(self, position_order) -> AbstractModel:
        """ Retorna uma parte baseado na position_order dada como argumento.

        Args:
            position_order(int): Position order da parte buscada.

        Returns:
            (AbstractModel): Parte com position order especificada.

        Raises:
            ValueError: Caso não tenha parte com a position order fornecida.
        """
        for part in self.__getAvailableParts():
            if part.position_order == position_order:
                return part

    def __getPreviousPart(self, part) -> AbstractModel:
        """Retorna a parte anterior (parte com position order diretamente anterior) em relação a parte do parâmetro.
        O algoritmo suporta "furos" nas position order's como por exemplo em (1,2,4,5), essa funcionalidade deve ser
        repensada ao se fazer a UI.

        Args:
            part(AbstractModel): Parte no qual se quer pegar a anterior.

        Returns:
            (AbstractModel): Parte com position order diretamente menor.
        """
        position_order = part.position_order
        previous_position_order = position_order - 1

        while previous_position_order >= 0: # vai até a primeira parte
            previous_part = self.getPartWithPositionOrder(previous_position_order)
            if previous_part is not None: # parte encontrada
                return previous_part

            previous_position_order -= 1

    def __putRocketOnGround(self):
        """Coloca o foguete no chão (x,y,0).
        """
        for part in self.__getAvailableParts():
            part.move(self.rocket_height)

    def __movePartsToPositions(self):
        """Ordenada as partes disponíveis no ESPAÇO começando pela parte de menor position order. Elas são movidas cada
        vez mais para baixo (z<0) e a altura do foguete é recalculada iterativamente, no final o foguete é posto no chão
        (tirando ele da zona negativa de z) com o método __putRocketOnGround().
        """
        ordered_parts = self.__orderAvailablePartsByPosition()
        self.rocket_height = Vector(0, 0, 0)
        for part in ordered_parts:
            part.centerOnOrigin()
            displacement = part.getTipDistanceToCg().magnitude() * -1  # move (para baixo) a própria altura acima do cg
            displacement = Vector(0, 0, displacement)

            previous_part = self.__getPreviousPart(part)
            if previous_part is None:  # primeira parte
                self.rocket_height = Vector(0, 0, part.height)

            if previous_part is not None:  # não é a primeira parte
                current_part_height = Vector(0, 0, part.height)
                self.rocket_height += current_part_height

                displacement -= (self.rocket_height - current_part_height)  # move (para baixo) a altura das peças anteriores

            part.move(displacement) # move o total acumulado em displacement

            if part.part_type == RocketParts.FIN:
                part: FinModel = part  # só para tirar o erro do INTELLIJ
                displacement = Vector(0, 0, part.root_chord + part.distance_to_base)
                part.move(displacement)

                # distance_from_center = Vector(part.distance_from_center, 0, 0)
                fin_index = -2
                for degrees in range(0, 361, 360 // part.nb_fins):  # rotaciona as aletas no espaço (TESTAR)
                    fin_index += 1
                    if degrees == 0:
                        continue

                    radians = degrees / 180
                    radians *= Constants.PI.value
                    z_axis = Vector(0, 0, 1)
                    # displacement = Vector.rotateAroundAxis(distance_from_center, z_axis, radians)
                    part.fin_rotation_vectors[fin_index] = Vector.rotateAroundAxis(part.fin_rotation_vectors[fin_index], z_axis, radians)
                    # part.move(displacement, ignore_ground=True)

        self.__putRocketOnGround() # foguete é movido para cima, saindo da região negativa de z e começando na origem.

    def __getAvailableParts(self) -> List[AbstractModel]:
        """Retorna as partes disponíveis atualmente no foguete. As partes que podem ser multiplas (corpos cilindricos e
        transições) são retirados de suas listas e colocados na lista que será retornada.

        Returns:
            List[AbstractModel]: Lista 1D com todas as partes disponíveis.
        """
        available_parts = []
        for key, value in self.parts.items():
            if value is None:
                continue

            if type(value) == list: # corpo cilindrico ou transição
                for part in value: # retira essas peças de suas listas e adiciona a uma só lista final
                    available_parts.append(part)
                continue

            available_parts.append(value)

        return available_parts

    def updateState(self) -> None:
        """Atualiza o estado estrutural do foguete e de suas peças, algumas atualizações como volume total e area
        molhada talvez não sejam necessárias de serem feitas pois não mudam (verificar se impacta muito a performance).
        """
        super().updateState() # atualiza o estado estrutural do foguete como um só corpo

        for part in self.__getAvailableParts(): # atualiza o estado estrutural de cada uma das peças (necessário).
            part.updateState()

    def calculateVolume(self) -> float:
        """Calcula o volume total do foguete.

        Returns:
            (float): Volume total do foguete.
        """
        available_parts = self.__getAvailableParts()
        total_volume = 0

        for part in available_parts:
            total_volume += part.volume

        return total_volume

    def calculateMass(self) -> float:
        """Calcula a massa total do foguete.

        Returns:
            (float): Massa total do foguete.
        """
        available_parts = self.__getAvailableParts()
        total_mass = 0

        for part in available_parts:
            total_mass += part.mass

        return total_mass

    def calculateMomentOfInertia(self, axis_offset_to_cg: float) -> float:  # axis_offset_to_cg pode ser negativo
        """Calcula o momento de inércia do foguete em relação a um eixo.

        Args:
            axis_offset_to_cg(float): Eixo de referência para o cálculo do momento de inércia.

        Returns:
            (float): Momento de inércia.
        """
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
        """Calcula a posição (em relação a origem 0,0,0) do cg do foguete.

        Returns:
            (Vector): Posição do cg do foguete.
        """
        total_mass = 0
        cg = Vector(0, 0, 0)
        available_parts = self.__getAvailableParts()

        if len(available_parts) == 0:
            return

        for part in available_parts:
            total_mass += part.mass
            cg += part.cg * part.mass

        if total_mass == 0:
            cg = 0
        else:
            cg = cg * (1 / total_mass)
        return cg

    def calculateCp(self) -> Vector:
        """Calcula a posição (em relação a origem 0,0,0) do cp do foguete.

        Returns:
            (Vector): Posição do cp do foguete.
        """
        total_shape_coefficient = 0
        cp = Vector(0, 0, 0)
        available_parts = self.__getAvailableParts()

        if len(available_parts) == 0:
            return

        for part in available_parts:
            if part.part_type == RocketParts.PARACHUTE and part.inflated is False:
                continue # só conta a contribuição (enorme) do paraquedas quando inflado

            cp += part.cp * part.shape_coefficient
            total_shape_coefficient += part.shape_coefficient

        if total_shape_coefficient == 0:
            cp = 0
        else:
            cp = cp * (1 / total_shape_coefficient)
        return cp

    def createDelimitationPoints(self) -> List[Vector]:
        """Seta os pontos de delimitação. O superior é o superior da primeira peça (em termos de position order)
        e o inferior é o inferior da ultima peça.

        Returns:
            List[Vector]: Pontos de delimitação do foguete.
        """
        ordered_parts = self.__orderAvailablePartsByPosition()
        if len(ordered_parts) == 0:
            return [Vector(0, 0, 0), Vector(0, 0, 0)]

        first_part: AbstractModel = ordered_parts[0]
        last_part: AbstractModel = ordered_parts[-1]

        delimitation_points = [first_part.delimitation_points[0], last_part.delimitation_points[1]]
        return delimitation_points

    def calculateWetArea(self) -> float:
        """Calcula a área molhada do foguete.

        Returns:
            (float): Área molhada do foguete.
        """
        available_parts = self.__getAvailableParts()
        total_wet_area = 0
        for part in available_parts:
            total_wet_area += part.wet_area

        return total_wet_area

    def addPart(self, part: AbstractModel):  # adiciona instâncias
        """Adiciona novas peças ao foguete. Adiciona peças por INSTÂNCIA, ou seja, se duas instâncias diferentes de uma
         com características iguais e
        """
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
        parts = []
        for part in self.__getAvailableParts():
            if part.part_type == part_type:
                if part_type == RocketParts.CYLINDRICAL_BODY or part_type == RocketParts.TRANSITION:
                    parts.append(part)
                    continue

                return part

        if len(parts) != 0:
            return parts

        # print(f"Part type {part_type.value} doesnt exist")

    def getParts(self) -> List[AbstractModel]:
        return self.__getAvailableParts()

    def move(self, displacement: Vector):
        super().move(displacement)

        for part in self.__getAvailableParts():
            part.move(displacement)

    def rotate(self, angular_displacement: Vector, axis_displacement: Vector = Vector(0, 0, 0)):
        super().rotate(angular_displacement)

        for part in self.__getAvailableParts():
            axis_displacement = part.cg - self.cg
            part.rotate(angular_displacement, axis_displacement=axis_displacement)
