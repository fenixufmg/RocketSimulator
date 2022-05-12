from multiprocessing.sharedctypes import Value
from core.physics.forces.weight_force import WeightForce
from core.physics.body.rigid_body import RigidBody
import matplotlib.pyplot as plt
from core.physics.simulation import Simulation
import numpy as np

from core.physics.vector import Vector

def accelerationTest(rigid_body:RigidBody, forces:list, simulation_time:int, axis:Vector=None):
    simulation = Simulation(rigid_body)
    for force in forces:
        simulation.addForce(force)
    simulations = simulation.simulate(simulation_time)

    x = []
    y = []

    for time, simulation in simulations.items():
        x.append(simulation.time) 

        if axis is None:
            y.append(simulation.acceleration.magnitude())
        else:
            y_value = Vector.projectVector(simulation.acceleration, axis).magnitudeRelativeTo(axis)
            y.append(y_value)
    
    plt.plot(x,y, color="red")
    plt.ylabel("Aceleração (m/s^2)")
    plt.xlabel("Tempo decorrido (s)")
    plt.show()

