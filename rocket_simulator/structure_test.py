from typing import List
from utils.wind_direction import WindDirection
from models.structure.motor_model import MotorModel
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
nose = NoseModel(2, 0.5, NoseType.PARABOLIC, 1, 0.2, acrylic, 0) # height 1.2
cylinder1 = CylindricalBodyModel(5, 2, 0.5, acrylic, 1)  # height 5
transition = TransitionModel(0.5, 2, 2, 0.5, 2, acrylic, 2) # concertar argumento nose diameter
parachute = ParachuteModel(EjectionCriteria.APOGEE, ParachuteType.HEMISPHERICAL, CableType.POLYESTER, 5, nose, inflation_randomness_factor=0)
cylinder2 = CylindricalBodyModel(4, 2, 0.5, acrylic, 3)  # height 4 , rocket_height = 10
motor = MotorModel(0.5, 2, 0.25, acrylic, 4)
fins = FinModel(1, 0.1, 1.5, 1, 0.3925, 0, 2, 4, acrylic, 5)

rocket = RocketModel()
rocket.addPart(parachute)  # fazer torque de excentricidade
rocket.addPart(nose)
rocket.addPart(cylinder1)
# rocket.addPart(transition)
rocket.addPart(cylinder2)
# rocket.addPart(fins)
# rocket.addPart(motor)
rotation = Vector(0, 0.1, 0)
rocket.rotate(rotation)

ambient = EarthAmbient(0.7, WindDirection.NO)
print(rocket.getPart(RocketParts.CYLINDRICAL_BODY))
# ambient = EarthAmbient(0, WindDirection.N)
# ambient = AirlessEarthAmbient()
# print("updating")
# rocket.updateState()
trajectoryTest(rocket, ambient, 10, arrow_scale=1, has_arrows=True, limit=20, additional_forces=[], step=0.2, debug=True)
# velocityTest(rocket, ambient, 10, axis=Vector(0,0,1))

# velocidade terminal paraquedas = -3.08

# physicsTest()
# geometryTest()

