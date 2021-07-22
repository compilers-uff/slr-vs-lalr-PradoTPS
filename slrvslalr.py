import ply.lex as lex
import ply.yacc as yacc

method = ''
while(method != 'SLR' and method != 'LALR'):
  print('SLR or LALR?')
  method = input()

tokens = (
  'ID',
)

literals = (
  '=',
  '*',
)

t_ID= r'id'

def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)

lexer = lex.lex()

def p_S(p):
  '''S : L '=' R
  | R'''

def p_L(p):
  '''L : '*' R
  | ID'''

def p_R(p):
  '''R : L'''

def p_error(p):
  print("Syntax error at token", p.type)
  return

yacc.yacc(method, debug=True)