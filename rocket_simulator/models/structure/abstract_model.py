from abc import ABC, abstractmethod
from core.physics.body.rigid_body import RigidBody
from rocket_simulator.core.physics.vector import Vector

class AbstractModel(ABC, RigidBody):
    def __init__(self) -> None:
        volume = self.calculateVolume()
        mass = self.calculateMass()
        moment_of_inertia = self.calculateMomentOfInertia()
        cg = self.calculateCg()
        cp = self.calculateCp()
        delimitation_points = self.createDelimitationPoints()
        super().__init__(delimitation_points, mass, volume, moment_of_inertia, cg, cp)
    
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

    def updateState(self) -> None:
        self.volume = self.calculateVolume()
        self.mass = self.calculateMass()
        self.moment_of_inertia = self.calculateMomentOfInertia()
        self.cg = self.calculateCg()
        self.cp = self.calculateCp()
