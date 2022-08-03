import imp
from core.physics.forces.force import Force
from core.physics.delta_time_simulation import DeltaTimeSimulation
from core.physics.body.application_point import ApplicationPoint
from core.physics.vector import Vector
from core.aerodynamic.body_normal_force_coefficient_derivative import body_normal_force_coefficient_derivative
from core.aerodynamic.normal_force import normal_force
from utils.constants import Constants
from models.structure.rocket_model import RocketModel
from models.structure.nose_model import NoseModel, NoseType
from math import pi, sin, radians


class NormalForceTest(Force):
    def __init__(self):
        super().__init__(0, 0, 0, ApplicationPoint.CP, None)
    
    def calculate(self, current_state: DeltaTimeSimulation):
        rocket = RocketModel()
        air_density = 1.2
        attack_angle = 1
        velocity = current_state.velocity.magnitudeRelativeTo(current_state.velocity)
        reference_area = pi * current_state.nose.base_radius ** 2 #conferir 
        parts = rocket.getParts()
        CNan_sum = 0 #Soma dos coeficientes normais
        for part in parts:
            type = str(part.part_type)
            #enxugar código!
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
            
            elif type == 'RocketParts.CYLINDRICAL_BODY': 
                pass

            else:
                pass
        
        #normal_force_coefficient = body_normal_force_coefficient_derivative() #CORRIGIR

        
        
        magnitude = normal_force(normal_force_coefficient, air_density, velocity, reference_area, attack_angle)
        
        normalForce = current_state.velocity #a força aponta para fora da lateral do foguete, deve-se adicionar algo que redirecione o vetor de forma correta
        normalForce = normalForce.unitVector() * magnitude
        
        self.setX(normalForce.x())
        self.setY(normalForce.y())
        self.setZ(normalForce.z())
