from cmath import cos, pi
from utils.rocket_parts import RocketParts
from math import atan, tan, sqrt
from core.physics.vector import Vector
from core.physics.body.rigid_body import RigidBody
from models.other.material_model import MaterialModel
from models.structure.abstract_model import AbstractModel


class FinModel(AbstractModel):
    def __init__(self, root_chord:float, tip_chord:float, span:float, max_thickness:float, sweep_angle:float, 
    distance_to_base:float, distance_from_cylinder_center:float, nb_fins:int, material: MaterialModel,
                 position_order: int):

        """ Peça que representa as aletas.

        Args:
            root_chord (float): Tamanho da root chord.
            tip_chord (float): Tamanho da root chord.
            span (float): Tamanho do span.
            max_thickness (float): Espessura maxima.
            sweep_angle (float): Sweep angle.
            distance_to_base (float): Distância até a base do foguete.
            distance_from_cylinder_center (float): Distância desde o centro do foguete.
            nb_fins (int): Número de aletas.
        """

        self.root_chord = root_chord
        self.tip_chord = tip_chord
        self.span = span
        self.max_thickness = max_thickness
        self.sweep_angle = sweep_angle
        self.distance_to_base = distance_to_base
        self.distance_from_center = distance_from_cylinder_center
        self.nb_fins = nb_fins
        self.material = material
        self.drag_coefficient = self.__calculateDragCoefficient()
        self.transversal_area = self.__calculateTransversalArea()
        self.height = 0
        self.fin_rotation_vectors = [Vector(distance_from_cylinder_center, 0, 0) for i in range(nb_fins)]
        
        super().__init__(RocketParts.FIN, position_order, self.__calculateShapeCoefficient() , self.drag_coefficient, self.transversal_area)
        self.__verify()

    def __verify(self):
        if self.max_thickness<0:
            """Verifica se os campos indicados pelo usuário são possíveis (incompleto).
    
            Raises:
                ValueError: Algum campo é incoerente.
            """
            raise ValueError("Impossible negative fin values")
        elif self.sweep_angle<0 or self.sweep_angle>pi/2:
            raise ValueError("Invalid sweep angle for fins")
        else:
            pass

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

    def __calculateShapeCoefficient(self):
        m = self.span*tan(self.sweep_angle)
        l = sqrt( (self.root_chord/2-(self.tip_chord/2+m))**2 + (self.span)**2)
        cn_alpha_Force = (4*self.nb_fins*(self.span/self.distance_from_center)**2)/( 1+sqrt(1+(2*l/(self.root_chord+self.tip_chord))**2) )
        return cn_alpha_Force

    def calculateVolume(self) -> float:
        area = (self.span * (self.tip_chord + self.root_chord)) / 2
        volume = area * self.max_thickness
        return volume

    def calculateMass(self) -> float:
        mass = self.material.density * self.calculateVolume()
        return mass

    def calculateCp(self) -> Vector: # Source: document rocket model pdf
        m = self.span*tan(self.sweep_angle)

        cp_local = self.getTipToBaseDistance().unitVector() * ( m*(self.root_chord + 2*self.tip_chord)/(3*(self.root_chord + self.tip_chord)) +
            1/6*(self.root_chord + self.tip_chord - self.root_chord*self.tip_chord/( self.root_chord + self.tip_chord) ))
        
        return self.toGroundCoordinates(cp_local)

    def calculateCg(self) -> Vector: # source: https://www.efunda.com/math/areas/trapezoid.cfm 
        m = self.span*tan(self.sweep_angle)

        cg_local = self.getTipToBaseDistance().unitVector()*((2*self.tip_chord*m + self.tip_chord**2 +m*self.root_chord +
            self.root_chord*self.tip_chord + self.root_chord**2)/(3*(self.root_chord+self.tip_chord)) )
        return self.toGroundCoordinates(cg_local)

    def calculateMomentOfInertia(self, distance_to_cg:float) -> float: # source: https://www.efunda.com/math/areas/trapezoid.cfm 
        m = self.span*tan(self.sweep_angle)
        inertia_yc= self.span*(4*self.tip_chord*self.root_chord*m**2 + 3*self.tip_chord**2*self.root_chord*m - 3*self.tip_chord*self.root_chord**2*m +
            self.tip_chord**4 + self.root_chord**4 + 2*self.tip_chord**3*self.root_chord + self.tip_chord**2*m**2 + self.tip_chord**3*m +2*self.tip_chord*
            self.root_chord**3-m*self.root_chord**3 + self.root_chord**2*m**2)/(36*(self.root_chord+self.tip_chord))
        return inertia_yc + self.mass * distance_to_cg**2

    def createDelimitationPoints(self):
        upper_delimitation = Vector(0, 0, self.root_chord)
        lower_delimitation = Vector(0, 0, 0)
        return [upper_delimitation, lower_delimitation]

    def calculateWetArea(self) -> float:
        m = self.span*tan(self.sweep_angle)
        faces_area = self.span*(self.root_chord+ self.tip_chord) # front and backside areas
        top_area = self.span*(self.span/cos(self.sweep_angle))
        side_area = self.span*self.tip_chord
        bottom_angle = atan(abs((self.root_chord - (m+self.tip_chord))/self.span))
        bottom_area = self.span*(self.span/cos(bottom_angle))
        sum_wet_area = faces_area + top_area + side_area + bottom_area
        return sum_wet_area