
from core.physics.physics import Physics
from core.physics.forces.test_force import TestForce
from core.physics.body.rigid_body import RigidBody
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from core.physics.body.application_point import ApplicationPoint
import decimal
from core.physics.vector import Vector
import numpy as np

def rotationTest():
    pi = 3.14
    test_vector = Vector(1,0,0)
    rotated_vector = Vector.rotateAroundZAxis(test_vector, 2*pi)
    rotated_vector = Vector.rotateAroundXAxis(rotated_vector, 2*pi)

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
    ax.scatter(rotated_vector.x(), rotated_vector.y(), rotated_vector.z(), color="red")
    plt.show()

def threeDTest():
    x = []
    y = []
    z = []
    for time, simulation in simulations.items():
        x.append(simulation.position.x()) 
        y.append(simulation.position.y()) 
        z.append(simulation.position.z())

    print(x)
    print(y)
    print(z)
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.plot3D(x,y,z)
    plt.show()

test_force = TestForce(4,4,0,ApplicationPoint.CG)
rigid_body = RigidBody([], None)

physics = Physics(rigid_body)
physics.addForce(test_force)
simulations = physics.simulate(20)

# rotationTest()
v1 = [1,2,3]
v2 = [0,1,0]
v3 = [0,0,1]
result = np.matrix([v1,v2,v3]).transpose()
print(result)
print(result[0])


