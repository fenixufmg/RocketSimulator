from math import pi

"""

* @author Caio Bertolato Pereira
* @email bertolatopereiracaio@gmail.com
* @desc returns the total drag force created by the parachute
"""

def drag_Force(drag_coefficient:float, theta:float, payload_Speed:float, parachute_Area:float) ->float:
    return (drag_coefficient*theta*payload_Speed^2*parachute_Area)/2