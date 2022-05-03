from abc import ABC, abstractmethod
from core.physics.body.rigid_body import RigidBody

class AbstractModel(ABC):

    @abstractmethod
    def __createRigidBody(self) -> RigidBody:
        pass