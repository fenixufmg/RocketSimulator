from core.physics.vector import Vector

class DeltaTimeSimulation:
    def __init__(self, rigid_body, time:int):
        """ Representa o estado do rigid body em determinado instante de tempo.

        Args:
            rigid_body (_type_): Corpo rígido do qual serão retiradas as informações.
            time (int): Instante de tempo.

        Fields:
            cg (Vector): Centro de gravidade do corpo
            cp (Vector): Centro de pressão do corpo
            velocity (Vector): Velocidade do corpo
            acceleration (Vector): Aceleração do corpo
            angular_velocity (Vector): Velocidade angular do corpo
            mass (float): Massa do corpo
            looking_direction (Vector): Vetor que representa a orientação do corpo
            time (float): Instante de tempo
        """
        self.cg = rigid_body.cg()
        self.cp = rigid_body.cp()
        self.velocity = rigid_body.velocity()
        self.acceleration = rigid_body.acceleration()
        self.angular_velocity = rigid_body.angularVelocity()
        self.mass = rigid_body.mass()
        self.looking_direction = rigid_body.getLookingDirection()
        self.time = time