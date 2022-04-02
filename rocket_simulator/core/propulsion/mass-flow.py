"""
@author marina
@email [marinasalesr@gmail.com]
@create date 2022-03-30 09:34:28
"""

import SymPy

def mass_flow(pp, Ab, r, p0, V0, R, T0, derivate_pressure):
  mn = pp*Ab*r - (p0*Ab*r + ((V0/(R*T0))*derivate_pressure))
  return mn
