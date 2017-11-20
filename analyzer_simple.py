import sys
import re
import ply.lex as lex


# Palabras reservadas
reserved = {
    'set'             : 'set',
    'gets'            : 'gets',
    'puts'            : 'puts',
    'expr'            : 'expr',
    'if'              : 'if',
    'then'            : 'then',
    'elseif'          : 'elseif',
    'else'            : 'else',
    'switch'          : 'switch',
    'default'         : 'default',
    'while'           : 'while',
    'continue'        : 'continue',
    'break'           : 'break',
    'incr'            : 'incr',
    'for'             : 'for',
    'size'            : 'size',
    'exists'          : 'exists',
    'array'           : 'array',
    'proc'            : 'proc',
    'return'          : 'return',
    'stdin'           : 'stdin',
    'token_igual_str' : 'eq',
    'case'            : 'case'
}

tokens = [
        'token_integer',
        'token_double',
        'token_string',
        'id',
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
        'token_pot'
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
t_token_mayor       = r'>'
t_token_menor       = r'<'
t_token_mayor_igual = r'>='
t_token_menor_igual = r'<='
t_token_igual_num   = r'=='
t_token_diff_num    = r'!='
t_token_and         = r'\&&'
t_token_or          = r'\|\|'
t_token_not         = r'!'
t_token_mas         = r'\+'
t_token_menos       = r'-'
t_token_mul         = r'\*'
t_token_div         = r'\/'
t_token_mod         = r'%'
t_token_pot         = r'\*\*'


def t_token_double(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_token_integer(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_token_string(t):
    r'\".+\"'
    t.value = str(re.sub('\"', '', t.value))
    return t

def t_token_igual_str(t):
    r'eq'
    t.value = str('token_igual_str')
    return t

def t_token_diff_str(t):
    r'ne'
    t.value = str('token_diff_str')
    return t

def t_id(t):
    r'[a-zA-Z_][a-zA-Z_]*(\d*)?'
    if t.value in reserved:
        t.type = reserved.get(t.value)
    else:
        t.type = str('id')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comments(t):
    r'\#(.)*'

def t_error(t):
    print("Error lexico (linea:" + (str(t.lineno + 1)) + ", posicion:" + (str(find_column(t))) + ")")
    t.lexer.skip(1000)

t_ignore = ' \t'

def find_column(token):
    last_cr = data.rfind('\n', 0, token.lexpos)
    if last_cr < 0:
        last_cr = -1
    column = (token.lexpos - last_cr)
    return column

def lexerRun(data, lexer):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        if (tok.type in ["token_integer", "token_string", "token_double", "id"]):
            print("<" + tok.type + "," +  str(tok.value) + "," +  str(tok.lineno) + "," + str(find_column(tok)) + ">")
        else:
            print("<" + tok.type + "," + str(tok.lineno) +  "," + str(find_column(tok)) + ">")



data = ''

lexer = lex.lex()

if __name__ == '__main__':
    # Necesita un archivo usando python. Ejemplo: python analyzer_simple.py < in00.txt
    for line in sys.stdin:
        data += line
    lexer.input(data)
    lexerRun(data, lexer)
