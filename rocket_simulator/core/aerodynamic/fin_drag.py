##/**
## * @author [author]
## * @email [example@mail.com]
## * @create date 2022-05-06 10:03:00
## * @modify date 2022-05-06 10:03:00
## * @desc [description]
## */

## condition: perpendicular air flow
def fin_drag_coeficient(mach_number: float) -> float:
    if(mach_number < 0.9):
        return pow((1 - (mach_number^2)), -0.417) - 1
    elif(mach_number < 1):
        return 1 - 1,785 * (mach_number - 0.9)