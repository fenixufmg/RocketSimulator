from multiprocessing.sharedctypes import Value
from core.physics.forces.weight_force import WeightForce
from core.physics.body.rigid_body import RigidBody
import matplotlib.pyplot as plt
from simulation.simulation import Simulation
import numpy as np

from core.physics.vector import Vector

def angularVelocityTest(rigid_body:RigidBody, forces:list, simulation_time:int, axis:Vector=None):
    simulation = Simulation(rigid_body, forces)
    simulations = simulation.simulate(simulation_time)

    x = []
    y = []

    for time, simulation in simulations.items():
        x.append(simulation.time) 
        
        if axis is None:
            y.append(simulation.angular_velocity.magnitude())
        else:
            y_value = Vector.projectVector(simulation.angular_velocity, axis).magnitudeRelativeTo(axis)
            y.append(y_value)
    
    plt.plot(x,y, color="red")
    plt.ylabel("Velocidade angular (rad/s)")
    plt.xlabel("Tempo decorrido (s)")
    plt.show()

