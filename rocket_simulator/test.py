
from core.physics.physics import Physics
from models.physics.forces.test_force import TestForce
from models.physics.rigid_body import RigidBody
import matplotlib.pyplot as plt
from models.physics.application_point import ApplicationPoint

test_force = TestForce(2,0,0,ApplicationPoint.CG)
rigid_body = RigidBody([], None)

physics = Physics(rigid_body)
physics.addForce(test_force)
simulations = physics.simulate(10)

x = []
y = []
for time, simulation in simulations.items():
    x.append(simulation.time)
    y.append(simulation.velocity.toString())

print(y)


