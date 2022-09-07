from asyncio import constants
import imp
from core.physics.forces.force import Force
from core.physics.delta_time_simulation import DeltaTimeSimulation
from core.physics.body.application_point import ApplicationPoint
from core.physics.vector import Vector
from models.structure.rocket_model import RocketModel
from utils.rocket_parts import RocketParts
from utils.nose_type import NoseType
from ...aerodynamic.boattail_pressure_drag import boattail_pressure_drag_coeficent
from utils.constants import Constants
from models.structure.nose_model import NoseModel
from models.structure.fin_model import FinModel
from core.aerodynamic.reynolds_number import reynolds_number
from core.aerodynamic.mach_number import mach_number
from core.aerodynamic.mean_aerodynamic_chord import mean_aerodynamic_chord_length
from core.aerodynamic.rocket_fineness_ratio import rocket_fineness_ratio
from core.aerodynamic.critical_reynolds_number import critical_reynolds_number
from core.aerodynamic.stag_pressure_drag import stag_pressure_drag_coeficient
from core.aerodynamic.fin_drag import fin_drag_coeficient
from core.aerodynamic.skin_friction_drag import skin_friction_drag
from core.aerodynamic.total_skin_friction_drag_coefficient import total_skin_friction_drag_coefficient 
from core.aerodynamic.base_drag import base_drag_coefficient
from core.aerodynamic.nose_pressure_drag import nose_pressure_drag
from math import pi, atan, degrees, cos

class DragForce(Force):
    def __init__(self):
        super().__init__(0, 0, 0, ApplicationPoint.CP, None)
        self.__drag_coefficient = None

    def __referenceArea(self, current_state: DeltaTimeSimulation) -> float:
        parts = current_state.parts
        #pegar como área de referência a área duperior do primeiro componente
        return

    def __calculateSkinDragCoefficient(self,  current_state: DeltaTimeSimulation) -> float: # coef. arrasto de pele
        rocketLength = current_state.rocket_height.magnitude()
        velocity = 47.78280931761668
        referenceArea = pi * current_state.nose.base_radius ** 2 
        parts = current_state.parts
        print(parts)
        for part in parts:
            if part.part_type == RocketParts.FIN:
                meanChord = mean_aerodynamic_chord_length('trapezoidal', part.root_chord, part.tip_chord)
                finMaxThickness = part.max_thickness
                finsWetArea = FinModel.calculateWetArea(self)
            
            else:
                meanChord = 0
                finMaxThickness = 0
                finsWetArea = 0

        #rocketSurfaceArea = current_state.wet_area
        rocketSurfaceArea = 75.39822369 #<-- cilindro1; Modificar para Wetted area
        reynoldsNumber = reynolds_number(velocity, rocketLength, Constants.KINEMATIC_VISCOSITY.value)
        mach = mach_number(velocity, 340)
        rocketFinenessRatio = rocket_fineness_ratio(rocketLength, current_state.nose.base_diameter)
        criticalReynoldsNumber = critical_reynolds_number(0.0000005, rocketLength)
        skingFrictionDrag = skin_friction_drag(reynoldsNumber, criticalReynoldsNumber, 0.0000005, rocketLength, mach)
        skinDragCoefficient = total_skin_friction_drag_coefficient(skingFrictionDrag, rocketFinenessRatio, rocketSurfaceArea, finMaxThickness, meanChord, finsWetArea, referenceArea)
        return skinDragCoefficient

    def __calculatePressureDragCoefficient(self, current_state: DeltaTimeSimulation) -> float:
        velocity = 47.78280931761668
        referenceArea = pi * current_state.nose.base_radius ** 2
        mach = mach_number(velocity, 340)
        baseDrag = base_drag_coefficient(mach)   
        stagnationDrag = 0 
        parts = current_state.parts
        pressureDragCoefficient = 0
        for part in parts:
            if part.part_type == RocketParts.NOSE:
                if current_state.nose.nose_type == NoseType.CONICAL:
                    bodynoseAngle = degrees(atan(part.base_radius / part.height))
                    noseDrag = nose_pressure_drag(bodynoseAngle) 
                    pressureDragCoefficient += noseDrag
                    print(noseDrag)

                else:
                    pass

            elif part.part_type == RocketParts.TRANSITION:
                topDiameter = part.top_diameter
                bottomDiameter = part.bottom_diameter
                height = part.height
                if bottomDiameter < topDiameter:
                    boatttailDrag = boattail_pressure_drag_coeficent(topDiameter, bottomDiameter, height, baseDrag, (pi * topDiameter ** 2) / 4, (pi * bottomDiameter ** 2) / 4) 
                    pressureDragCoefficient += boatttailDrag * abs((pi * topDiameter ** 2) / 4 - (pi * bottomDiameter ** 2) / 4) / referenceArea
                else:
                    bodyshoulderAngle = degrees(atan(abs((part.bottom_diameter/2) - (part.top_diameter/2))/part.height))
                    shoulderDrag = nose_pressure_drag(bodyshoulderAngle) 
                    pressureDragCoefficient += shoulderDrag * abs((pi * bottomDiameter ** 2) / 4 - (pi * topDiameter ** 2) / 4) / referenceArea

            elif part.part_type == RocketParts.CYLINDRICAL_BODY:
                if len(parts) == 1:
                    stagnationDrag = stag_pressure_drag_coeficient(mach) * pi * (part.diameter / 2) ** 2

            elif part.part_type == RocketParts.FIN:
                leadingEdgeDrag = fin_drag_coeficient(mach) * cos(degrees(atan(abs(part.root_chord - part.tip_chord) / part.span))) ** 2
                trailingEdgeDrag = base_drag_coefficient(mach)
                finDrag = leadingEdgeDrag + trailingEdgeDrag 
                pressureDragCoefficient += finDrag * part.nb_fins * part.max_thickness * part.span / referenceArea
                baseDrag *= (pi * part.distance_from_center ** 2) / referenceArea

            else:
                pass

            #Existe documentação para implementação do arrasto para guias de lançamento também
        return pressureDragCoefficient + baseDrag + stagnationDrag

    def __calculateDragCoefficient(self, current_state: DeltaTimeSimulation) -> float: # coef. arrasto final usado no calculo do arrasto
        return self.__calculateSkinDragCoefficient(current_state) + self.__calculatePressureDragCoefficient(current_state)
        #return self.__calculatePressureDragCoefficient(current_state)
    def __calculateDrag(self, transversal_section_area:float, drag_coefficient:float, velocity:float):
        air_density = Constants.AIR_DENSITY.value
        return ((1/2)*air_density*velocity**2*transversal_section_area*drag_coefficient)

    def calculate(self, current_state: DeltaTimeSimulation):
        velocity = 47.78280931761668
        referenceArea = pi * current_state.nose.base_radius ** 2 
        
        self.__drag_coefficient = self.__calculateDragCoefficient(current_state)

        magnitude = self.__calculateDrag(referenceArea, self.__drag_coefficient, velocity)

        dragForce = current_state.velocity * -1
        dragForce = dragForce.unitVector() * magnitude

        print('Velocity = 47.78280931761668 m/s')
        print(f'Cd = {self.__drag_coefficient}')
        # print(dragForce.magnitude())

        self.setX(dragForce.x())
        self.setY(dragForce.y())
        self.setZ(dragForce.z())

