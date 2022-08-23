from utils.utils import Utils
import imp

from numpy import single
from core.physics.forces.force import Force
from core.physics.delta_time_simulation import DeltaTimeSimulation
from core.physics.body.application_point import ApplicationPoint
from core.physics.vector import Vector
from core.aerodynamic.body_normal_force_coefficient_derivative import body_normal_force_coefficient_derivative
from core.aerodynamic.fin_body_interference import final_normal_force_coefficient_derivative
from core.aerodynamic.fin_normal_force_coefficient_derivative import normal_force_coefficient_derivative
from core.aerodynamic.single_fin_normal_force_coefficient import single_fin_normal_force_coefficient
from core.aerodynamic.normal_force import normal_force
from core.aerodynamic.mach_number import mach_number
from utils.constants import Constants
from models.structure.rocket_model import RocketModel
from models.structure.nose_model import NoseModel, NoseType
from models.structure.fin_model import FinModel
from math import pi, sin, radians

class NormalForceTest(Force):
    def __init__(self):
        super().__init__(0, 0, 0, ApplicationPoint.CP, None)
    
    def calculate(self, current_state: DeltaTimeSimulation):
        air_density = 1.2 #Ampliar
        attack_angle = Utils.radiansToDegrees(Vector.angleBetweenVectors(current_state.looking_direction, current_state.velocity))
        velocity = current_state.velocity.magnitudeRelativeTo(current_state.velocity)
        reference_area = pi * current_state.nose.base_radius ** 2 
        mach = mach_number(velocity, 340)
        parts = current_state.parts
        CNan_sum = 0 #Soma dos coeficientes normais
        for part in parts:
            type = str(part.part_type)
            if type == 'RocketParts.NOSE':
                Abase = reference_area #Área da base do corpo
                Atop = 0 #Área do topo do corpo
                CNan = body_normal_force_coefficient_derivative(Abase, Atop, reference_area, attack_angle) #Coeficiente de força normal derivado
                CNan_sum += CNan
                
            elif type == 'RocketParts.TRANSITION':
                Abase = pi * (current_state.transitions.bottom_diameter ** 2) / 4 #Área da base do corpo
                Atop = pi * (current_state.transitions.top_diameter ** 2) / 4 #Área do topo do corpo
                CNan = body_normal_force_coefficient_derivative(Abase, Atop, reference_area, attack_angle) #Coeficiente de força normal derivado
                CNan_sum += CNan
            
            elif type == 'RocketParts.FIN':
                CNa1 = single_fin_normal_force_coefficient(current_state.fin.span, reference_area, mach, current_state.fin.wet_area, current_state.fin.sweep_angle) #Criar código para transversal_area
                CNanF = normal_force_coefficient_derivative(CNa1, 0, current_state.fin.nb_fins, current_state.fin.nb_fins)
                CNaTb = final_normal_force_coefficient_derivative(CNanF, current_state.fin.span, current_state.fin.distance_from_center)
                CNan_sum += CNaTb
            
            else:
                pass
        print(CNan_sum) 
    
        magnitude = normal_force(CNan_sum, air_density, velocity, reference_area, attack_angle)

        normalForceX = Vector.projectVector(current_state.velocity, Vector(1, 0, 0))
        normalForceY = Vector.projectVector(current_state.velocity, Vector(0, 1, 0))

        if normalForceX.toList()[0] > 0:
            normalForceX = normalForceX.unitVector()
        else:
            normalForceX = normalForceX.unitVector() * (-1)

        if normalForceY.toList()[1] > 0:
            normalForceY = normalForceY.unitVector()
        else:
            normalForceY = normalForceY.unitVector() * (-1)
            
        normalForce = normalForceX + normalForceY
        normalForce = normalForce.unitVector() * magnitude

        print(normalForce)
        self.setX(normalForce.x())
        self.setY(normalForce.y())
        self.setZ(normalForce.z())
