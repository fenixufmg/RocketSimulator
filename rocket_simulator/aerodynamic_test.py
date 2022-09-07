from core.physics.forces.translation_test_force import TranslationTestForce
from core.physics.forces.rotation_test_force import RotationTestForce
from core.physics.vector import Vector
from core.physics.body.application_point import ApplicationPoint
from models.other.material_model import MaterialModel
from models.structure.motor_model import MotorModel
from models.structure.nose_model import NoseModel, NoseType
from models.structure.cylindrical_body_model import CylindricalBodyModel
from models.structure.fin_model import FinModel
from models.structure.rocket_model import RocketModel
from models.structure.transition_model import TransitionModel
from rb_test.trajectory_test import trajectoryTest
from rb_test.velocity_test import velocityTest
from rb_test.angular_velocity_test import angularVelocityTest
from core.physics.forces.drag_force import DragForce
from core.physics.forces.thrust_test import ThrustTest
from core.physics.forces.normal_force import NormalForce
from core.physics.forces.pitch_damping_moment import PitchDampingMoment

from core.physics.forces.weight_force import WeightForce
from rb_test.acceleration_test import accelerationTest
from core.physics.forces.impulse_test_force import ImpulseTestForce
from utils.wind_direction import WindDirection
from simulation.airless_earth_ambient import AirlessEarthAmbient
from simulation.earth_ambient import EarthAmbient

rocket = RocketModel()

acrylic = MaterialModel("acrylic")
nose = NoseModel(4, 0.5, NoseType.CONICAL, 1, 0.2, acrylic, 0)  
cylinder1 = CylindricalBodyModel(5, 4, 0.5, acrylic, 1)
transition = TransitionModel(5, 8, 4, 0.5, 4, acrylic, 2)
cylinder2 = CylindricalBodyModel(5, 8, 0.5, acrylic, 3)

# motor = MotorModel(0.5, 2, 0.25, acrylic, 2)
fins = FinModel(1, 0.5, 1.5, 0.05, 0.3925, 0, 4, 4, acrylic, 3)

rocket.addPart(nose)
#rocket.addPart(cylinder1)
#rocket.addPart(transition)
#rocket.addPart(cylinder2)
#rocket.addPart(fins)
# cg -> cp = 2.666
# mass = 15.89
# rotation = Vector(0, 0.5 ,0)
rotation = Vector(0, 0.2, 0) #Consertar
#rocket.rotate(rotation)


thrust_test = ImpulseTestForce(100)
#rotation_force = RotationTestForce(0, 50, 0, ApplicationPoint.CP)
normalForce = NormalForce()

ambient = EarthAmbient(0, WindDirection.N)
#ambient = AirlessEarthAmbient()

pitch = PitchDampingMoment()

trajectoryTest(rocket, ambient, 1, arrow_scale=1, has_arrows=True, limit=20, additional_forces=[], step=1, debug=False)
#trajectoryTest(rocket, ambient, 10, arrow_scale=1, has_arrows=True, limit=20, additional_forces=[normalForce], step=0.2, debug=True)
#trajectoryTest(rocket, ambient, 10, arrow_scale=1, has_arrows=True, limit=20, additional_forces=[], step=0.2, debug=False)
# velocityTest(rocket, [thrust_test, weight, dragForce], 30, axis=Vector(1,0,0))
# accelerationTest(rocket ,[thrust_test, weight, dragForce], 50, axis=Vector(1,0,0))
#angularVelocityTest(rocket,[translation_force, rotation_force, weight], 40, axis=Vector(1,0,0))

# ambient = EarthAmbient(rocket)
# simulations = ambient.simulate(30)



    