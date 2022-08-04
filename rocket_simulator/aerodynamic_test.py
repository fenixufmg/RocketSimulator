from core.physics.body.rigid_body import RigidBody
from core.physics.forces.translation_test_force import TranslationTestForce
from core.physics.forces.rotation_test_force import RotationTestForce
from core.physics.vector import Vector
from core.physics.body.application_point import ApplicationPoint
from models.other.material_model import MaterialModel
from models.structure.nose_model import NoseModel, NoseType
from models.structure.cylindrical_body_model import CylindricalBodyModel
from models.structure.fin_model import FinModel
from models.structure.rocket_model import RocketModel
from rb_test.trajectory_test import trajectoryTest
from rb_test.velocity_test import velocityTest
from rb_test.angular_velocity_test import angularVelocityTest
from core.physics.forces.drag_force import DragForce
from core.physics.forces.thrust_test import ThrustTest

from core.physics.forces.weight_force import WeightForce
from rb_test.acceleration_test import accelerationTest
from core.physics.forces.impulse_test_force import ImpulseTestForce

def inertia_test(x):
    return 1

rocket = RocketModel()

acrylic = MaterialModel("acrylic")
nose = NoseModel(2, 0.5, NoseType.PARABOLIC, 1, acrylic, 0)
cylindrical_body = CylindricalBodyModel(5, 2, 0.5, acrylic, 1)

rocket.addPart(nose)
rocket.addPart(cylindrical_body)
# cg -> cp = 2.666
# mass = 15.89
# rotation = Vector(0, 0.5 ,0)
rotation = Vector(0, 0.2 ,0)
rocket.rotate(rotation)


# rocket.delimitation_points = [Vector(0, 0, 2), Vector(0, 0, -2)]
# rocket.mass = 2
# rocket.volume = None
# rocket.moment_of_inertia_function = inertia_test
# rocket.cg = Vector(0, 0, 0)
# rocket.cp = Vector(0, 0, -1)

weight = WeightForce()
dragForce = DragForce()
# thrust_test = TranslationTestForce(400, 0, 1500)
# thrust_test = TranslationTestForce(0, 0, 2000)
thrust_test = ImpulseTestForce(200)
rotation_force = RotationTestForce(0,1,0,ApplicationPoint.CP)

trajectoryTest(rocket, [thrust_test, weight, dragForce], 30, arrow_scale=1, has_arrows=True, limit=20)
# velocityTest(rocket, [thrust_test, weight, dragForce], 30, axis=Vector(1,0,0))
# accelerationTest(rocket ,[thrust_test, weight, dragForce], 50, axis=Vector(1,0,0))
# angularVelocityTest(rocket,[translation_force, rotation_force, weight], 40, axis=Vector(1,0,0))


    