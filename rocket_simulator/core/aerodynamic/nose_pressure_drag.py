from math import sin, radians

"""
/**
 * @author João Lucas Gomes Alencar
 * @email alencarj2021@mail.com
 * @create date 2022-04-09 14:36:50
 * @modify date 2022-06-10 22:46:57
 * @desc If the transition batween the body of the rocket and the nose is smooth, 
the nose pressure drag coefficient is equal to zero. But if the transition has a conical shape,
"bodynoseAngle" in the angle between the coincident line over the ciclindrical body component under
the nose and the suface of the conical shape.
 */
 """

def nose_pressure_drag(bodynoseAngle: float):
    return 0.8 * (sin(radians(bodynoseAngle))) ** 2 #Angle between body and cilindricbody is in degrees

