import math
from parachute_area import *


"""
\**

* @author Caio Bertolato Pereira
* @email bertolatopereiracaio@gmail.com
* @this defines the list of parachutes and their drag_coefficient

"""
parachute1 = Parachute('flat_Circular', 1.75 )
parachute2 = Parachute('conical', 1.83)
parachute3 = Parachute('hemispherical', 1,7)
parachute4 = Parachute('annular', 0,9)
parachute5 = Parachute('cross', 0,75)

parachutes = [parachute1, parachute2, parachute3, parachute4, parachute5]

parachutes_map = {
    'flat_Circular' : parachute1,
    'conical' : parachute2,
    'hemispherical' : parachute3,
    'annular' : parachute4,
    'cross' : parachute5
}

print(parachutes_map['conical'])

class drag_coefficient:
    def parachute_type(self, parachute_Name, drag_Coefficient):
        for item in self.parachutes:
            if item == parachute_Name:
                return drag_Coefficient