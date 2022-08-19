##/**
## * @author [alexlb7]
## * @email [alexandrelb.700@gmail.com]
## * @create date 2022-05-06 09:20:26
## * @modify date 2022-05-06 09:20:26
## * @desc Returns the base drag coefficient
## */

def base_drag_coefficient(mach_number: float) -> float:

    if (mach_number < 1):
        return 0.12 + 0.13*pow((mach_number), 2)
    
    else:
        pass



