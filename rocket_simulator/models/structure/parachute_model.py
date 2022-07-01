from typing import List
from core.physics.vector import Vector
from utils.rocket_parts import RocketParts
from utils.cable_type import CableType
from utils.parachute_type import ParachuteType
from utils.paths import Paths
from core.physics.body.rigid_body import RigidBody
from other.material_model import MaterialModel
from math import pi
from models.structure.abstract_model import AbstractModel
import json
import enum
from random import randint

class ParachuteModel(AbstractModel):
    def __init__(self, parachute_type: ParachuteType, cable_type:CableType, diameter:float, coupled_part:AbstractModel, inflation_randomness_factor: float = 1):
        self.parachute_type = parachute_type
        self.inflation_randomness_factor = inflation_randomness_factor
        self.cable_type = cable_type
        self.diameter = diameter
        self.coupled_part = coupled_part
        self.ejected = False
        self.inflated = False
        self.inflation_force = None
        self.drag_coefficient = self.__calculateDragCoefficient()
        self.transversal_area = self.__calculateTransversalArea()

        super().__init__(RocketParts.PARACHUTE, coupled_part.position_order, 0, self.drag_coefficient, self.transversal_area)
        self.__verify(diameter)

    def __verify(self, diameter:float): # fazer
        pass

    def eject(self): # concertar para ajustar o fator randomico de acordo com DELTA_TIME
        if self.inflated is True:
            return

        self.ejected = True
        
        upper_limit = 2**(self.inflation_randomness_factor * 2)
        inflation_tentative = randint(1, upper_limit)
        if inflation_tentative == 1: # success
            print("Parachute inflated")
            self.inflated = True
            self.calculateInflationForce()
    
    def calculateMaximumInflationForce(self):
        self.inflation_force = ??

    def __calculateDragCoefficient(self):
        parachute_folder = Paths.PARACHUTES.value

        parachute_file = f"{parachute_folder}/{self.parachute_type.value}.json"
        with open(parachute_file) as parachute_file:
            data = json.load(parachute_file)

            self.drag_coefficient = data["drag_coefficient"]

    def __calculateTransversalArea(self) -> float:
        return ((self.diameter/2)**2)*5.099

    def calculateVolume(self) -> float: # possivelmente errado
        inner_diameter = self.diameter - 2 * self.thickness
        volume = pi * self.height * ((self.diameter / 2) ^ 2 - (inner_diameter / 2) ^ 2)
        return volume

    def calculateMass(self) -> float: # possivelmente errado
        mass = self.material.density * self.calculateVolume
        return mass

    def calculateMomentOfInertia(self, distance_to_cg: float) -> float: # possivelmente errado
        mass = self.calculateMass
        Ixx = 1/12*mass*(3*( (self.diameter^2)/4 +((self.diameter-2*self.thickness)^2)/4 )+self.height^2)
        return Ixx

    def calculateCg(self) -> Vector: # possivelmente errado
        height = self.getTipToBaseDistance()
        cg_local = height * 0.5
        return self.toGroundCoordinates(cg_local)

    def calculateCp(self) -> Vector: # possivelmente errado
        height = self.getTipToBaseDistance()
        cg_local = height * 0.5  
        cp_local = cg_local # Assuming same position as cp
        return self.toGroundCoordinates(cp_local)

    def createDelimitationPoints(self) -> List[Vector]: # possivelmente errado
        upper_delimitation = Vector(0, 0, self.height)
        lower_delimitation = Vector(0, 0, 0)
        return [upper_delimitation, lower_delimitation]

    
