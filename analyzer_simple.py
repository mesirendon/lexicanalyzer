import sys
import ply.lex as lex

tokens = [
        'integer',
        'double',
        'string'
        ]

def t_double(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_integer(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_string(t):
    r'\".+\"'
    t.value = str(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

t_ignore = ' \t'

lex.lex()

data = ''
for line in sys.stdin:
    data += line

lex.input(data)

# Tokenize
cr = 0
while True:
    tok = lex.token()
    if not tok:
        break      # No more input
    print("<" + tok.type + "," + str(tok.lineno) + "," + str(tok.lexpos) + ">")
