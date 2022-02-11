def thin_walls_check (external_radius: float, internal_radius: float)->bool:
    
    e = external_radius-internal_radius
    thin_walls_criteria = e/(2*external_radius)
    
    if thin_walls_criteria <= 0.1:
        return True
    else:
        return False