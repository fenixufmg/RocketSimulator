from core.physics.vector import Vector
from models.other.material_model import MaterialModel
from models.structure.motor_model import MotorModel
from models.structure.nose_model import NoseModel, NoseType
from models.structure.cylindrical_body_model import CylindricalBodyModel
from models.structure.fin_model import FinModel
from models.structure.parachute_model import ParachuteModel, EjectionCriteria
from models.structure.rocket_model import RocketModel
from models.structure.transition_model import TransitionModel
from rb_test.trajectory_test import trajectoryTest
from simulation.airless_earth_ambient import AirlessEarthAmbient
from utils.cable_type import CableType
from utils.parachute_type import ParachuteType
from utils.wind_direction import WindDirection
from simulation.earth_ambient import EarthAmbient

rocket = RocketModel()

acrylic = MaterialModel("acrylic")
nose = NoseModel(4, 0.5, NoseType.CONICAL, 1, 0.2, acrylic, 0)
parachute = ParachuteModel(EjectionCriteria.APOGEE, ParachuteType.HEMISPHERICAL, CableType.POLYESTER, 8, nose, inflation_randomness_factor=0)
cylinder1 = CylindricalBodyModel(5, 4, 0.5, acrylic, 1)
transition = TransitionModel(5, 8, 4, 0.5, 4, acrylic, 2)
cylinder2 = CylindricalBodyModel(5, 8, 0.5, acrylic, 3)

motor = MotorModel(0.5, 2, 0.25, acrylic, 2)
# fins = FinModel(1, 0.5, 1.5, 0.05, 0.3925, 0, 4, 4, acrylic, 3)

rocket.addPart(nose)
rocket.addPart(cylinder1)
#rocket.addPart(transition)
#rocket.addPart(cylinder2)
# rocket.addPart(fins)
# rocket.addPart(parachute)
rocket.addPart(motor)

rotation = Vector(0, 0.2, 0)
rocket.rotate(rotation)

# thrust_test = ImpulseTestForce(100)
#rotation_force = RotationTestForce(0, 50, 0, ApplicationPoint.CP)
# normalForce = NormalForce()

ambient = EarthAmbient(0, WindDirection.N)
# ambient = AirlessEarthAmbient()

# pitch = PitchDampingMoment()

trajectoryTest(rocket, ambient, 20, arrow_scale=1, has_arrows=True, limit=20, additional_forces=[], step=0.5, debug=True)
#trajectoryTest(rocket, ambient, 10, arrow_scale=1, has_arrows=True, limit=20, additional_forces=[normalForce], step=0.2, debug=True)
#trajectoryTest(rocket, ambient, 10, arrow_scale=1, has_arrows=True, limit=20, additional_forces=[], step=0.2, debug=False)
# velocityTest(rocket, [thrust_test, weight, dragForce], 30, axis=Vector(1,0,0))
# accelerationTest(rocket ,[thrust_test, weight, dragForce], 50, axis=Vector(1,0,0))
#angularVelocityTest(rocket,[translation_force, rotation_force, weight], 40, axis=Vector(1,0,0))