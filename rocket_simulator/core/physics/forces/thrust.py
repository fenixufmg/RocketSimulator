from core.physics.forces.force import Force
from core.physics.delta_time_simulation import DeltaTimeSimulation
from core.physics.body.application_point import ApplicationPoint
from models.other.propellant_model import PropellantModel


class Thrust(Force):
    def __init__(self, propellant_model:PropellantModel):
        self.propellant_model = propellant_model
        super().__init__(0,0,0, ApplicationPoint.CG, None)
    
    def calculate(self, current_state:DeltaTimeSimulation):
        direction = current_state.looking_direction
        magnitude = self.propellant_model.interpolateThrust(current_state.time)  # deverá pegar a magnitude baseado na curva de empuxo (IMPLEMENTAR)
        thrust = direction * magnitude

        self.setX(thrust.x())
        self.setY(thrust.y())
        self.setZ(thrust.z())

