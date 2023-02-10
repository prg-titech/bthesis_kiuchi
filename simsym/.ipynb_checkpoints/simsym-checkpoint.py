from typing import List
from sympy import Eq, solve, latex
from sympy.physics.units.systems import SI
from sympy.physics.units import Quantity, length, mass, time

t = Quantity('t', latex_repr='t')
SI.set_quantity_dimension(t, dimension=time)
g = Quantity('g', latex_repr='g')
SI.set_quantity_dimension(g, dimension=length/time**2)

class Object() :
  def __init__(self, name: str) -> None:
    self.name = name
    self.x = Quantity(f'x{name}', latex_repr=f'x_{name}')
    SI.set_quantity_dimension(self.x, dimension=length)
    self.y = Quantity(f'y{name}', latex_repr=f'y_{name}')
    SI.set_quantity_dimension(self.y, dimension=length)
    self.vx = Quantity(f'v{name}x', latex_repr=f'v_{{{name}x}}')
    SI.set_quantity_dimension(self.vx, dimension=length/time)
    self.vy = Quantity(f'v{name}y', latex_repr=f'v_{{{name}y}}')
    SI.set_quantity_dimension(self.vy, dimension=length/time)

  def __repr__(self) -> str:
    return str(self)

  def __str__(self) -> str:
    return f'物体 {self.name}'

  def subs(self, param):
    return subs(self, param)

class Eqs():
  eqs: List[Eq] = []
  def append(self, eq: Eq) -> None:
    self.eqs.append(eq)

  def reset(self) -> None:
    self.eqs = []

eqs = Eqs()

def subs(obj: Object, param):
  res = []
  for lhs, rhs in solve(eqs.eqs, (obj.x, obj.y, obj.vx, obj.vy)).items():
    res.append((lhs, rhs.subs(param)))
  return res