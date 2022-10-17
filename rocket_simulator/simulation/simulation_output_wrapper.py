from typing import List
from core.physics.delta_time_simulation import DeltaTimeSimulation
import numpy as np


class SimulationOutputWrapper():
    def __init__(self, data:dict, step=None) -> None:
        """ Classe responsável por pegar os dados de output de Simulation.simulate() e processar/gerenciar eles.
        """
        self.__raw_data = data
        self.__DELTA_TIME = self.__setDeltaTime()
        self.__time = list(data.keys())[-1]  # tempo máximo de simulação
        self.__step = step  # steps custom para posterior filtragem dos dados.

    def __setDeltaTime(self):
        """ Retorna o DELTA_TIME com base em duas amostras.
        """
        samples = list(self.__raw_data.keys())[:2]
        return samples[1] - samples[0]

    def read(self) -> dict:
        """ Filtra os dados de 'pulando' os valores de tempo de acordo com self.__step.
        """
        if self.__step is None:
            return self.__raw_data

        filtered_data = dict()
        for time in np.arange(0, self.__time + self.__DELTA_TIME, self.__step):
            try:
                filtered_data[time] = self.__raw_data[time]
            except KeyError:
                raise ValueError(f"Invalid step: {self.__step}")

        return filtered_data

    def write(self):
        """ Essa função irá salvar os dados brutos e/ou filtrados em disco.
        """
        pass
    
