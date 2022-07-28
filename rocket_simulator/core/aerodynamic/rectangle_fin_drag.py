##/**
## * @author [alexlb7]
## * @email [alexandrelb.700@gmail.com]
## * @create date 2022-05-06 10:10:00
## * @modify date 2022-05-06 09:10:00
## * @desc [description]
## */

from stag_pressure_drag import stag_pressure_drag_coeficient

#condition: perpendicular air flow
def rectangle_fin_drag_coeficient(mach_number) -> float:
    #condition: sub-sonic
    return stag_pressure_drag_coeficient(mach_number)