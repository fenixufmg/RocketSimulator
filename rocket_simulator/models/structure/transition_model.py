from utils.rocket_parts import RocketParts
from math import pi,sqrt
from core.physics.vector import Vector
from models.other.material_model import MaterialModel
from core.physics.body.rigid_body import RigidBody
from models.structure.abstract_model import AbstractModel
from typing import List


class TransitionModel(AbstractModel):
    def __init__(self, height, bottom_diameter, top_diameter, thickness, nose_diameter, material: MaterialModel, position_order: int):
        """ Classe que representa uma transição (peça).

        Args:
            height (float): Altura da transição.
            bottom_diameter (float): Diametro inferior da transição.
            top_diameter (float): Diametro superior da transição.
            thickness (float): Espessura da transição.
            nose_diameter (float): Diâmetro do nariz do foguete, idealmente esse parametro não existiria.

        """
        self.height = height
        self.bottom_diameter = bottom_diameter
        self.top_diameter = top_diameter
        self.thickness = thickness
        self.material = material
        self.drag_coefficient = self.__calculateDragCoefficient()
        self.transversal_area = self.__calculateTransversalArea()
        self.nose_diameter = nose_diameter

        super().__init__(RocketParts.TRANSITION, position_order, self.__calculateShapeCoefficient(), self.drag_coefficient, self.transversal_area)
        self.__verify()

    def __verify(self):
        """Verifica se os campos indicados pelo usuário são possíveis (incompleto).

            Raises:
                ValueError: Algum campo é incoerente.
        """
        if self.bottom_diameter < self.top_diameter:  # bottom part is thinner
            if self.thickness >= self.bottom_diameter / 2:
                raise ValueError("Value of thickness is bigger than half of bottom outer diameter")
        else:
            if self.thickness >= self.top_diameter / 2:
                raise ValueError("Value of thickness is bigger than half of top outer diameter")

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

    def __calculateShapeCoefficient(self) -> float:
        c_N_alpha_cb = 2*((self.bottom_diameter/self.nose_diameter)**2-(self.top_diameter/self.bottom_diameter)**2)
        return c_N_alpha_cb

    def calculateVolume(self) -> float:
        top_inner_diameter = self.top_diameter - 2 * self.thickness
        bottom_inner_diameter = self.bottom_diameter - 2 * self.thickness

        outer_trunk_volume = (pi / 3) * self.height * (
                    self.bottom_diameter ** 2 + self.bottom_diameter * self.top_diameter + self.top_diameter ** 2)
        inner_trunk_volume = (pi / 3) * self.height * (
                    bottom_inner_diameter ** 2 + bottom_inner_diameter * top_inner_diameter + top_inner_diameter ** 2)

        total_volume = outer_trunk_volume - inner_trunk_volume
        return total_volume

    def calculateMass(self) -> float:
        mass = self.material.density * self.calculateVolume()
        return mass

    def calculateMomentOfInertia(self, distance_to_cg: float) -> float: # https://media.cheggcdn.com/media/51d/51d19df6-2a92-4a5f-bdb2-275f8c7d8f0c/php43DZ1T.png based on last example
        if self.top_diameter == self.bottom_diameter: # momento de inercia de cilindro
            mass = self.calculateMass()
            Ixx = 1/12*mass*(3*( (self.top_diameter**2)/4 +((self.top_diameter-2*self.thickness)**2)/4 )+self.height**2)
            return Ixx + self.mass * distance_to_cg**2

        # from https://en.wikipedia.org/wiki/List_of_moments_of_inertia and parallel axis theorem
        top_inner_radius = (self.top_diameter - 2 * self.thickness)/2
        bottom_inner_radius = (self.bottom_diameter - 2 * self.thickness)/2
        bottom_radius = self.bottom_diameter/2
        top_radius = self.top_diameter/2
        Iyy = 3*self.calculateMass()*((bottom_radius**5+bottom_inner_radius**5)-(top_radius**5+top_inner_radius**5))/(
            20*((bottom_radius**3+bottom_inner_radius**3)-(top_radius**3+top_inner_radius**3)))
        return Iyy + self.mass * distance_to_cg**2

    def calculateCg(self) -> Vector:  # aproximando por um tronco cheio https://www.passeidireto.com/pergunta/17392987/como-achar-um-centro-de-gravidade-em-um-tronco-de-cone 

        bottom_radius = self.bottom_diameter/2
        top_radius = self.top_diameter/2

        if self.bottom_diameter < self.top_diameter:  # bottom part is thinner
            cg_local = self.height -self.height/4*((top_radius**2 +2*top_radius*bottom_radius + 3*bottom_radius**2)/(
                top_radius**2 + top_radius*bottom_radius + bottom_radius**2))
            
        else:
            cg_local = self.height -self.height/4*((bottom_radius**2 +2*bottom_radius*top_radius + 3*top_radius**2)/(
                bottom_radius**2 + bottom_radius*top_radius + top_radius**2))
            
        cg = self.getTipToBaseDistance().unitVector() * cg_local

        return self.toGroundCoordinates(cg)

    def calculateCp(self) -> Vector: # Reference from donwloaded files
        if self.top_diameter != self.bottom_diameter:
            Cp = self.getTipToBaseDistance() * (1/3)*(1 + (1-self.top_diameter/self.bottom_diameter)/(1-(self.top_diameter/self.bottom_diameter)**2))
            return self.toGroundCoordinates(Cp)
        else:
            Cp = self.getTipToBaseDistance()*0.5
            return self.toGroundCoordinates(Cp)

    def createDelimitationPoints(self) -> List[Vector]:
        upper_delimitation = Vector(0, 0, self.height)
        lower_delimitation = Vector(0, 0, 0)
        return [upper_delimitation, lower_delimitation]

    def calculateWetArea(self) -> float: # Reference from https://brasilescola.uol.com.br/matematica/tronco-cone.htm 
        g = sqrt(self.height**2 + (self.top_diameter-self.bottom_diameter)**2) 
        wet_area = pi*g*(self.top_diameter+self.bottom_diameter)
        return wet_area

