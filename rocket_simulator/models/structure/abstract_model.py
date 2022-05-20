from abc import ABC, abstractmethod
from core.physics.body.rigid_body import RigidBody
from rocket_simulator.core.physics.vector import Vector

class AbstractModel(ABC):
    def __init__(self) -> None:
        self.volume = self.calculateVolume()
        self.mass = self.calculateMass()
        self.moment_of_inertia = self.calculateMomentOfInertia()
        self.cg = self.calculateCg()
        self.cp = self.calculateCp()
        # self.delimitation_points = self.createDelimitationPoints()
        self.rigid_body = self.createRigidBody()

    @abstractmethod
    def calculateVolume(self) -> float:
        raise NotImplementedError("Function not implemented")

    @abstractmethod
    def calculateMass(self)-> float:
        raise NotImplementedError("Function not implemented")

    @abstractmethod
    def calculateMomentOfInertia(self) -> float:
        raise NotImplementedError("Function not implemented")

    @abstractmethod
    def calculateCg(self) -> Vector:
        raise NotImplementedError("Function not implemented")

    @abstractmethod
    def calculateCp(self) -> Vector:
        raise NotImplementedError("Function not implemented")

    @abstractmethod
    def createDelimitationPoints(self) -> list:
        raise NotImplementedError("Function not implemented")

    @abstractmethod
    def createRigidBody(self) -> RigidBody:
        raise NotImplementedError("Function not implemented")
