from cmath import sqrt
import cmath

class Parachute:
    def __init__(self, name, drag_coefficient):
        self.name = name
        self.drag_coefficient = drag_coefficient

    def getname(self):
        return self.name
    
    def getdrag_coefficient(self):
        return self.drag_coefficient
