from dataclasses import dataclass
from email.mime import base
from enum import Enum

from core.physics.body.rigid_body import RigidBody
from other.material_model import MaterialModel
from models.structure.abstract_model import AbstractModel
from core.physics.vector import Vector
from utils.constants import Constants

class NoseType(Enum):
    CONICAL = 1
    OGIVE = 2
    PARABOLIC = 3

class NoseModel(AbstractModel):
    def __init__(self, cylinder_height:float ,base_diameter:float, thickness:float, nose_type:NoseType, thinness_factor:float ,material:MaterialModel):
        self.__cylinder_height = cylinder_height
        self.__base_diameter = base_diameter
        self.__base_radius = base_diameter / 2
        self.__thickness = thickness # implementar nariz oco
        self.__nose_type = nose_type
        self.__thinness_factor = thinness_factor
        self.__material = material
        super().__init__()

    def calculateVolume(self) -> float: # https://www.grc.nasa.gov/www/k-12/airplane/volume.html
        if self.__nose_type == NoseType.CONICAL:
            return (Constants.PI * self.__base_diameter**2 * self.__height) / (12)

        elif self.__nose_type == NoseType.OGIVE:
            # return (2 * Constants.PI * self.__base_diameter**2 * self.__height) / (15) 
            raise ValueError(f"Nose type {self.__nose_type} is not available.")

        elif self.__nose_type == NoseType.PARABOLIC:
            h = self.__cylinder_height
            r = self.__base_radius
            pi = Constants.PI
            k = self.__thinness_factor

            return pi*((h + k*r**2)*(r**2) - (k*r**4)/2)
            
        else:
            raise ValueError(f"Nose type {self.__nose_type} is not available.")


    def calculateMass(self)-> float:
        return self.volume * self.__material.density

    def calculateMomentOfInertia(self) -> float:
        pass

    def calculateCg(self) -> Vector: # https://en-gb.facebook.com/engineerprofph/photos/pcb.286878569591821/286874736258871/?type=3&theater
        if self.__nose_type == NoseType.CONICAL:
            return self.__height - self.__height/4 

        elif self.__nose_type == NoseType.OGIVE:
            raise ValueError(f"Nose type {self.__nose_type} is not available.")

        elif self.__nose_type == NoseType.PARABOLIC:
            return self.__height - self.__height/3 
        else:
            raise ValueError(f"Nose type {self.__nose_type} is not available.")

    def calculateCp(self) -> Vector:
        cp = None
        if self.__nose_type == NoseType.CONICAL:
            cp = self.getTipToBaseDistance() * (2/3)

        elif self.__nose_type == NoseType.OGIVE:
            cp = self.getTipToBaseDistance() * (0.466)

        elif self.__nose_type == NoseType.PARABOLIC:
            cp = self.getTipToBaseDistance() * (1/2)

        else:
            raise ValueError(f"Nose type {self.__nose_type} is not available.")

        return self.toGroundCoordinates(cp)

    def createDelimitationPoints(self) -> list:
        upper_delimitation = Vector(0, 0, self.__height)
        lower_delimitation = Vector(0, 0, 0)
        return [upper_delimitation, lower_delimitation]

    