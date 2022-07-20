from core.physics.forces.force import Force
from core.physics.delta_time_simulation import DeltaTimeSimulation
from core.physics.body.application_point import ApplicationPoint

class RotationTestForce(Force):
    def __init__(self, x, y, z, application_point: ApplicationPoint):
        self._setted_x = x
        self._setted_y = y
        self._setted_z = z
        super().__init__(x, y, z, application_point)

    def calculate(self, current_state:DeltaTimeSimulation):
        pass
        if current_state.time < 5:
            self.setX(0)
            self.setY(0)
            self.setZ(0)
            
        if current_state.time >= 5:
            self.setX(self._setted_x)
            self.setY(self._setted_y)
            self.setZ(self._setted_z)

        # if current_state.time >= 8:
        #     self.setX(-self._setted_x)
        #     self.setY(-self._setted_y)
        #     self.setZ(-self._setted_z)

        if current_state.time >= 7:
            self.setX(0)
            self.setY(0)
            self.setZ(0)