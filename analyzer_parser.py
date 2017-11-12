# -*- enconding: utf-8 -*-

import ply.yacc as yacc
from analyzer_simple import tokens
import analyzer_simple
import sys

VERBOSE = 1

def p_program(p):
    'program : declaration_list'
    pass

def p_declaration_list(p):
    '''declaration_list : declaration_list declaration
                        | declaration'''
    pass

def p_declaration(p):
    '''declaration : set_declaration
                   | gets_declaration token_pyc
                   | puts_declaration
                   | token_cor_izq execution_list token_cor_der token_pyc
                   | empty'''
                   # | incr_declaration
                   # | ifs_declaration
                   # | whiles_declaration
                   # | fors_declaration
                   # | switchs_declaration'''
    pass

def p_execution_list(p):
    '''execution_list : array size id
                      | array exists id
                      | id args
                      | gets_declaration
                      | exprs'''
    pass

def p_procs(p):
    'procs : proc id token_llave_izq args token_llave_der'
    pass

def p_args(p):
    '''args : token_llave_izq args_list token_llave_der args
            | token_llave_izq token_cor_izq execution_list token_cor_der token_llave_der args
            | token_llave_izq execution_list token_llave_der args
            | empty'''
    pass

def p_args_list(p):
    '''args_list : number
                 | token_dollar id token_par_izq token_integer token_par_der
                 | token_dollar id
                 | token_string'''
    pass

def p_exprs(p):
    '''exprs : expr token_llave_izq expression token_llave_der'''
    pass

def p_set_declaration(p):
    '''set_declaration : set id token_integer token_pyc
                       | set id token_double token_pyc
                       | set id token_string token_pyc
                       | set id id token_pyc
                       | set id token_cor_izq id args token_cor_der token_pyc
                       | set id token_dollar id token_pyc
                       | set id token_par_izq token_integer token_par_der elem token_pyc
                       | set id token_par_izq token_integer token_par_der token_cor_izq exprs token_cor_der token_pyc
                       | set id token_par_izq token_cor_izq exprs token_cor_der token_par_der exprs token_pyc
                       | set id token_par_izq token_cor_izq exprs token_cor_der token_par_der elem token_pyc
                       '''
    pass

def p_gets_declaration(p):
    'gets_declaration : gets stdin'
    pass

def p_puts_declaration(p):
    '''puts_declaration : puts token_integer token_pyc
                        | puts token_double token_pyc
                        | puts token_string token_pyc
                        | puts token_dollar id token_pyc'''
    pass

# def p_ifs_declaration(p):
    # 'ifs_declaration : if token_llave_izq boolean_expresion token_llave_der then token_llave_izq block token_llave_der elseif_declaration else_declaration'
    # pass

# def p_elseif_declaration(p):
    # '''elseif_declaration : elseif token_llave_izq boolean_expresion token_llave_der token_llave_izq block token_llave_der elseif_declaration
                          # | empty'''
    # pass

# def p_else_declaration(p):
    # '''else_declaration : else token_llave_izq block token_llave_der
                        # | empty'''
    # pass

def p_boolean_expresion(p):
    '''boolean_expresion : token_integer boolean_gateway
                         | expression boolean_operator expression boolean_gateway'''
    pass

def p_boolean_gateway(p):
    '''boolean_gateway : token_and boolean_expresion
                       | token_or boolean_expresion
                       | empty'''
    pass

def p_boolean_operator(p):
    '''boolean_operator : token_igual_num
                        | token_diff_num
                        | token_igual_str
                        | token_diff_str
                        | token_mayor
                        | token_menor
                        | token_mayor_igual
                        | token_menor_igual'''
    pass

def p_expression(p):
    '''expression : expression token_mas term
                  | expression token_menos term
                  | term'''
    pass

def p_term(p):
    '''term : term token_mul factor
            | term token_div factor
            | term token_mod factor
            | factor'''
    pass

def p_factor(p):
    '''factor : pow token_pot factor
              | pow'''
    pass

def p_pow(p):
    '''pow : token_menos pow
           | token_not pow
           | elem'''
    pass

def p_elem(p):
    '''elem : number
            | token_dollar id token_par_izq token_integer token_par_der
            | token_dollar id
            | token_string
            | token_cor_izq id args token_cor_der
            | token_par_izq expression token_par_der'''
    pass

def p_number(p):
    '''number : token_integer
              | token_double'''
    pass

def p_subroutines(p):
    '''subroutines : '''
    pass

###############################################

# def p_incr_declaration(p):
    # 'incr_declaration : incr id token_integer'
    # pass

# # Estructuras de control
# def p_whiles_declaration(p):
    # 'whiles_declaration : while token_llave_izq boolean_expresion token_llave_der token_llave_izq block token_llave_der'
    # pass

# def p_fors_declaration(p):
    # 'fors_declaration : for token_llave_izq set_declaration token_llave_der token_llave_izq expression token_llave_der token_llave_izq incr_declaration token_llave_der token_llave_izq block token_llave_der'
    # pass

# def p_switchs_declaration(p):
    # 'switchs_declaration : switch token_dollar id token_llave_izq case_declaration default_declaration token_llave_der'
    # pass

# def p_case_declaration(p):
    # 'case_declaration : case token_integer token_llave_izq block token_llave_der'
    # pass

# def p_default_declaration(p):
    # '''default_declaration : token_llave_izq block token_llave_der
                           # | empty'''
    # pass

###############################################
def p_empty(p):
    'empty :'
    pass

def p_error(p):
    #print str(dir(p))
    #print str(dir(cminus_lexer))
    if VERBOSE:
        if p is not None:
            print "Syntax error at line " + str(p.lexer.lineno) + " Unexpected token  " + str(p.value)
        else:
            print "Syntax error at line: " + str(cminus_lexer.lexer.lineno)
    else:
        raise Exception('syntax', 'error')

parser = yacc.yacc()

if __name__ == '__main__':

    if (len(sys.argv) > 1):
        fin = sys.argv[1]
    else:
        fin = 'examples/gcd.c'

    f = open(fin, 'r')
    data = f.read()
    print data
    parser.parse(data, tracking=True)
