from abc import ABC, abstractmethod

class AbstractComponent(ABC):

    @abstractmethod
    def mass(self) -> float:
        pass

    @abstractmethod
    def cg(self) -> float:
        pass

    @abstractmethod
    def cp(self) -> float:
        pass