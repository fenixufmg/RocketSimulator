from abc import ABC, abstractmethod
from typing import List
from core.physics.body.rigid_body import RigidBody
from core.physics.vector import Vector
from utils.rocket_parts import RocketParts

class AbstractModel(ABC, RigidBody):
    def __init__(self, part_type: RocketParts, position_order: int, shape_coefficient:float, 
                drag_coefficient:float, transversal_area:float) -> None:
        # rocket specific
        self.part_type = part_type
        self.position_order = position_order
        self.shape_coefficient = shape_coefficient
        self.drag_coefficient = drag_coefficient
        self.transversal_area = transversal_area  

        # rigid body fields
        self.delimitation_points = self.createDelimitationPoints()
        volume = self.calculateVolume()
        self.volume = volume
        mass = self.calculateMass()
        moment_of_inertia = self.calculateMomentOfInertia
        cg = self.calculateCg()
        cp = self.calculateCp()
        super().__init__(self.delimitation_points, mass, volume, moment_of_inertia, cg, cp)
    
    @abstractmethod
    def calculateVolume(self) -> float:
        raise NotImplementedError("Function not implemented")

    @abstractmethod
    def calculateMass(self) -> float:
        raise NotImplementedError("Function not implemented")

    @abstractmethod
    def calculateMomentOfInertia(self, distance_to_cg:float) -> float:
        raise NotImplementedError("Function not implemented")

    @abstractmethod
    def calculateCg(self) -> Vector:
        raise NotImplementedError("Function not implemented")

    @abstractmethod
    def calculateCp(self) -> Vector: # http://ftp.demec.ufpr.br/foguete/bibliografia/TIR-33%20Calculating%20the%20Center%20of%20Pressure%20of%20a%20Model%20Rocket.pdf
        raise NotImplementedError("Function not implemented")

    @abstractmethod
    def createDelimitationPoints(self) -> List[Vector]:
        raise NotImplementedError("Function not implemented")

    # def getHeight(self) -> float:
    #     raise NotImplementedError("Function not implemented")

    def updateState(self) -> None:
        self.volume = self.calculateVolume()
        self.mass = self.calculateMass()
        self.moment_of_inertia = self.calculateMomentOfInertia
        self.cg = self.calculateCg()
        self.cp = self.calculateCp()

    def toGroundCoordinates(self, local_coordinates:Vector) -> Vector:
        return self.getTip() + local_coordinates

    def getPosition(self):
        position = [self.delimitation_points[0].toList(), self.cg.toList(), self.delimitation_points[1].toList()]
        return position

