from math import sin, radians

def nose_pressure_drag(bodynoseAngle: float) -> float:
    if 0 <= bodynoseAngle <= 360:
     return 0.8*sin(radians(bodynoseAngle))
    elif bodynoseAngle > 360:
     return 0.8*sin(radians(bodynoseAngle%360))

#Angle between body and cilindricbody is in degrees
    