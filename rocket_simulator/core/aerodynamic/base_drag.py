##/**
## * @author [author]
## * @email [example@mail.com]
## * @create date 2022-05-06 09:20:26
## * @modify date 2022-05-06 09:20:26
## * @desc [description]
## */
 
##import mach_number
import math

def base_drag(mach_number: float) -> float:
    if(mach_number<1):
        return 0.12 + 0.13*pow((mach_number), 2)


