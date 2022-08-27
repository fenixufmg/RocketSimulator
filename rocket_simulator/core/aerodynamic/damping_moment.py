"""
/**
 * @author João Lucas Gomes Alencar
 * @email alencarj2021@mail.com
 * @create date 2022-08-27 11:19:00
 * @modify date 2022-08-27 13:22:46
 * @desc returns the damping coefficient wich reduces the normal forces
 */
 """

def damping_moment(cylinder_length, average_radius, angular_velocity, reference_area, ) -> float:
    '''This value is computed separately for the portions of the rocket body fore
        and aft of the CG using an average body radius as rt'''
    reference_area = 2 * average_radius * cylinder_length 
    