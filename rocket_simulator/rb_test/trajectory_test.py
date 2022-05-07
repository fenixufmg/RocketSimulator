# Não editar
from core.physics.forces.weight_force import WeightForce
from core.physics.body.rigid_body import RigidBody
import matplotlib.pyplot as plt
import matplotlib
from core.physics.physics import Simulation
import numpy as np

def trajectoryTest(rigid_body:RigidBody, forces:list, simulation_time:int, arrow_scale=150):
    weight = WeightForce()
    simulation = Simulation(rigid_body)
    for force in forces:
        simulation.addForce(force)
    simulation.addForce(weight)
    simulations = simulation.simulate(simulation_time)

    x = []
    y = []
    z = []
    x_magnitudes = []
    y_magnitudes = []
    z_magnitudes = []

    velocities = []
    for time, simulation in simulations.items():
        # print(time)
        # print(f"v = {simulation.velocity.magnitude()}")
        # print(f"s = {simulation.cg.magnitude()}")
        velocities.append(simulation.velocity.magnitude())
        x.append(simulation.cg.x()) 
        y.append(simulation.cg.y()) 
        z.append(simulation.cg.z())
        # print(simulation.angular_velocity.magnitude())
        looking_direction = simulation.looking_direction * arrow_scale

        x_magnitudes.append(looking_direction.x())
        y_magnitudes.append(looking_direction.y())
        z_magnitudes.append(looking_direction.z())
        
    fig = plt.figure(figsize=(8,5))
    ax = fig.add_subplot(projection='3d')

    # ============ configurações do gráficos ============ #
    ax.set_xlim(0, 5000)
    ax.set_ylim(-2500, 2500)
    ax.set_zlim(0, 5000)
    min_velocity = min(velocities)
    max_velocity = max(velocities)

    colors = []
    last_velocity = 0
    for velocity in velocities:
        rgb = [0,255,0]
        red_value = int((256*velocity/max_velocity)) - 1
        green_value = 255 - red_value

        if velocity > last_velocity: # velocidade crescendo
            rgb = [red_value, green_value, rgb[2],1]

        elif velocity < last_velocity: # velocidade diminuindo
            rgb = [red_value, green_value, rgb[2],1]

        last_velocity = velocity
        rgb = [rgb[0]/255, rgb[1]/255, rgb[2]/255,1]

        colors.append(rgb)
        # colors.append(rgb)
        # colors.append(rgb)
    # ============ configurações do gráficos ============ #

    # ax.plot3D(x,y,z)
    ax.scatter(x,y,z, c=colors)
    plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
    # ax.quiver(x,y,z, x_magnitudes, y_magnitudes, z_magnitudes)
    
    normalizer = matplotlib.colors.Normalize(vmin=0, vmax=255)
    # pcm = ax.pcolormesh(x, y, z, vmin=0, vmax=1, cmap='PuBu_r')
    # print(pcm(colors))
    # viridis = matplotlib.cm.get_cmap("viridis", 12)
    # print(viridis(colors))

    ax.quiver(x,y,z, x_magnitudes, y_magnitudes, z_magnitudes)
    plt.show()