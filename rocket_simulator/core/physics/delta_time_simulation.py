from typing import List

from core.physics.vector import Vector
from utils.rocket_parts import RocketParts


class DeltaTimeSimulation:
    def __init__(self, rocket, time: int):
        """ Representa o estado do foguete em determinado instante de tempo.

        Args:
            rocket (RocketModel): Foguete do qual serão retiradas as informações.
            time (int): Instante de tempo.

        Fields:
            cg (Vector): Centro de gravidade do corpo
            cp (Vector): Centro de pressão do corpo
            tip (Vector): Ponta do corpo
            base (Vector): Base do corpo
            velocity (Vector): Velocidade do corpo
            acceleration (Vector): Aceleração do corpo
            angular_velocity (Vector): Velocidade angular do corpo
            mass (float): Massa do corpo
            looking_direction (Vector): Vetor que representa a orientação do corpo
            time (float): Instante de tempo
        """
        self.cg: Vector = rocket.cg
        self.cp: Vector = rocket.cp
        self.tip: Vector = rocket.delimitation_points[0]
        self.base: Vector = rocket.delimitation_points[1]
        self.position: Vector = rocket.total_displacement
        self.velocity: Vector = rocket.velocity
        self.acceleration: Vector = rocket.total_acceleration
        self.angular_acceleration: Vector = rocket.total_angular_acceleration
        self.angular_velocity: Vector = rocket.angular_velocity
        self.mass: float = rocket.mass
        self.looking_direction: Vector = rocket.getLookingDirection()
        self.time: float = time
        self.is_on_ground:bool = rocket.is_on_ground

        # peças
        self.parachute = rocket.getPart(RocketParts.PARACHUTE)
        self.nose = rocket.getPart(RocketParts.NOSE)
        self.cilyndrical_bodies = rocket.getPart(RocketParts.CYLINDRICAL_BODY)
        self.transitions = rocket.getPart(RocketParts.TRANSITION)
        self.fin = rocket.getPart(RocketParts.FIN)
        self.motor = rocket.getPart(RocketParts.MOTOR)
