##/**
## * @author [author]
## * @email [example@mail.com]
## * @create date 2022-05-06 09:52:00
## * @modify date 2022-05-06 09:52:00
## * @desc [description]
## */

def estag_pressure_drag_coeficient(mach_number: float) -> float:
    
    if(mach_number<1):
        division = 1 + ((mach_number^2) / 4) + ((mach_number^4) / 40)
    
    ## division is the pressure / estag_pressure

    return 0.85 * division