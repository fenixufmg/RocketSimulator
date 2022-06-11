from math import sin, radians

"""
/**
 * @author João Lucas Gomes Alencar
 * @email alencarj2021@mail.com
 * @create date 2022-04-09 14:36:50
 * @modify date 2022-06-10 23:39:48
 * @desc If the transition batween the body of the rocket and the shoulder is smooth, 
the nose pressure drag coefficient is equal to zero. But if the transition has a conical shape,
"bodynoseAngle" in the angle between the coincident line over the ciclindrical body component under
the shoulder and the suface of the conical shape.
 */
 """

def shoulder_pressure_drag(transition: str, bodynoseAngle: float):

    if transition == "smooth":
        return 0
    else:
        return 0.8 * (sin(radians(bodynoseAngle))) ** 2

#Angle between body and cilindricbody is in degrees

def shoulder_pressure_drag_reference_area(Abase, Atop):
    """
    Args:
        Abase: Area of the base of the body
        Atop: Area of the top of the body
    Returns:
        ArefS: Reference area of the shoulder
    """

    return abs(Abase - Atop) 
