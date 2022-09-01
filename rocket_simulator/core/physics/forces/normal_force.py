from utils.rocket_parts import RocketParts
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
from math import pi

class NormalForce(Force):
    def __init__(self):
        super().__init__(0, 0, 0, ApplicationPoint.CP, None)
    
    def calculate(self, current_state: DeltaTimeSimulation):
        if current_state.velocity.magnitude() == 0:
            self.setX(0)
            self.setY(0)
            self.setZ(0)
            return
            
        # print("Normal_force debug:")
        air_density = 1.2 #Ampliar
        attack_angle = Vector.angleBetweenVectors(current_state.looking_direction, current_state.velocity)
        attack_angle = Utils.radiansToDegrees(attack_angle)
        # print(f"    looking_direction: {current_state.looking_direction}")
        # print(f"    velocity: {current_state.velocity}")
        # print(f"    attack_angle: {attack_angle}")
        velocity = current_state.velocity.magnitude()
        reference_area = pi * current_state.nose.base_radius ** 2 
        mach = mach_number(velocity, 340)
        parts = current_state.parts
        CNan_sum = 0 #Soma dos coeficientes normais
        for part in parts:
            if part.part_type == RocketParts.NOSE:
                Abase = reference_area #Área da base do corpo
                Atop = 0 #Área do topo do corpo
                CNan = body_normal_force_coefficient_derivative(Abase, Atop, reference_area, attack_angle) #Coeficiente de força normal derivado
                
                # print(f"    CNan: {CNan}")
                CNan_sum += CNan
                
            elif part.part_type == RocketParts.TRANSITION:
                Abase = pi * (part.bottom_diameter ** 2) / 4 #Área da base do corpo
                Atop = pi * (part.top_diameter ** 2) / 4 #Área do topo do corpo
                CNan = body_normal_force_coefficient_derivative(Abase, Atop, reference_area, attack_angle) #Coeficiente de força normal derivado
                CNan_sum += CNan
            
            elif part.part_type == RocketParts.FIN:
                CNa1 = single_fin_normal_force_coefficient(part.span, reference_area, mach, part.wet_area, part.sweep_angle) #Criar código para transversal_area
                CNanF = normal_force_coefficient_derivative(CNa1, 0, part.nb_fins, part.nb_fins)
                CNaTb = final_normal_force_coefficient_derivative(CNanF, part.span, part.distance_from_center)
                CNan_sum += CNaTb


        
        # print(f"    Time: {current_state.time}")
        # print(f"    Rocket velocity: {current_state.velocity.magnitude()}")
        # print(f"    CNan_sum: {CNan_sum}") 
        
    
        magnitude = normal_force(CNan_sum, air_density, velocity, reference_area, attack_angle)

        normalForceX = Vector.projectVector(current_state.velocity, Vector(1, 0, 0)).unitVector()
        normalForceY = Vector.projectVector(current_state.velocity, Vector(0, 1, 0)).unitVector()
        normalForceZ = Vector.projectVector(current_state.velocity, Vector(0, 0, 1)).unitVector()

        # if normalForceX.toList()[0] > 0: # não precisa
        #     normalForceX = normalForceX.unitVector()
        # else:
        #     normalForceX = normalForceX.unitVector() * (-1)

        # if normalForceY.toList()[1] > 0:
        #     normalForceY = normalForceY.unitVector()
        # else:
        #     normalForceY = normalForceY.unitVector() * (-1)

        # if normalForceZ.toList()[2] > 0:
        #     normalForceZ = normalForceZ.unitVector()
        # else:
        #     normalForceZ = normalForceZ.unitVector() * (-1)
            
        normalForce = normalForceX + normalForceY + normalForceZ
        normalForce = normalForce.unitVector() * magnitude

        print(f"    Normal force: {normalForce}")
        self.setX(normalForce.x())
        self.setY(normalForce.y())
        self.setZ(normalForce.z())
