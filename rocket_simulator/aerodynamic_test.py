from core.physics.body.rigid_body import RigidBody
from core.physics.forces.translation_test_force import TranslationTestForce
from core.physics.forces.rotation_test_force import RotationTestForce
from core.physics.vector import Vector
from core.physics.body.application_point import ApplicationPoint
from rb_test.trajectory_test import trajectoryTest
from rb_test.velocity_test import velocityTest


rigid_body = RigidBody([], 2, None, 1, Vector(0,0,0), Vector(0,0,-1))

translation_force = TranslationTestForce(10,0,50,ApplicationPoint.CG)
rotation_force = RotationTestForce(5,0,0,ApplicationPoint.CP)

# trajectoryTest(rigid_body, [translation_force], 40)
trajectoryTest(rigid_body, [translation_force, rotation_force], 40, arrow_scale=300)
# velocityTest(rigid_body, [translation_force, rotation_force], 40)