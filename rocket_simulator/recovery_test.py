from core.physics.body.rigid_body import RigidBody
from core.physics.forces.translation_test_force import TranslationTestForce
from core.physics.forces.rotation_test_force import RotationTestForce
from core.physics.vector import Vector
from core.physics.body.application_point import ApplicationPoint
from rb_test.trajectory_test import trajectoryTest
from rb_test.velocity_test import velocityTest
from rb_test.angular_velocity_test import angularVelocityTest

from core.physics.forces.weight_force import WeightForce
from rb_test.acceleration_test import accelerationTest

rigid_body = RigidBody([Vector(0,0,2), Vector(0,0,-2)], 2, None, 1, Vector(0,0,0) ,Vector(0,0,-1))

translation_force = TranslationTestForce(10,0,50,ApplicationPoint.CG)
weight = WeightForce()
rotation_force = RotationTestForce(0,0.1,0,ApplicationPoint.CP)
# rotation_force = RotationTestForce(0,0.1,0,ApplicationPoint.CUSTOM, cg_offset=2.1)

trajectoryTest(rigid_body, [translation_force, rotation_force, weight], 40, arrow_scale=400, has_arrows=True)
# velocityTest(rigid_body ,[translation_force, rotation_force, weight], 40, axis=Vector(0,0,1))
# accelerationTest(rigid_body ,[translation_force, rotation_force, weight], 40, axis=Vector(0,0,1))
# angularVelocityTest(rigid_body,[translation_force, rotation_force, weight], 40, axis=Vector(1,0,0))