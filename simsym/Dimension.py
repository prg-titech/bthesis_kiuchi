from __future__ import annotations
from enum import Enum
from fractions import Fraction

class _Dim(Enum):
  Length = 'L'
  Mass = 'M'
  Time = 'T'

class _DimDict(dict[_Dim, Fraction]):
  def __str__(self) -> str:
    numerator = ''
    denominator = ''
    for d in _Dim:
      if self[d] > 0:
        numerator += d.value
        if self[d] != 1:
          numerator += f'^{self[d]}'
      elif self[d] < 0:
        denominator += d.value
        if self[d] != -1:
          denominator += f'^{-self[d]}'

    if denominator == numerator == '':
      return '[1]'
    if denominator == '':
      return f'[{numerator}]'
    elif numerator == '':
      return f'[1/{denominator}]'
    else:
      return f'[{numerator}/{denominator}]'

  def __repr__(self) -> str:
    return str(self)

class Dimension():
  dim: _DimDict
  def __init__(self, dim: _DimDict) -> None:
    for d in _Dim:
      if d not in dim.keys():
        dim[d] = 0
    self.dim = dim

  def __add__(self, other: Dimension) -> Dimension:
    if self.dim == other.dim:
      return self.dim
    else:
      raise TypeError(f"Can't add {self.dim} to {other.dim}")

  def __sub__(self, other: Dimension) -> Dimension:
    if self.dim == other.dim:
      return self.dim
    else:
      raise TypeError(f"Can't add {self.dim} to {other.dim}")

  def __mul__(self, other: Dimension) -> Dimension:
    dim = {}
    for d in _Dim:
      dim[d] = self.dim[d] + other.dim[d]
    return Dimension(dim=_DimDict(dim))

  def __pow__(self, other: int) -> Dimension:
    dim = {}
    for d in _Dim:
      dim[d] = self.dim[d] * other
    return Dimension(dim=_DimDict(dim))

  def __truediv__(self, other: Dimension) -> Dimension:
    dim = {}
    for d in _Dim:
      dim[d] = self.dim[d] - other.dim[d]
    return Dimension(dim=_DimDict(dim))

  def __str__(self) -> str:
    return str(self.dim)

  def __repr__(self) -> str:
    return str(self)

Length = Dimension(_DimDict({_Dim.Length:1}))
Mass = Dimension(_DimDict({_Dim.Mass:1}))
Time = Dimension(_DimDict({_Dim.Time:1}))

if __name__ == '__main__':
  print(Length)
  try:
    print(Length + Mass)
  except TypeError as e:
    print(e)
  print(Length * Mass)
  print(Length / Mass / Mass)

