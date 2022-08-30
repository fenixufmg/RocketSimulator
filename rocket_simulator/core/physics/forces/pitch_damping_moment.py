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
        referenceArea = pi * current_state.nose.base_radius ** 2
        referenceDiameter = current_state.nose.base_diameter
        rocketLength = current_state.rocket_height.magnitude()
        velocity = current_state.velocity.magnitude()
        parts = current_state.parts
        attack_angle = Utils.radiansToDegrees(Vector.angleBetweenVectors(current_state.looking_direction, current_state.velocity))
        Cdamp = 0 #Soma dos coeficientes de momento
        averageRadius = 0 #Raio médio do foguete

        for part in parts:
            type = str(part.part_type)
            if type == 'RocketParts.NOSE':
                averageRadius += current_state.nose.base_radius
                print(averageRadius)
                
            elif type == 'RocketParts.TRANSITION':
                topDiameter = current_state.transitions.top_diameter
                bottomDiameter = current_state.transitions.bottom_diameter
                if topDiameter > bottomDiameter:
                    averageRadius += current_state.transitions.top_diameter / 2

                else:
                    averageRadius += current_state.transitions.bottom_diameter / 2

            elif type == 'RocketParts.CYLINDRICAL_BODY':
                averageRadius += current_state.cilyndrical_bodies.diameter / 2 #ERRO: ESTÁ PEGANDO APENAS DO PRIMEIRO CILINDRO
                print(averageRadius)
            
            elif type == 'RocketParts.FIN':
                finArea = FinModel.calculateWetArea(self)
                numberFins = current_state.fin.nb_fins
                angularVelocity = angular_velocity(velocity, attack_angle)
                cg_cg_distance = current_state.fin.cg - current_state.cg
                tip_base_distance = current_state.base - current_state.tip
                cg_fin_distance = Vector.projectVector(cg_cg_distance, tip_base_distance)
                cg_fin_distance = cg_fin_distance.magnitude()
                Cdamp += pitch_damping_moment_coefficient(numberFins, finArea, referenceArea, referenceDiameter, angularVelocity, velocity, cg_fin_distance)

            else:
                pass
            
        if 'RocketParts.FIN' in parts:
            averageRadius = averageRadius / (len(parts) - 1)
        else:
            averageRadius = averageRadius / len(parts)

        Cdamp += 0.55 * rocketLength ** 4 * averageRadius * angularVelocity ** 2 / (referenceArea * referenceDiameter * velocity ** 2)
        
        magnitude = damping_force(Cdamp, air_density, velocity, referenceArea, referenceDiameter, current_state.tip_to_cg.magnitude())
        dampingForce = NormalForce.unitVector() * -1 * magnitude

        self.setX(dampingForce.x())
        self.setY(dampingForce.y())
        self.setZ(dampingForce.z())

        