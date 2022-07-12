import cgi
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
    def __init__(self, base_diameter:float, thickness:float, nose_type:NoseType, thinness_factor:float, material:MaterialModel, position_order: int):
        self.base_diameter = base_diameter
        self.base_radius = base_diameter / 2
        self.thinness_factor = thinness_factor
        self.height = thinness_factor*self.base_radius**2
        self.thickness = thickness # implementar nariz oco
        self.nose_type = nose_type
        self.material = material
        self.drag_coefficient = self.__calculateDragCoefficient()
        self.transversal_area = self.__calculateTransversalArea()

        super().__init__(RocketParts.NOSE, position_order, 2, self.drag_coefficient, self.transversal_area)
        self.__verify()

    def __verify(self):
        if self.base_diameter <= 0:
            raise ValueError("Base diameter <= 0 not allowed")
        if self.thickness <= 0:
            raise ValueError("Thickness <= 0 not allowed")
        if self.thickness > self.base_radius:
            raise ValueError("Thickness greater than radius")
        if self.thinness_factor <= 0:
            raise ValueError("Thinness factor <= 0 not allowed")

    def __calculateDragCoefficient(self): # fazer
        pass
    
    def __calculateTransversalArea(self): # fazer
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

            return pi*((0 + k*r**2)*(r**2) - (k*r**4)/2)
            
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

    def createDelimitationPoints(self) -> list:
        upper_delimitation = Vector(0, 0, self.height)
        lower_delimitation = Vector(0, 0, 0)
        return [upper_delimitation, lower_delimitation]

    