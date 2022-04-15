from models.physics.application_point import ApplicationPoint
from models.physics.delta_time_simulation import DeltaTimeSimulation
from vector import Vector
from abc import ABC, abstractmethod

class Force(Vector, ABC):
    def __init__(self, x, y, z, application_point:ApplicationPoint, cg_offset=None):
        super().__init__(x, y, z)
        self.__application_point = application_point
        self.__cg_offset = cg_offset

    def applicationPoint(self):
        if self.__application_point == ApplicationPoint.CUSTOM:
            if self.__cg_offset is None:
                raise ValueError("No cg_offset given to custom application point")

            return self.__cg_offset
        return self.__application_point

    @abstractmethod
    def calculate(self, last_simulation:DeltaTimeSimulation):
        pass
    