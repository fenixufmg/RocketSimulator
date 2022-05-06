from core.physics.forces.weight_force import WeightForce
from core.physics.body.rigid_body import RigidBody
import matplotlib.pyplot as plt
from core.physics.physics import Simulation
import numpy as np

def velocityTest(rigid_body:RigidBody, forces:list, simulation_time:int):
    weight = WeightForce()
    simulation = Simulation(rigid_body)
    for force in forces:
        simulation.addForce(force)
    simulation.addForce(weight)
    simulations = simulation.simulate(simulation_time)

    x = []
    y = []

    for time, simulation in simulations.items():
        x.append(simulation.time) 
        # y.append(simulation.velocity.magnitude()) 
        y.append(simulation.velocity.z()) 
    
    plt.plot(x,y, color="red")
    plt.ylabel("Velocidade (m/s)")
    plt.xlabel("Tempo decorrido (s)")
    plt.show()

