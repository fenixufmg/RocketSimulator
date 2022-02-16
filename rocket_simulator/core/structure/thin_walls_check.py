"""
@author [diego]
@email [dmgp1302@gmail.com]
@create date 2022-02-11 17:58:45
@modify date 2022-02-11 18:37:03
""" 

def thin_walls_check (external_radius: float, internal_radius: float)->bool:
    '''thin_walls_check [summary]

    Args:
        external_radius (float): [description]
        internal_radius (float): [description]

    Returns:
        bool: returns if it is or it is not a thin walled vessel (motor). If it is not, all starter parameters must be recalculated
    '''    
    e = external_radius-internal_radius
    thin_walls_criteria = e/(2*external_radius)
    
    if thin_walls_criteria <= 0.1:
        return True
    else:
        return False