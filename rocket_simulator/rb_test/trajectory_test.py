# Não editar
from core.physics.forces.weight_force import WeightForce
from core.physics.body.rigid_body import RigidBody
import matplotlib.pyplot as plt
import matplotlib
from core.physics.simulation import Simulation
import numpy as np

def __mapColors(values):
    values_len = len(values)
    colors = [0 for number in range(len(values)*3)]
    for index, value in enumerate(values):
        arrow_index = values_len + index*2

        colors[index] = value
        colors[arrow_index] = value
        colors[arrow_index+1] = value

    normalizer=plt.Normalize(min(colors),max(colors))
    color_mapper = matplotlib.colors.LinearSegmentedColormap.from_list("", ["lime", "green" ,"olivedrab","orange","chocolate","red"])
    return (normalizer, color_mapper, color_mapper(normalizer(colors)))

def trajectoryTest(rigid_body:RigidBody, forces:list, simulation_time:int, limit=5000, arrow_scale=150, has_arrows=True):
    simulation = Simulation(rigid_body)
    for force in forces:
        simulation.addForce(force)
    simulations = simulation.simulate(simulation_time)

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

    # ============ configurações do gráficos ============ #
    fig = plt.figure(figsize=(8,5))
    ax = fig.add_subplot(projection='3d')
    ax.set_xlim(0, limit)
    ax.set_ylim(-limit/2, limit/2)
    ax.set_zlim(0, limit)
    norm, cmap, vector_colors = __mapColors(velocities)
    point_colors = cmap(norm(velocities))
    # ============ configurações do gráficos ============ #

    ax.scatter(x,y,z, c=point_colors)
    plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
    if has_arrows:
        ax.quiver(x,y,z, x_magnitudes, y_magnitudes, z_magnitudes, color=vector_colors, cmap=cmap, norm=norm)
    plt.show()