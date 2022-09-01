from utils.rocket_parts import RocketParts
from utils.utils import Utils
import imp

from numpy import single
from core.physics.forces.force import Force
from core.physics.delta_time_simulation import DeltaTimeSimulation
from core.physics.body.application_point import ApplicationPoint
from core.physics.vector import Vector
from core.aerodynamic.pitch_moment_coefficient_dervative import pitch_moment_coefficient_derivative
from core.aerodynamic.pitch_damping_moment_coefficient import pitch_damping_moment_coefficient
from core.aerodynamic.damping_force import damping_force
from core.aerodynamic.angular_velocity import angular_velocity
from utils.constants import Constants
from models.structure.rocket_model import RocketModel
from models.structure.nose_model import NoseModel, NoseType
from models.structure.fin_model import FinModel
from math import pi
from core.physics.forces.normal_force import NormalForce

class PitchDampingMoment(Force):
    def __init__(self):
        super().__init__(0, 0, 0, ApplicationPoint.CP, None)

    def calculate(self, current_state: DeltaTimeSimulation):
        air_density = 1.2 #Ampliar
        parts = current_state.parts

        if RocketParts.NOSE in parts:
            referenceArea = pi * current_state.nose.base_radius ** 2
            referenceDiameter = current_state.nose.base_diameter
        else:
            referenceArea = pi * (current_state.maximum_diameter_cilyndrical_body.diameter / 2) ** 2
            referenceDiameter = current_state.maximum_diameter_cilyndrical_body.diameter
        rocketLength = current_state.rocket_height.magnitude()
        velocity = current_state.velocity.magnitude()
        attack_angle = Utils.radiansToDegrees(Vector.angleBetweenVectors(current_state.looking_direction, current_state.velocity))
        angularVelocity = angular_velocity(velocity, attack_angle)
        Cdamp = 0 #Soma dos coeficientes de momento
        averageRadius = 0 #Raio médio do foguete

        if velocity == 0:
            self.setX(0)
            self.setY(0)
            self.setZ(0)
            return

        for part in parts:
            if part.part_type == RocketParts.NOSE:
                averageRadius += current_state.nose.base_radius
                # print(averageRadius)
                
            elif part.part_type == RocketParts.TRANSITION:
                topDiameter = part.top_diameter
                bottomDiameter = part.bottom_diameter
                if topDiameter > bottomDiameter:
                    averageRadius += current_state.transitions.top_diameter / 2

                else:
                    averageRadius += part.bottom_diameter / 2

            elif part.part_type == RocketParts.CYLINDRICAL_BODY:
                averageRadius += part.diameter / 2 #ERRO: ESTÁ PEGANDO APENAS DO PRIMEIRO CILINDRO
                # print(averageRadius)
            
            elif part.part_type == RocketParts.FIN:
                finArea = FinModel.calculateWetArea(self)
                numberFins = current_state.fin.nb_fins
                cg_cg_distance = current_state.fin.cg - current_state.cg
                tip_base_distance = current_state.base - current_state.tip
                tip_base_distance = tip_base_distance.unitVector()
                cg_fin_distance  = Vector.projectVector(cg_cg_distance, tip_base_distance )
                cg_fin_distance =  cg_fin_distance.magnitude()
                Cdamp += pitch_damping_moment_coefficient(numberFins, finArea, referenceArea, referenceDiameter, angularVelocity, velocity, cg_fin_distance)

            else:
                pass
            
        if RocketParts.FIN in parts:
            averageRadius = averageRadius / (len(parts) - 1)
        else:
            averageRadius = averageRadius / len(parts)

        
        Cdamp += 0.55 * rocketLength ** 4 * averageRadius * angularVelocity ** 2 / (referenceArea * referenceDiameter * velocity ** 2)
        
        magnitude = damping_force(Cdamp, air_density, velocity, referenceArea, referenceDiameter, current_state.tip_to_cg.magnitude())
        dampingForce = NormalForce.unitVector() * -1 * magnitude # não tem como fazer desse jeito (a direção), achar outro vetor pra pegar a direçao

        self.setX(dampingForce.x())
        self.setY(dampingForce.y())
        self.setZ(dampingForce.z())

        