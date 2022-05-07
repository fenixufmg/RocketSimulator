from core.physics.vector import Vector

class DeltaTimeSimulation:
    def __init__(self, rigid_body, time:int):
        self.cg = rigid_body.cg()
        self.cp = rigid_body.cp()
        self.velocity = rigid_body.velocity()
        self.angular_velocity = rigid_body.angularVelocity()
        self.mass = rigid_body.mass()
        self.looking_direction = rigid_body.getLookingDirection()
        self.time = time