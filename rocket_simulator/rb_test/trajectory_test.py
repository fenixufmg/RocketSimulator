# Não editar
from core.physics.forces.weight_force import WeightForce
from core.physics.body.rigid_body import RigidBody
import matplotlib.pyplot as plt
import matplotlib

from models.structure.rocket_model import RocketModel
from simulation.simulation_output_wrapper import SimulationOutputWrapper
from simulation.abstract_ambient import AbstractAmbient
from simulation.simulation import Simulation
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def __mapColors(values):
    values_len = len(values)
    colors = [0 for number in range(len(values)*3)]
    for index, value in enumerate(values):
        # bagunça generalizada, procurar por documentação da função axis.quiver() caso queira mudar.
        arrow_index = values_len + index*2

        colors[index] = value
        colors[arrow_index] = value
        colors[arrow_index+1] = value

    normalizer=plt.Normalize(min(colors),max(colors))
    color_mapper = matplotlib.colors.LinearSegmentedColormap.from_list("", ["lime", "green" ,"olivedrab","orange","chocolate","red"])
    return (normalizer, color_mapper, color_mapper(normalizer(colors)))


def trajectoryTest(rocket:RocketModel, ambient: AbstractAmbient, simulation_time:int, limit=5000, arrow_scale=150, additional_forces:list=[] ,has_arrows=True, debug=True, step=None):
    simulation = Simulation(rocket, ambient, additional_forces=additional_forces)
    simulations = simulation.simulate(simulation_time)

    output_wrapper = SimulationOutputWrapper(simulations, step=step)
    simulations = output_wrapper.read()

    x = []
    y = []
    z = []
    x_magnitudes = []
    y_magnitudes = []
    z_magnitudes = []

    velocities = []
    for time, simulation in simulations.items():
        velocities.append(simulation.velocity.magnitude())
        x.append(simulation.cg.x()) 
        y.append(simulation.cg.y()) 
        z.append(simulation.cg.z())
        looking_direction = simulation.looking_direction * arrow_scale

        x_magnitudes.append(looking_direction.x())
        y_magnitudes.append(looking_direction.y())
        z_magnitudes.append(looking_direction.z())
        if debug:
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
            print(f"    Tip->cp (mag): {(simulation.cp - simulation.tip).magnitude()}")
            print()
            print(f"    Is on ground: {simulation.is_on_ground}")
            print(f"    Mass: {simulation.mass}")
            print("="*40)

    # ============ configurações do gráficos ============ #
    fig = plt.figure(figsize=(8,5))
    ax = fig.add_subplot(projection='3d')
    # ax = fig.gca(projection='3d')
    ax.set_xlim(0, limit)
    ax.set_ylim(-limit/2, limit/2)
    ax.set_zlim(0, limit)
    norm, cmap, vector_colors = __mapColors(velocities)
    point_colors = cmap(norm(velocities))

    ax.scatter(x,y,z, c=point_colors)
    plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
    if has_arrows:
        ax.quiver(x,y,z, x_magnitudes, y_magnitudes, z_magnitudes, color=vector_colors, cmap=cmap, norm=norm)
    # ============ configurações do gráficos ============ #

    plt.show()