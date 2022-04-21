
from core.physics.physics import Physics
from core.physics.forces.test_force import TestForce
from core.physics.body.rigid_body import RigidBody
import matplotlib.pyplot as plt
from core.physics.body.application_point import ApplicationPoint
import decimal

test_force = TestForce(4,4,0,ApplicationPoint.CG)
rigid_body = RigidBody([], None)

physics = Physics(rigid_body)
physics.addForce(test_force)
simulations = physics.simulate(15)

x = []
y = []
for time, simulation in simulations.items():
    x.append(simulation.time)
    y.append(simulation.position.magnitude())

print("========================================================")
print(y)
plt.plot(x, y)
plt.show()


