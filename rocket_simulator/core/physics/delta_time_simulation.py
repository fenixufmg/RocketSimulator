from typing import List

from core.physics.vector import Vector
from utils.rocket_parts import RocketParts


class DeltaTimeSimulation:
    def __init__(self, rocket, time: int):
        """ Representa o estado do foguete em determinado instante de tempo.

        Args:
            rocket (RocketModel): Foguete do qual serão retiradas as informações.
            time (int): Instante de tempo.
        """
        self.cg: Vector = rocket.cg
        self.cp: Vector = rocket.cp
        self.tip: Vector = rocket.delimitation_points[0]
        self.base: Vector = rocket.delimitation_points[1]

        self.tip_to_cg = self.cg - self.tip
        self.rocket_height = rocket.rocket_height
        self.position: Vector = rocket.total_displacement
        self.velocity: Vector = rocket.velocity
        self.acceleration: Vector = rocket.total_acceleration
        self.moment_of_inertia: float = rocket.moment_of_inertia
        self.angular_acceleration: Vector = rocket.total_angular_acceleration
        self.angular_velocity: Vector = rocket.angular_velocity
        self.mass: float = rocket.mass
        self.volume:float = rocket.volume
        self.wet_area:float = rocket.wet_area
        self.looking_direction: Vector = rocket.getLookingDirection()
        self.time: float = time
        self.is_on_ground:bool = rocket.is_on_ground

        # peças
        self.parts = rocket.getParts()
        self.parachute = rocket.getPart(RocketParts.PARACHUTE)
        self.nose = rocket.getPart(RocketParts.NOSE)
        self.cilyndrical_bodies = rocket.getPart(RocketParts.CYLINDRICAL_BODY)

        self.transitions = rocket.getPart(RocketParts.TRANSITION)
        self.fin = rocket.getPart(RocketParts.FIN)
        self.motor = rocket.getPart(RocketParts.MOTOR)

        self.maximum_diameter_cilyndrical_body = self.__getMaximumDiameterCylindricalBody()
        self.maximum_top_diameter_transition = self.__getMaximumTopDiameterTransition()
        self.maximum_bottom_diameter_transition = self.__getMaximumBottomDiameterTransition()

    def __getMaximumDiameterCylindricalBody(self):  # Provisorio, mudar para outra classe para organização
        maximum_diameter = 0
        result = None

        if self.cilyndrical_bodies is None:
            return

        for body in self.cilyndrical_bodies:
            if body.diameter > maximum_diameter:
                maximum_diameter = body.diameter
                result = body

        return result

    def __getMaximumTopDiameterTransition(self):  # Provisorio, mudar para outra classe para organização
        maximum_diameter = 0
        result = None

        if self.transitions is None:
            return

        for body in self.transitions:
            if body.top_diameter > maximum_diameter:
                maximum_diameter = body.top_diameter
                result = body

        return result

    def __getMaximumBottomDiameterTransition(self):  # Provisorio, mudar para outra classe para organização
        maximum_diameter = 0
        result = None

        if self.transitions is None:
            return

        for body in self.transitions:
            if body.bottom_diameter > maximum_diameter:
                maximum_diameter = body.bottom_diameter
                result = body

        return result

