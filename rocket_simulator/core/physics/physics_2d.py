from models.physics.point import Point
from models.physics.rigid_body import RigidBody
from models.physics.vector import Vector

class Physics2d:
    def __init__(self):
        self.__rigid_body = None

    def simulate(self, time:int) -> list: # chama addConstantForce e addVariableForce a cada 1s (delta time)
        delta_time_simulations = []

        # codigo iterativo

        return delta_time_simulations 

    def setRigidBody(self, rigid_body:RigidBody) -> None:
        if rigid_body is not None:
            self.__rigid_body = rigid_body

    def addConstantForce(self, force:Vector) -> None:
        pass

    def addVariableForce(self, force_function, *args) -> None:
        force:Vector = force_function(args)

    def __applyForce(self, force:Vector) -> None: # chamado a cada 1s (delta time)
        pass




