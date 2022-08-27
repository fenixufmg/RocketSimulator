from utils.utils import Utils
import imp

from numpy import single
from core.physics.forces.force import Force
from core.physics.delta_time_simulation import DeltaTimeSimulation
from core.physics.body.application_point import ApplicationPoint
from core.physics.vector import Vector
from core.aerodynamic.pitch_moment_coefficient_dervative import pitch_moment_coefficient_derivative
from core.aerodynamic.normal_force import normal_force
from core.aerodynamic.mach_number import mach_number
from utils.constants import Constants
from models.structure.rocket_model import RocketModel
from models.structure.nose_model import NoseModel, NoseType
from models.structure.fin_model import FinModel
from math import pi, sin, radians
from core.physics.forces.normal_force import NormalForce

class PitchDampingMoment(Force):
    def __init__(self):
        super().__init__(0, 0, 0, ApplicationPoint.CP, None)

    def calculate(self, current_state: DeltaTimeSimulation):
        referenceArea = pi * current_state.nose.base_radius ** 2
        referenceDiameter = current_state.nose.base_diameter
        parts = current_state.parts
        attack_angle = Utils.radiansToDegrees(Vector.angleBetweenVectors(current_state.looking_direction, current_state.velocity))
        Cdamp = 0 #Soma dos coeficientes de momento
        for part in parts:
            type = str(part.part_type)
            if type == 'RocketParts.NOSE':
                Abase = referenceArea #Área da base do corpo
                Atop = 0 #Área do topo do corpo
                
            elif type == 'RocketParts.TRANSITION':
                pass
            
            elif type == 'RocketParts.FIN':
                pass
            else:
                pass

        pitchForce = 0

        self.setX(pitchForce.x())
        self.setY(pitchForce.y())
        self.setZ(pitchForce.z())