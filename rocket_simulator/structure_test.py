from typing import List

from models.structure.parachute_model import ParachuteModel, EjectionCriteria
from simulation.airless_earth_ambient import AirlessEarthAmbient
from simulation.earth_ambient import EarthAmbient
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
from models.structure.transition_model import TransitionModel
from models.other.material_model import MaterialModel
from models.structure.cylindrical_body_model import CylindricalBodyModel
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib

from utils.cable_type import CableType
from utils.parachute_type import ParachuteType
from utils.utils import Utils
from models.structure.fin_model import FinModel
from models.structure.rocket_model import RocketParts


# def isOnLine(line: List[Vector], point: Vector):
#     a = (line[1].y() - line[0].y()) / (line[1].x() - line[0].x())
#     b = line[0].y() - a * line[0].x()
#     y = a * line[0].x() + b
#     y = float(str(f"{y:.4f}"))
#
#     y_point = float(str(f"{point.y():.4f}"))
#
#     return y == y_point


def geometryTest():
    fig = plt.figure(figsize=(8, 5))
    # ax = fig.add_subplot(111, projection='3d')
    ax = fig.gca(projection='3d')
    print()
    parts = rocket.getParts()
    for part in parts:
        delimitation_points = part.delimitation_points
        coords = [part.part_type]

        for delimitation in delimitation_points:
            coords.append(delimitation.toList())

        print(coords)
        print(f"    {part.part_type} cg: {part.cg}")
        print(f"    {part.part_type} cp: {part.cp}")

        ax.scatter(delimitation_points[0].x(), delimitation_points[0].y(), delimitation_points[0].z(), color="red")
        ax.scatter(delimitation_points[1].x(), delimitation_points[1].y(), delimitation_points[1].z(), color="red")
        ax.scatter(part.cg.x(), part.cg.y(), part.cg.z(), color="green")
        ax.scatter(part.cp.x(), part.cp.y(), part.cp.z(), color="lightgreen")

    print()
    print(f"Rocket CG: {rocket.cg}")
    print(f"Rocket CP: {rocket.cp}")

    # plt.show()


acrylic = MaterialModel("acrylic")
nose = NoseModel(2, 0.5, NoseType.PARABOLIC, 1, 0.2, acrylic, 0)
parachute = ParachuteModel(EjectionCriteria.APOGEE, ParachuteType.HEMISPHERICAL, CableType.POLYESTER, 5, nose)
# transition = TransitionModel(0.5, 2, 2, 0.5, acrylic, 1)
cylinder1 = CylindricalBodyModel(5, 2, 0.5, acrylic, 2)  # height 5
# cylinder2 = CylindricalBodyModel(4, 2, 0.5, acrylic, 3)  # height 4 , rocket_height = 10
fins = FinModel(1, 0.5, 1.5, 0.05, 0.3925, 0, 2, 4, acrylic, 4)

rocket = RocketModel()
rocket.addPart(parachute)
rocket.addPart(nose)
rocket.addPart(cylinder1)
# rocket.addPart(fins)
rotation = Vector(0, 0.1, 0)
# rocket.rotate(rotation)

# ambient = EarthAmbient()
ambient = AirlessEarthAmbient()
trajectoryTest(rocket, ambient, 10, arrow_scale=1, has_arrows=True, limit=20, additional_forces=[], step=0.5, debug=True)


# physicsTest()
# geometryTest()

# [<RocketParts.NOSE: 'nose'>, [0.0, 0.0, 6.2], [0.0, 0.0, 5.0]]
# RocketParts.NOSE cg: (0.0, 0.0, 5.4)
# RocketParts.NOSE cp: (0.0, 0.0, 5.6)
# [<RocketParts.CYLINDRICAL_BODY: 'cylidrical body'>, [0.0, 0.0, 5.0], [0.0, 0.0, 0.0]]
# RocketParts.CYLINDRICAL_BODY cg: (0.0, 0.0, 2.5)
# RocketParts.CYLINDRICAL_BODY cp: (0.0, 0.0, 2.5)
#
# Rocket CG: (0.0, 0.0, 2.9559848745936588)
# Rocket CP: (0.0, 0.0, 5.6000000000000005)


# CERTO VER SE QUANDO INFLA CALCULA CERTO
# Time: 0.0
# Velocity: (0, 0, 0)
# Acceleration: (0, 0, 0)
# Moment of inertia: None
# Angular velocity: (0, 0, 0)
# Angular acceleration: (0, 0, 0)
# Cg position: (0.0, 0.0, 2.9559848745936588)
# Cp position: (0.0, 0.0, 5.6000000000000005)
# cg->cp: (0.0, 0.0, 2.6440151254063418)
# cg->cp (mag): 2.6440151254063418
#
# Tip position: (0, 0, 6.2)
# Base position: (0.0, 0.0, 0.0)
# Tip->Base: (0.0, 0.0, -6.2)
# Tip->Base (mag): 6.2
#
# Is on ground: False
# Mass: 16.63497721664445
# ========================================

# ========================================
# Time: 10.0
# Velocity: (2.5104927011680913, 0.0, -13.198811920270028)
# Acceleration: (0.0, 0.0, -9.8)
# Moment of inertia: 146.94234560541
# Angular velocity: (0.0, 0.0, 0.0)
# Angular acceleration: (0.0, 0.0, 0.0)
# Cg position: (7.154904198329057, 0.0, -0.24828471648553566)
# Cp position: (7.482574578317383, 0.0, 3.0174894488923516)
# cg->cp: (0.3276703799883256, 0.0, 3.2657741653778873)
# cg->cp (mag): 3.2821713509765655
#
# Tip position: (7.477333263318525, 0.0, 2.9652511259884258)
# Base position: (6.8583660801081905, 0.0, -3.203774698735333)
# Tip->Base: (-0.6189671832103345, 0.0, -6.169025824723759)
# Tip->Base (mag): 6.199999999999999
#
# Is on ground: True
# Mass: 16.701914716644453
# ========================================
#
# Process finished with exit code 0
