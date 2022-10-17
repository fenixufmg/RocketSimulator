from typing import List

from core.physics.forces.impulse_test_force import ImpulseTestForce
from core.physics.forces.thrust import Thrust
from utils.rocket_parts import RocketParts
from math import pi
from core.physics.vector import Vector
from models.other.material_model import MaterialModel
from models.structure.abstract_model import AbstractModel


class MotorModel(AbstractModel):
    def __init__(self, height, diameter, thickness, material: MaterialModel, position_order: int):
        # adicionar propellant model aos parametros
        """ Peça que representa o motor do foguete. E responsável por dar o empuxo.

        Args:
            height (float): Altura do motor.
            diameter (float): Diametro do motor.
            thickness (float): Espessura do motor.
        """
        self.height = height
        self.diameter = diameter  # Outer diameter
        self.thickness = thickness
        self.material = material
        self.drag_coefficient = self.__calculateDragCoefficient()
        self.transversal_area = self.__calculateTransversalArea()

        # self.thrust = Thrust(propellant_model)
        self.thrust = ImpulseTestForce(400) # provisório até implementar o thrust


        super().__init__(RocketParts.MOTOR, position_order, 0, self.drag_coefficient, self.transversal_area)
        self.__verify(diameter, thickness)

    def __verify(self, diameter, thickness):
        """Verifica se os campos indicados pelo usuário são possíveis (incompleto).

            Raises:
                ValueError: Algum campo é incoerente.
        """
        if thickness >= diameter / 2:
            raise ValueError("Value of thickness is bigger than half of outer diameter")

    def __calculateDragCoefficient(self) -> float: # fazer
        """Calcula o coeficiente de arrasto.

        Returns:
            (float): Coeficiente de arrasto.
        """
        pass

    def __calculateTransversalArea(self) -> float: # fazer
        """Calcula a área transversal no instante T-0.

        Returns:
            (float): Área transversal.
        """
        pass

    def calculateVolume(self) -> float:
        inner_diameter = self.diameter - 2 * self.thickness
        volume = pi * self.height * ((self.diameter / 2) ** 2 - (inner_diameter / 2) ** 2)
        return volume

    def calculateMass(self) -> float:
        mass = self.material.density * self.volume
        return mass

    def calculateMomentOfInertia(self, distance_to_cg: float) -> float: # https://en.wikipedia.org/wiki/List_of_moments_of_inertia
        mass = self.calculateMass()
        Ixx = 1/12*mass*(3*( (self.diameter**2)/4 +((self.diameter-2*self.thickness)**2)/4 )+self.height**2)
        return Ixx + self.mass * distance_to_cg**2

    def calculateCg(self) -> Vector:  # Feito amigo
        # Primeiro pega o vetor de altura da peça, a sua direção varia com a orientação do foguete, mas o módulo é
        # constante. getTipToBaseDistance() retorna o vetor que sai da ponta superior e vai até à ponta inferior
        height = self.getTipToBaseDistance()
        cg_local = height * 0.5  # produto por escalar
        return self.toGroundCoordinates(cg_local)

    def calculateCp(self) -> Vector: # CONFERIR DEPOIS
        height = self.getTipToBaseDistance()
        cg_local = height * 0.5
        cp_local = cg_local # Assuming same position as cp
        return self.toGroundCoordinates(cp_local)

    def createDelimitationPoints(self) -> List[Vector]:
        upper_delimitation = Vector(0, 0, self.height)
        lower_delimitation = Vector(0, 0, 0)
        return [upper_delimitation, lower_delimitation]

    def calculateWetArea(self) -> float:
        wet_area = pi*self.diameter*self.height
        return wet_area
