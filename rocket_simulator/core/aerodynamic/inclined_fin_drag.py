##/**
## * @author [alexlb7]
## * @email [alexandrelb.700@gmail.com]
## * @create date 2022-05-06 10:19:00
## * @modify date 2022-05-06 10:19:00
## * @desc [description]
## */

from cmath import cos
import circular_fin_drag
import rectangle_fin_drag

def inclined_fin_drag_coeficient(mach_number: float, LE_angle: float, fin_type: str) -> float:
    if( fin_type == 'c'):
        return circular_fin_drag(mach_number) * pow(cos(LE_angle), 2)
    elif( fin_type == 'r'):
        return rectangle_fin_drag(mach_number) * pow(cos(LE_angle), 2) 
