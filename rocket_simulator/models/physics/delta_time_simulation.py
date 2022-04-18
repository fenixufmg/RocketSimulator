from models.physics.vector import Vector

class DeltaTimeSimulation:
    def __init__(self, rigid_body, time:int):
        self.position = rigid_body.cg()
        self.velocity = rigid_body.velocity()
        self.angular_velocity = rigid_body.angularVelocity()
        self.mass = rigid_body.mass()
        self.time = time