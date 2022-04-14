from models.physics.point_2d import Point2d
from models.physics.rigid_body_2d import RigidBody2d
from models.physics.vector_2d import Vector2d

class Physics2d:
    def __init__(self):
        self.__rigid_body = None

    def simulate(self, time:int) -> list: # chama addConstantForce e addVariableForce a cada 1s (delta time)
        delta_time_simulations = []

        # codigo iterativo

        return delta_time_simulations 

    def setRigidBody(self, rigid_body:RigidBody2d) -> None:
        if rigid_body is not None:
            self.__rigid_body = rigid_body

    def addConstantForce(self, force:Vector2d) -> None:
        pass

    def addVariableForce(self, force_function, *args) -> None:
        force:Vector2d = force_function(args)

    def __applyForce(self, force:Vector2d) -> None: # chamado a cada 1s (delta time)
        pass




