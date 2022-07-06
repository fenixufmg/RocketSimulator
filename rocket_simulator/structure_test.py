from core.physics.body.rigid_body import RigidBody
from core.physics.forces.translation_test_force import TranslationTestForce
from core.physics.forces.rotation_test_force import RotationTestForce
from core.physics.vector import Vector
from core.physics.body.application_point import ApplicationPoint
from models.structure.rocket_model import RocketModel

from rb_test.trajectory_test import trajectoryTest
from rb_test.velocity_test import velocityTest
from rb_test.angular_velocity_test import angularVelocityTest

from core.physics.forces.weight_force import WeightForce
from rb_test.acceleration_test import accelerationTest
from models.structure.nose_model import NoseModel
from models.structure.nose_model import NoseType
from models.other.material_model import MaterialModel
from models.structure.cylindrical_body_model import CylindricalBodyModel
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib


def geometryTest():
    fig = plt.figure(figsize=(8,5))
    # ax = fig.add_subplot(111, projection='3d')
    ax = fig.gca(projection='3d')

    parts = rocket.getParts()
    for part in parts:
        delimitation_points = part.delimitation_points
        coords = [part.part_type]
        for delimitation in delimitation_points:
            coords.append(delimitation.toList())

        print(coords)

        ax.scatter(delimitation_points[0].x(), delimitation_points[0].y(), delimitation_points[0].z(), color="red")
        ax.scatter(delimitation_points[1].x(), delimitation_points[1].y(), delimitation_points[1].z(), color="blue")

    plt.show()


def physicsTest():
    weight = WeightForce()
    thrust_test = TranslationTestForce(130, 0, 600)
    # trajectoryTest(rocket, [weight, thrust_test], 100, arrow_scale=400, has_arrows=True)
    trajectoryTest(rocket, [weight, thrust_test], 100, arrow_scale=400, has_arrows=True)


acrylic = MaterialModel("acrylic")
nose = NoseModel(2, 0.5, NoseType.PARABOLIC, 1, acrylic, 0) # height 1
cylinder1 = CylindricalBodyModel(5, 2, 0.5, acrylic, 1) # height 5
cylinder2 = CylindricalBodyModel(4, 2, 0.5, acrylic, 2) # height 4 , rocket_height = 10

rocket = RocketModel()
rocket.addPart(nose)
rocket.addPart(cylinder1)
rocket.addPart(cylinder2)

physicsTest()
# geometryTest()

