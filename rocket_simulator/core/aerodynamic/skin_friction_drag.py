"""
/**
 * @author João Lucas Gomes Alencar
 * @email alencarj2021@mail.com
 * @create date 2022-02-24 14:41:35
 * @modify date 2022-02-24 14:41:35
 * @desc Returns adjusted skin friction drag as functioin of mach number
 */
 """

from numpy import log as ln

def skin_friction_drag(reynolds_number: float, critical_reynolds_number: float, 
                        material_roughness: float, rocket_length: float, 
                        mach_number: float) -> float:

    if reynolds_number <= 10000:
        cf = 0.0148 #cf: Initial skin drag coefficient 

    elif 10000 < reynolds_number < critical_reynolds_number:
        cf = 1 / (1.5 * ln(reynolds_number) - 5.6) ** 2
    
    elif reynolds_number > critical_reynolds_number:
        cf = 0.032 * (material_roughness / rocket_length) ** 0.2
    
    else:
        print('ERRO:O veículo está SUPERSÔNICO. Impossível de calcular')
        cf = 0

    #adjust skin friction drag coefficient according to the mach number
    adjust_cf = cf * (1 - 0.1 * mach_number ** 2)
    return adjust_cf