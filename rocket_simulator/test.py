
from tkinter import Y
from core.physics.physics import Simulation
from core.physics.forces.test_force import TestForce
from core.physics.body.rigid_body import RigidBody
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from core.physics.body.application_point import ApplicationPoint
import decimal
from core.physics.vector import Vector
import numpy as np

from core.physics.forces.weight_force import WeightForce

def rotationTest():
    pi = 3.14
    test_vector = Vector(1,1,0)
    axis = Vector(1,0,0)
    rotated_vector = Vector.rotateAroundAxis(test_vector, axis, pi/6)

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(0,0,0, color="green")
    ax.scatter(1,0,0, color="green")
    ax.scatter(-1,0,0, color="green")
    ax.scatter(0,1,0, color="green")
    ax.scatter(0,-1,0, color="green")
    ax.scatter(0,0,1, color="green")
    ax.scatter(0,0,-1, color="green")

    ax.scatter(test_vector.x(), test_vector.y(), test_vector.z(), color="blue")
    ax.scatter(axis.x(), axis.y(), axis.z(), color="green")
    ax.scatter(rotated_vector.x(), rotated_vector.y(), rotated_vector.z(), color="red")
    plt.show()

def rbRotationTest():
    # rotation_test_force = RotationTestForce(1,1,0, ApplicationPoint.CUSTOM, cg_offset=0)
    # rotation_test_force = RotationTestForce(1,1,0, ApplicationPoint.CP)
    # rotation_test_force = RotationTestForce(1,1,0, ApplicationPoint.CUSTOM, cg_offset=-rigid_body.getCpCgDistance().magnitude())
    rotation_test_force = RotationTestForce(1,1,0, ApplicationPoint.CP)
    pi = 3.14

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(0,0,0, color="green")
    ax.scatter(1,0,0, color="green")
    ax.scatter(-1,0,0, color="green")
    ax.scatter(0,1,0, color="green")
    ax.scatter(0,-1,0, color="green")
    ax.scatter(0,0,1, color="green")
    ax.scatter(0,0,-1, color="green")

    rigid_body.test()
    print(rigid_body.getCpCgDistance().magnitude())

    x = rigid_body.cg().x()
    y = rigid_body.cg().y()
    z = rigid_body.cg().z()
    ax.scatter(x, y, z, color="red")

    x = rigid_body.cp().x()
    y = rigid_body.cp().y()
    z = rigid_body.cp().z()
    # print(rigid_body.cp().toList())

    ax.scatter(x, y, z, color="blue")

    print(rigid_body.getLookingDirection().toList())
    rigid_body.applyForce(rotation_test_force, 1)
    print(rigid_body.getLookingDirection().toList())
    looking_direction = rigid_body.getLookingDirection()

    x = rigid_body.cp().x()
    y = rigid_body.cp().y()
    z = rigid_body.cp().z()
    # print(rigid_body.cp().toList())

    print(rigid_body.getCpCgDistance().magnitude())
    ax.scatter(x, y, z, color="blue")

    x = rigid_body.cg().x()
    y = rigid_body.cg().y()
    z = rigid_body.cg().z()
    ax.scatter(x, y, z, color="red")

    x = looking_direction.x()
    y = looking_direction.y()
    z = looking_direction.z()
    ax.scatter(x, y, z, color="orange")

    plt.show()

def threeDTest():
    test_force = TestForce(4,4,0,ApplicationPoint.CG)
    simulation = Simulation(rigid_body)
    simulation.addForce(test_force)
    simulations = simulation.simulate(20)

    x = []
    y = []
    z = []
    for time, simulation in simulations.items():
        print(time)
        print(f"v = {simulation.velocity.magnitude()}")
        print(f"s = {simulation.position.magnitude()}")
        x.append(simulation.position.x()) 
        y.append(simulation.position.y()) 
        z.append(simulation.position.z())

    # print(x)
    # print(y)
    # print(z)
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.plot3D(x,y,z)
    plt.show()

def trajectoryTest():
    test_force = TestForce(10,0,50,ApplicationPoint.CG)
    weight = WeightForce()

    simulation = Simulation(rigid_body)
    simulation.addForce(test_force)
    simulation.addForce(weight)
    simulations = simulation.simulate(40)

    x = []
    y = []
    z = []
    for time, simulation in simulations.items():
        print(time)
        print(f"v = {simulation.velocity.magnitude()}")
        print(f"s = {simulation.position.magnitude()}")
        x.append(simulation.position.x()) 
        y.append(simulation.position.y()) 
        z.append(simulation.position.z())

    # print(x)
    # print(y)
    # print(z)
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.set_xlim(0, 5000)
    ax.set_ylim(-2500, 2500)
    ax.set_zlim(0, 5000)
    ax.plot3D(x,y,z)
    # ax.quiver() # plotar setas
    plt.show()

rigid_body = RigidBody([], 2, None, 1, Vector(0,0,0), Vector(0,0,-1))

# threeDTest()
# trajectoryTest()
# rbRotationTest()
# rotationTest()
# decimal.getcontext().prec = 4




