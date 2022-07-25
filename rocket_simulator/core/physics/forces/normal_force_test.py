import imp
from core.physics.forces.force import Force
from core.physics.delta_time_simulation import DeltaTimeSimulation
from core.physics.body.application_point import ApplicationPoint
from core.physics.vector import Vector
from core.aerodynamic.body_normal_force_coefficient_derivative import body_normal_force_coefficient_derivative
from core.aerodynamic.normal_force import normal_force
from utils.constants import Constants
from math import pi, sin, radians


class NormalForceTest(Force):
    def __init__(self):
        super().__init__(0, 0, 0, ApplicationPoint.CP, None)
    
    def calculate(self, current_state: DeltaTimeSimulation):
      normal_force_coefficient = body_normal_force_coefficient_derivative #conferir
      air_density = 1.2
      velocity = current_state.velocity.magnitudeRelativeTo(current_state.velocity)
      reference_area = pi * current_state.nose.base_radius ** 2 #conferir 
      #attack_angle =
      magnitude = normal_force(normal_force_coefficient, air_density, velocity, reference_area, attack_angle)
      
      normalForce = current_state.velocity #a força aponta para fora da lateral do foguete, deve-se adicionar algo que redirecione o vetor de forma correta
      normalForce = normalForce.unitVector() * magnitude
      
      self.setX(normalForce.x())
      self.setY(normalForce.y())
      self.setZ(normalForce.z())
