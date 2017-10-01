import sys
import ply.lex as lex


# Palabras reservadas
reserved = {
    'set'           : 'set',
    'gets'          : 'gets',
    'puts'          : 'puts',
    'expr'          : 'expr',
    'if'            : 'if',
    'then'          : 'then',
    'elseif'        : 'elseif',
    'else'          : 'else',
    'switch'        : 'switch',
    'default'       : 'default',
    'while'         : 'while',
    'continue'      : 'continue',
    'break'         : 'break',
    'incr'          : 'incr',
    'for'           : 'for',
#    'array size'    : 'ARRAY SIZE',
#    'array exists'  : 'ARRAY EXISTS',
    'array'         : 'array',
    'proc'          : 'proc',
    'return'        : 'return',
}

tokens = [
        'integer',
        'double',
        'string',
        'token_llave_izq',
        'token_llave_der',
        'token_dollar',
        'token_pyc',
        'token_cor_izq',
        'token_cor_der',
        'token_par_izq',
        'token_par_der',
        'token_mayor',
        'token_menor',
        'token_mayor_igual',
        'token_menor_igual',
        'token_igual_str',
        'token_igual_num',
        'token_diff_str',
        'token_diff_num',
        'token_and',
        'token_or',
        'token_not',
        'token_mas',
        'token_menos',
        'token_mul',
        'token_div',
        'token_mod',
        #'token_pot',
        ] + list(reserved.values())

# Tokens simples
t_token_llave_izq   = r'\{'
t_token_llave_der   = r'\}'
t_token_dollar      = r'\$'
t_token_pyc         = r'\;'
t_token_cor_izq     = r'\['
t_token_cor_der     = r'\]'
t_token_par_izq     = r'\('
t_token_par_der     = r'\)'
t_token_mayor       = r'\>'
t_token_menor       = r'\<'
t_token_mayor_igual = r'\>='
t_token_menor_igual = r'\<='
t_token_igual_str   = r'eq'
t_token_igual_num   = r'\=='
t_token_diff_str    = r'ne'
t_token_diff_num    = r'\!='
t_token_and         = r'\&&'
#t_token_or          = r'\||'
t_token_not         = r'\!'
t_token_mas         = r'\+'
t_token_menos       = r'\-'
t_token_mul         = r'\*'
t_token_div         = r'\/'
t_token_mod         = r'\%'
#t_token_pot         = r'\**'


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

def t_reserved(t):
    r'[a-z_][a-z_]*'
    t.type = reserved.get(t.value,'ID')
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
