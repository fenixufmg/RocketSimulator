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
from models.structure.nose_model import NoseModel
from models.structure.nose_model import NoseType
from models.other.material_model import MaterialModel
from models.structure.cylindrical_body_model import CylindricalBodyModel

acrylic = MaterialModel("acrylic")
nose = NoseModel(2, 0.5, NoseType.PARABOLIC, 1, acrylic, 0)
cylinder1 = CylindricalBodyModel(10, 2, 0.5, acrylic, 1)