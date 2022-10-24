from abc import ABC, abstractmethod
from posixpath import abspath
from typing import List
from core.physics.body.rigid_body import RigidBody
from core.physics.vector import Vector
from utils.rocket_parts import RocketParts

class AbstractModel(ABC, RigidBody):
    def __init__(self, part_type: RocketParts, position_order: int, shape_coefficient:float, 
                drag_coefficient:float, transversal_area:float) -> None:
        """Classe abstrata que representa oque todas as peças tem que ter e tudo que elas devem fazer (no geral).
        Todas as peças são representadas no espaço como o conjunto de 4 vetores (pontos): Cg, Cp, delimitação superior
        e delimitação inferior. Os ultimos dois são os pontos extremos da parte, servem para se saber onde cada
        componente começa e termina.

        Args:
            part_type (RocketParts): Categoria da classe (nariz, motor, aleta, etc...).

            position_order (int): Número que representa a posição relativa da peça, o menor número será a primeira peça
            (de cima para baixo) e o maior será a última (que está na base do foguete).

            shape_coefficient (float): Coeficiente usado nos cálculos aerodinâmicos.

            drag_coefficient (float): Coeficiente de arrasto, no momento todos os coeficientes de arrasto de todas as
            peças estão sendo calculados em drag_force.py, mudar para que cada peça consiga calcular separadamente
            seu próprio coeficiente.

            transversal_area (float): área transversal no instante T-0 (antes do lançamento).

        Fields:
            part_type (RocketParts): Categoria da classe (nariz, motor, aleta, etc...).

            position_order (int): Número que representa a posição relativa da peça, o menor número será a primeira peça
            (de cima para baixo) e o maior será a última (que está na base do foguete).

            shape_coefficient (float): Coeficiente usado nos cálculos aerodinâmicos.

            drag_coefficient (float): Coeficiente de arrasto, no momento todos os coeficientes de arrasto de todas as
            peças estão sendo calculados em drag_force.py, mudar para que cada peça consiga calcular separadamente
            seu próprio coeficiente.

            transversal_area (float): área transversal no instante T-0 (antes do lançamento).

            wet_area (float): área molhada da peça.

        """
        # rocket specific
        self.part_type = part_type
        self.position_order = position_order
        self.shape_coefficient = shape_coefficient
        self.drag_coefficient = drag_coefficient
        self.transversal_area = transversal_area  

        # rigid body fields
        self.delimitation_points = self.createDelimitationPoints()
        volume = self.calculateVolume()
        self.volume = volume
        self.wet_area = self.calculateWetArea()
        mass = self.calculateMass()
        moment_of_inertia_function = self.calculateMomentOfInertia
        cg = self.calculateCg()
        cp = self.calculateCp()
        super().__init__(self.delimitation_points, mass, volume, moment_of_inertia_function, cg, cp)
    
    @abstractmethod
    def calculateVolume(self) -> float:
        """Calcula o volume da peça. Não muda durante o voo.

        Returns:
            (float): Volume da peça.
        """
        raise NotImplementedError("Function not implemented")

    @abstractmethod
    def calculateMass(self) -> float:
        """Calcula a massa da peça. Muda durante o voo.

        Returns:
            (float): Massa da peça.
        """
        raise NotImplementedError("Function not implemented")

    @abstractmethod
    def calculateMomentOfInertia(self, distance_to_cg:float) -> float:
        """Calcula o momento de inércia a uma certa distância do cg. Forma de calcular não muda durante o voo.

        Returns:
            (float): Momento de inércia.
        """
        raise NotImplementedError("Function not implemented")

    @abstractmethod
    def calculateCg(self) -> Vector:
        """Calcula a posição do cg. Posição em relação ao foguete pode variar durante o voo.

        Returns:
            (Vector): Posição do cg.
        """
        raise NotImplementedError("Function not implemented")

    @abstractmethod
    def calculateCp(self) -> Vector: # http://ftp.demec.ufpr.br/foguete/bibliografia/TIR-33%20Calculating%20the%20Center%20of%20Pressure%20of%20a%20Model%20Rocket.pdf
        """Calcula a posição do cp. Posição em relação ao foguete pode variar durante o voo.

        Returns:
            (vector): Posição do cp.
        """
        raise NotImplementedError("Function not implemented")

    @abstractmethod
    def createDelimitationPoints(self) -> List[Vector]:
        """Cria os pontos de delimitação. Posição em relação ao foguete não muda durante o voo.

        Returns:
            (List[Vector]): Pontos de delimitação.
        """
        raise NotImplementedError("Function not implemented")

    @abstractmethod
    def calculateWetArea(self) -> float:
        """Calcula a área molhada. Não muda durante o voo.

        Returns:
            (float): Área molhada.
        """
        raise NotImplementedError("Function not implemented")

    def updateState(self) -> None:
        """Atualiza o estado da peça com base nas características que ela tem no momento, algumas "atualizações" podem
        não ser necessárias, pois os valores não mudam durante o voo.

        """
        self.volume = self.calculateVolume()  # potencialmente desnecessario
        self.wet_area = self.calculateWetArea()  # potencialmente desnecessario
        self.mass = self.calculateMass()  # necessario para algumas peças como o motor que mudam de massa durante o voo.
        self.moment_of_inertia = self.calculateMomentOfInertia # potencialmente desnecessario
        self.cg = self.calculateCg()  # necessário pois a massa muda
        self.cp = self.calculateCp()  # incerto.
        # self.delimitation_points = self.createDelimitationPoints() ## BUG

    def toGroundCoordinates(self, local_coordinates:Vector) -> Vector:
        """Transforma as coordenadas relativas ao corpo (origem na delimitação superior e positivo na direção da
        delimitação inferior) para as coordenadas relativas ao solo. Esse método é sempre chamado no final dos cálculos
        de cg e cp, menos em rocket_model.py, pois lá as coordenadas das peças já estão em relação ao solo.

        Args:
            local_coordinates (Vector): Coordenadas relativas ao corpo.

        Returns:
            (vector): Coordenadas relativas ao solo.
        """
        return self.getTip() + local_coordinates

    def getPosition(self) -> List[List]:
        """Retorna uma lista 2D com as coordenadas das limitações superiores e inferiores.

        Returns:
            (List[List]): Lista 2D com as delimitações.
        """
        position = [self.delimitation_points[0].toList(), self.cg.toList(), self.delimitation_points[1].toList()]
        return position

