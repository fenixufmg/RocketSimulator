##/**
## * @author [alexlb7]
## * @email [alexandrelb.700@gmail.com]
## * @create date 2022-05-06 09:52:00
## * @modify date 2022-05-06 09:52:00
## * @desc returns the pressure drag coefficient for the boattail
## */

def boattail_pressure_drag_coeficent(front_diameter: float, end_diameter: float, length:float, 
                                    base_coefficient:float, front_area: float, base_area: float) -> float:
    
    d = length / (front_diameter - end_diameter)
    result = (base_area / front_area) * base_coefficient

    if (d < 1):
        multiply = 1
    elif (d < 3):
        multiply = (3 - d) / 2
    elif (d > 3):
        multiply = 0
    
    return result * multiply
