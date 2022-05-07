from core.physics.body.rigid_body import RigidBody
from core.physics.forces.translation_test_force import TranslationTestForce
from core.physics.forces.rotation_test_force import RotationTestForce
from core.physics.vector import Vector
from core.physics.body.application_point import ApplicationPoint
from rb_test.trajectory_test import trajectoryTest
from rb_test.velocity_test import velocityTest
import matplotlib.pyplot as plt
import matplotlib


rigid_body = RigidBody([], 2, None, 1, Vector(0,0,0), Vector(0,0,-1))

translation_force = TranslationTestForce(10,0,50,ApplicationPoint.CG)
rotation_force = RotationTestForce(0,0.1,0,ApplicationPoint.CP)

# trajectoryTest(rigid_body, [translation_force], 40)
# trajectoryTest(rigid_body, [translation_force, rotation_force], 40, arrow_scale=300)
# rbRotationTest(rigid_body, [rotation_force], 40)
# velocityTest(rigid_body, [translation_force, rotation_force], 40)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

x = [0, 0, 0]
y = [0, 0, 0]
z = [0, 0, 0]

x_dir = [-3, 0, 0]
y_dir = [-4, 4, -1]
z_dir = [-2, 2, 1]

color_vec1 = 200
color_vec2 = 100
color_vec3 = 50
vector_colors = [color_vec1, color_vec2, color_vec3]
colors = [0 for number in range(len(vector_colors)*3)]
for index, vector_color in enumerate(vector_colors):
    arrow_index = 3+index*2

    colors[index] = vector_color
    colors[arrow_index] = vector_color
    colors[arrow_index+1] = vector_color

norm=plt.Normalize(50,200)
cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", ["red","violet","blue"])
# colors = plt.cm.viridis(colors)
colors = norm(colors)
colors = cmap(colors)
print(colors)

ax.quiver(x,y,z,x_dir,y_dir,z_dir,color=colors,  # line1, line2, line3, l1arrow1, l1arrow2, l2arrow1, l2arrow2, l3arrow1, l3arrow2
arrow_length_ratio=0.3, cmap=cmap, norm=norm)
ax.set(ylim=(-5, 5), xlim=(-5, 5), zlim=(-5, 5))
plt.show()