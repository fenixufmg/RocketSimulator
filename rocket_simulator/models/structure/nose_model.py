from utils.nose_type import NoseType
from utils.rocket_parts import RocketParts
from email.mime import base
from enum import Enum

from core.physics.body.rigid_body import RigidBody
from models.other.material_model import MaterialModel
from models.structure.abstract_model import AbstractModel
from core.physics.vector import Vector
from utils.constants import Constants



class NoseModel(AbstractModel):
    def __init__(self, base_diameter:float, thickness:float, nose_type:NoseType, thinness_factor:float, cylinder_height:float, material:MaterialModel, position_order: int):
        """ Classe que representa o nariz do foguete.

        Args:
            base_diameter (float): Diãmetro da base.
            thickness (float): Espessura.
            nose_type (NoseType): Tipo do nariz.
            thinness_factor (float): fator de 'magreza' do nariz.
            cylinder_height (float): Altura do cilindro do nariz.

        """
        self.base_diameter = base_diameter
        self.base_radius = base_diameter / 2
        self.thinness_factor = thinness_factor

        self.cylinder_height = cylinder_height # altura da parte cilindrica do nariz.
        self.height = cylinder_height + thinness_factor*self.base_radius**2  # altura da parte parabolica do nariz
        self.paraboloid_height = self.height - self.cylinder_height

        self.thickness = thickness # implementar nariz oco
        self.nose_type = nose_type
        self.material = material
        self.drag_coefficient = self.__calculateDragCoefficient()
        self.transversal_area = self.__calculateTransversalArea()

        super().__init__(RocketParts.NOSE, position_order, 2, self.drag_coefficient, self.transversal_area)
        self.__verify()

    def __verify(self):
        """Verifica se os campos indicados pelo usuário são possíveis (incompleto).

            Raises:
                ValueError: Algum campo é incoerente.
        """
        if self.base_diameter <= 0:
            raise ValueError("Base diameter <= 0 not allowed")
        if self.thickness <= 0:
            raise ValueError("Thickness <= 0 not allowed")
        if self.thickness > self.base_radius:
            raise ValueError("Thickness greater than radius")
        if self.thinness_factor <= 0:
            raise ValueError("Thinness factor <= 0 not allowed")

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

    def calculateVolume(self) -> float: # https://www.grc.nasa.gov/www/k-12/airplane/volume.html
        if self.nose_type == NoseType.CONICAL:
            return (Constants.PI.value * self.base_diameter**2 * self.height) / (12)

        elif self.nose_type == NoseType.OGIVE:
            # return (2 * Constants.PI * self.base_diameter**2 * self.height) / (15) 
            raise ValueError(f"Nose type {self.nose_type} is not available.")

        elif self.nose_type == NoseType.PARABOLIC:
            r = self.base_radius
            pi = Constants.PI.value
            k = self.thinness_factor

            return pi*((self.cylinder_height + k*r**2)*(r**2) - (k*r**4)/2)
            
        else:
            raise ValueError(f"Nose type {self.nose_type} is not available.")

    def calculateMass(self)-> float:
        return self.volume * self.material.density

    def calculateMomentOfInertia(self, distance_to_cg:float) -> float:  # aproximação usando cone
        inertia_around_cg = self.mass * ((3*self.base_radius**2)/20 + (3*self.height**2)/80)
        return inertia_around_cg + self.mass * distance_to_cg**2

    def calculateCg(self) -> Vector: # https://en-gb.facebook.com/engineerprofph/photos/pcb.286878569591821/286874736258871/?type=3&theater
        cg = None
        if self.nose_type == NoseType.CONICAL:
            cg = self.height - self.height/4 # escalar

        elif self.nose_type == NoseType.OGIVE:
            raise ValueError(f"Nose type {self.nose_type} is not available.")

        elif self.nose_type == NoseType.PARABOLIC:
            cg = self.height - self.height/3 # escalar
        else:
            raise ValueError(f"Nose type {self.nose_type} is not available.")
        
        cg = self.getTipToBaseDistance().unitVector() * cg
        cg = self.toGroundCoordinates(cg)
        return cg
    def calculateCp(self) -> Vector:
        cp = None
        if self.nose_type == NoseType.CONICAL:
            cp = self.getTipToBaseDistance() * (2/3)

        elif self.nose_type == NoseType.OGIVE:
            cp = self.getTipToBaseDistance() * (0.466)

        elif self.nose_type == NoseType.PARABOLIC:
            cp = self.getTipToBaseDistance() * (1/2)

        else:
            raise ValueError(f"Nose type {self.nose_type} is not available.")

        return self.toGroundCoordinates(cp)

    def calculateWetArea(self) -> float: # https://mathworld.wolfram.com/Paraboloid.html
        a = self.base_radius
        h = self.paraboloid_height
        pi = Constants.PI.value

        paraboloid_area = (pi*a)/(6*h**2)
        paraboloid_area *= ((a**2 + 4*h**2)**1.5 - a**3)

        cylinder_area = self.cylinder_height * (2*pi*a) 
        return cylinder_area + paraboloid_area

    def createDelimitationPoints(self) -> list:
        upper_delimitation = Vector(0, 0, self.height)
        lower_delimitation = Vector(0, 0, 0)
        return [upper_delimitation, lower_delimitation]

    