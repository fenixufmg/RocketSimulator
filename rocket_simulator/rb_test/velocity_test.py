from multiprocessing.sharedctypes import Value
from core.physics.forces.weight_force import WeightForce
from core.physics.body.rigid_body import RigidBody
import matplotlib.pyplot as plt

from models.structure.rocket_model import RocketModel
from simulation.abstract_ambient import AbstractAmbient
from simulation.simulation import Simulation
import numpy as np

from core.physics.vector import Vector
from simulation.simulation_output_wrapper import SimulationOutputWrapper


def velocityTest(rocket:RocketModel, ambient: AbstractAmbient, simulation_time:int, additional_forces=[],axis:Vector=None, step=None):
    simulation = Simulation(rocket, ambient, additional_forces=additional_forces)
    simulations = simulation.simulate(simulation_time)

    output_wrapper = SimulationOutputWrapper(simulations, step=step)
    simulations = output_wrapper.read()

    x = []
    y = []

    for time, simulation in simulations.items():
        x.append(simulation.time) 

        print(f"Time: {time}")
        print(f"    Velocity: {simulation.velocity}")
        print(f"    Acceleration: {simulation.acceleration}")

        print(f"    Moment of inertia: {simulation.moment_of_inertia}")
        print(f"    Angular velocity: {simulation.angular_velocity}")
        print(f"    Angular acceleration: {simulation.angular_acceleration}")

        print(f"    Cg position: {simulation.cg}")
        print(f"    Cp position: {simulation.cp}")
        print(f"    cg->cp: {simulation.cp - simulation.cg}")
        print(f"    cg->cp (mag): {(simulation.cp - simulation.cg).magnitude()}")
        print()
        print(f"    Tip position: {simulation.tip}")
        print(f"    Base position: {simulation.base}")
        print(f"    Tip->Base: {simulation.base - simulation.tip}")
        print(f"    Tip->Base (mag): {(simulation.base - simulation.tip).magnitude()}")
        print()
        print(f"    Is on ground: {simulation.is_on_ground}")
        print(f"    Mass: {simulation.mass}")
        print("="*40)



        if axis is None:
            y.append(simulation.velocity.magnitude())
        else:
            y_value = Vector.projectVector(simulation.velocity, axis).magnitudeRelativeTo(axis)
            y.append(y_value)
    
    plt.plot(x,y, color="red")
    plt.ylabel("Velocidade (m/s)")
    plt.xlabel("Tempo decorrido (s)")
    plt.show()

