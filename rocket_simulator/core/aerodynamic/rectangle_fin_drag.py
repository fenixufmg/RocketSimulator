##/**
## * @author [alexlb7]
## * @email [alexandrelb.700@gmail.com]
## * @create date 2022-05-06 10:10:00
## * @modify date 2022-05-06 09:10:00
## * @desc [description]
## */

import estag_pressure_drag

#condition: perpendicular air flow
def rectangle_fin_drag_coeficient(mach_number) -> float:
    #condition: sub-sonic
    return estag_pressure_drag.estag_pressure_drag_coeficient(mach_number)