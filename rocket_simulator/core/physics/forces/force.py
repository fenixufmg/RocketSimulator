from core.physics.body.application_point import ApplicationPoint
from core.physics.delta_time_simulation import DeltaTimeSimulation
from core.physics.vector import Vector
from abc import ABC, abstractmethod


class Force(Vector, ABC):
    def __init__(self, x: float, y: float, z: float, application_point: ApplicationPoint, cg_offset: float = None):
        """Classe que representa uma força física.

        Args:
            x (float): Valor no eixo x.
            y (float): Valor no eixo y.
            z (float): Valor no eixo z.
            application_point (ApplicationPoint): Ponto de aplicação da força.
            cg_offset (float): Parâmetro opcional que indica a distância do ponto de aplicação para o CG. Se positivo
            o ponto está acima do CG, se negativo o ponto está abaixo do CG.

        Fields:
            __application_point (ApplicationPoint): Ponto de aplicação da força.
            __cg_offset (float): Distância entre o ponto de aplicação e o CG.
        """
        super().__init__(x, y, z)
        self.application_point = application_point
        self.cg_offset = cg_offset  # valores positivos -> acima do cg, valores negativos -> abaixo do cg
        self.__validate()

    def __validate(self) -> None:
        """Verifica se um cg_offset foi dado se o ponto de aplicação for custom.

        Raises:
            ValueError: Levantado se houver uma combinação errada entre pontos de aplicação e cg_offset.
        """
        if self.application_point == ApplicationPoint.CUSTOM:  # ponto de aplicação custom
            if self.cg_offset is None:  # cg_offset não foi definido
                raise ValueError("No cg_offset given to custom application point")
        else:  # Ponto de aplicação CG ou CP.
            if self.cg_offset is not None:  # cg_offset dado para ponto de aplicação CG ou CP (errado)
                raise ValueError("cg_offset is not defined for this application point")

    @abstractmethod
    def calculate(self, current_state: DeltaTimeSimulation) -> None:
        """Método abstrato que representa como o cálculo da força deve ser feito para cada instante de
        tempo (para cada estado do corpo).

        Raises:
            NotImplementedError: Levantado se essa função não for implementada em uma classe que a estende.
        """
        raise NotImplementedError("Function not implemented")
