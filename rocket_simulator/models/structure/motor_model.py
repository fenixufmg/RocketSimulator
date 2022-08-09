from core.physics.forces.force import Force
from core.physics.forces.impulse_test_force import ImpulseTestForce
from utils.rocket_parts import RocketParts
from models.structure.abstract_model import AbstractModel
from core.physics.vector import Vector
from utils.constants import Constants

class MotorModel(AbstractModel):
    def __init__(self, position_order:int):
        self.drag_coefficient = self.__calculateDragCoefficient()
        self.transversal_area = self.__calculateTransversalArea()
 
        super().__init__(RocketParts.MOTOR, position_order,  self.drag_coefficient, self.transversal_area)
        self.__verify()

    def __verify(self): # fazer
        pass

    def __calculateDragCoefficient(self): # fazer
        pass
    
    def __calculateTransversalArea(self): # fazer
        pass

