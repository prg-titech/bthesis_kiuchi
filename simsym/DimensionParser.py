from Dimension import Dimension, Length, Mass, Time
import ply.lex as lex
import ply.yacc as yacc

tokens = (
  'LENGTH',
  'MASS',
  'TIME',
  'NUM',
  'HAT',
  'DIVIDE',
  'ONE'
)
def t_LENGTH(t):
  r'l|L'
  t.value = Length
  return t
def t_MASS(t):
  r'm|M'
  t.value = Mass
  return t
def t_TIME(t):
  r't|T'
  t.value = Time
  return t
def t_NUM(t):
  r'\d+'
  t.value = int(t.value)
  return t
t_HAT = r'\^'
t_DIVIDE = r'/'
t_ignore = ' \t'
def t_error(t):
  raise SyntaxError("Illegal character '%s'" % t.value[0])
lexer = lex.lex()

precedence = (
  ('left', 'HAT'),
  ('left', 'DIVIDE')
)
def p_statement_div(p):
  """statement : expression
               | expression DIVIDE expression
               | NUM DIVIDE expression"""
  if len(p) == 2:
    p[0] = p[1]
  else:
    if p[1] == 1:
      p[0] = (Length / Length) / p[3]
    else:
      p[0] = p[1] / p[3]
def p_expression_hat(p):
  """expression : dimension
                | dimension expression
                | dimension HAT number
                | dimension HAT number expression"""
  if len(p) == 2:
    p[0] = p[1]
  elif len(p) == 3:
    p[0] = p[1] * p[2]
  elif len(p) == 4:
    p[0] = p[1] ** p[3]
  else:
    p[0] = p[1] ** p[3] * p[4]
def p_dimension(p):
  """dimension : LENGTH
                | MASS
                | TIME"""
  p[0] = p[1]
def p_number(p):
  """number : NUM"""
  p[0] = p[1]
def p_error(p):
  raise SyntaxError("Syntax Error")
yacc.yacc()

def parseDim(dim_string: str) -> Dimension:
  return yacc.parse(dim_string)

if __name__ == '__main__':
  dim_strs = (
    'L',
    'LM',
    'L/T',
    'L^2',
    'LM/T^2',
    '1/L',
    'LMTTM/MMMMMMMM^3'
  )

  for dim_str in dim_strs:
    print(dim_str, parseDim(dim_str))
