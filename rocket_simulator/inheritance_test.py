from abc import ABC, abstractmethod
class Parent(ABC):
    def __init__(self) -> None:
        self.a = self.calculateA()
        pass

    @abstractmethod
    def calculateA(self):
        pass

class Child(Parent):
    def __init__(self) -> None:
        super().__init__()

    def calculateA(self):
        return 2

    def getA(self):
        return self.a

child = Child()
print(child.getA())