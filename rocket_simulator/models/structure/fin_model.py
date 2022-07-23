from cmath import pi
from utils.rocket_parts import RocketParts
from math import tan
from core.physics.vector import Vector
from core.physics.body.rigid_body import RigidBody
from models.other.material_model import MaterialModel
from models.structure.abstract_model import AbstractModel


class FinModel(AbstractModel):
    def __init__(self, root_chord, tip_chord, span, max_thickness, sweep_angle, material: MaterialModel,
                 position_order: int, distance_to_base, distance_from_cylinder_center, nb_fins:int):
        self.root_chord = root_chord
        self.tip_chord = tip_chord
        self.span = span
        self.max_thickness = max_thickness
        self.sweep_angle = sweep_angle
        self.distance_to_base = distance_to_base
        self.distance_from_cylinder_center = distance_from_cylinder_center
        self.nb_fins = nb_fins
        self.material = material
        self.drag_coefficient = self.__calculateDragCoefficient()
        self.transversal_area = self.__calculateTransversalArea()
        
        super().__init__(RocketParts.FIN, position_order, self.drag_coefficient, self.transversal_area)
        self.__verify()

    def __verify(self): 
        if self.max_thickness<0:
            raise ValueError("Impossible negative fin values")
        elif self.sweep_angle<0 or self.sweep_angle>pi/2:
            raise ValueError("Invalid sweep angle for fins")
        else:
            pass

    def __calculateDragCoefficient(self): # fazer
        pass
    
    def __calculateTransversalArea(self): # fazer
        pass

    def getDistanceToBase(self) -> float:
        return self.distance_to_base

    def getDistanceFromCenter(self) -> float:
        return self.distance_from_cylinder_center

    def getNumberOfFins(self) -> int:
        return self.nb_fins

    def calculateVolume(self) -> float:
        area = (self.span * (self.tip_chord + self.root_chord)) / 2
        volume = area * self.max_thickness
        return volume

    def calculateMass(self) -> float:
        mass = self.material.density * self.calculateVolume
        return mass

    def calculateCp(self) -> Vector: # Source: document rocket model pdf
        m = self.span*tan(self.sweep_angle)

        cp_local = self.getTipToBaseDistance().unitVector * ( m*(self.root_chord + 2*self.tip_chord)/(3*(self.root_chord + self.tip_chord)) +
            1/6*(self.root_chord + self.tip_chord - self.root_chord*self.tip_chord/( self.root_chord + self.tip_chord) ))
        
        return self.toGroundCoordinates(cp_local)

    def calculateCg(self) -> Vector: # source: https://www.efunda.com/math/areas/trapezoid.cfm 
        m = self.span*tan(self.sweep_angle)

        cg_local = self.getTipToBaseDistance().unitVector*((2*self.tip_chord*m + self.tip_chord^2 +m*self.root_chord +
            self.root_chord*self.tip_chord + self.root_chord^2)/(3*(self.root_chord+self.tip_chord)) )
        return self.toGroundCoordinates(cg_local)

    def calculateMomentOfInertia(self) -> float: # source: https://www.efunda.com/math/areas/trapezoid.cfm 
        m = self.span*tan(self.sweep_angle)
        inertia_yc= self.span*(4*self.tip_chord*self.root_chord*m^2 + 3*self.tip_chord^2*self.root_chord*m - 3*self.tip_chord*self.root_chord^2*m +
            self.tip_chord^4 + self.root_chord^4 + 2*self.tip_chord^3*self.root_chord + self.tip_chord^2*m^2 + self.tip_chord^3*m +2*self.tip_chord*
            self.root_chord^3-m*self.root_chord^3 + self.root_chord^2*m^2)/(36*(self.root_chord+self.tip_chord))
        return inertia_yc