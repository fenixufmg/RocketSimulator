from core.physics.forces.force import Force
from core.physics.vector import Vector
from utils.wind_direction import WindDirection
from core.physics.delta_time_simulation import DeltaTimeSimulation
from core.physics.body.application_point import ApplicationPoint

class WindForce(Force):
    def __init__(self, wind_velocity:float, wind_direction:WindDirection) -> None:
        super().__init__(0, 0, 0, ApplicationPoint.CP)
        self.wind_velocity:float = wind_velocity
        self.wind_direction:float = wind_direction.value

    def calculate(self, current_state: DeltaTimeSimulation): # https://www.wikihow.com/Calculate-Wind-Load
        wet_area = current_state.wet_area / 2
        wind_pressure = 0.613 * self.wind_velocity**2
        drag_coefficient = 0.75 # provisório
        magnitude = wet_area * wind_pressure * drag_coefficient

        direction = Vector(1, 0, 0)
        direction = Vector.rotateAroundAxis(direction, Vector(0, 0, 1), self.wind_direction)

        wind_force = direction * magnitude
        print(f"Wind force {wind_force}")

        self.setX(wind_force.x())
        self.setY(wind_force.y())
        self.setZ(wind_force.z())

