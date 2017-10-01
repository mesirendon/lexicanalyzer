import ply.lex as lex

tokens = (
        'token_llave_izq'  ,
        'token_llave_der'  ,
        'token_dollar'     ,
        'token_pyc'        ,
        'token_cor_izq'    ,
        'token_cor_der'    ,
        'token_par_izq'    ,
        'token_par_der'    ,
        'token_mayor'      ,
        'token_menor'      ,
        'token_mayor_igual',
        'token_menor_igual',
        'token_igual_str'  ,
        'token_igual_num'  ,
        'token_diff_str'   ,
        'token_diff_num'   ,
        'token_and'        ,
        'token_or'         ,
        'token_not'        ,
        'token_mas'        ,
        'token_menos'      ,
        'token_mul'        ,
        'token_div'        ,
        'token_mod'        ,
        'token_pot'        ,
        'set'              ,
        'gets'             ,
        'puts'             ,
        'integer'          ,
        'double'           ,
        'string'           ,
        'expr'             ,
        'if'               ,
        'then'             ,
        'elseif'           ,
        'else'             ,
        'switch'           ,
        'default'          ,
        'while'            ,
        'continue'         ,
        'break'            ,
        'incr'             ,
        'for'              ,
        'array'            ,
        'array size'       ,
        'array exists'     ,
        'proc'             ,
        'return'
        )

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
t_token_or          = r'\||'
t_token_not         = r'\!'
t_token_mas         = r'\+'
t_token_menos       = r'\-'
t_token_mul         = r'\*'
t_token_div         = r'\/'
t_token_mod         = r'\%'
t_token_pot         = r'\**'

# Palabras reservadas
t_set               = r'set'
t_gets              = r'gets'
t_puts              = r'puts'
t_expr              = r'expr'
t_if                = r'if'
t_then              = r'then'
t_elseif            = r'elseif'
t_else              = r'else'
t_switch            = r'switch'
t_default           = r'default'
t_while             = r'while'
t_continue          = r'continue'
t_break             = r'break'
t_incr              = r'incr'
t_for               = r'for'
t_array             = r'array'
# t_array size        = r'array size'
# t_array exists      = r'array exists'
t_proc              = r'proc'
t_return            = r'return'

def t_integer(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_double(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_string(t):
    r'\".+\"'
    t.value = str(t.value)
    return t


lexer = lex.lex()

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)
