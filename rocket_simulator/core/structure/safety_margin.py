def safety_margin(von_Mises_stress:float,yield_stress:float)->float:
    return yield_stress/von_Mises_stress