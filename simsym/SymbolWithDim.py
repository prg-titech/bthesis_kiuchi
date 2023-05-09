from __future__ import annotations
from sympy import Eq, latex, Symbol
from Dimension import Dimension, Length, Mass, Time

class SymbolWithDim():
  sym: Symbol
  dim: Dimension
  def __init__(self, sym, dim: Dimension) -> None:
    if type(sym) is str:
      self.sym = Symbol(sym)
    else:
      self.sym = sym
    self.dim = dim

  def __add__(self, other: SymbolWithDim):
    return SymbolWithDim(self.sym+other.sym, self.dim+other.dim)

  def __sub__(self, other: SymbolWithDim):
    return SymbolWithDim(self.sym-other.sym, self.dim-other.dim)

  def __mul__(self, other: SymbolWithDim):
    return SymbolWithDim(self.sym*other.sym, self.dim*other.dim)

  def __truediv__(self, other: SymbolWithDim):
    return SymbolWithDim(self.sym/other.sym, self.dim/other.dim)

  def __str__(self):
    return f'{str(self.sym)} {str(self.dim)}'

  def latex(self):
    return '$' + str(self.sym) + r'~\mathrm{' + str(self.dim) + '}$'

if __name__ == '__main__':
  x = SymbolWithDim('x', Length)
  y = SymbolWithDim('y', Length)
  print(x)
  print(y)
  print(x+y)
  print(x*y)
  try:
    print(x+x*y)
  except TypeError as e:
    print(e)


