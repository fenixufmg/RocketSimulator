from core.physics.body.application_point import ApplicationPoint
from core.physics.delta_time_simulation import DeltaTimeSimulation
from core.physics.vector import Vector
from abc import ABC, abstractmethod

class Force(Vector, ABC):
    def __init__(self, x, y, z, application_point:ApplicationPoint, cg_offset:float=None):
        super().__init__(x, y, z)
        self.__application_point = application_point
        self.__cg_offset = cg_offset # valores positivos -> acima do cg, valores negativos -> abaixo do cg
        self.__validate()

    def __validate(self):
        if self.__application_point == ApplicationPoint.CUSTOM:
            if self.__cg_offset is None:
                raise ValueError("No cg_offset given to custom application point")
        else:
            if self.__cg_offset is not None:
                raise ValueError("cg_offset is not defined for this application point")
        
        if isinstance(self.__cg_offset, Vector):
            raise ValueError(f"Wrong cg_offset type: {type(self.__cg_offset)}")


    def applicationPoint(self):
        return self.__application_point

    def cgOffset(self):
        return self.__cg_offset

    @abstractmethod
    def calculate(self, current_state:DeltaTimeSimulation):
        raise NotImplementedError("Function not implemented")
    