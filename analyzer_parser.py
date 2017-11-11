# -*- enconding: utf-8 -*-

import ply.yacc as yacc
from analyzer_simple import tokens
import analyzer_simple
import sys

VERBOSE = 1

def p_program(p):
    'program : declaration_list'
    pass

def p_declaration_list_1(p):
    'declaration_list : declaration_list declaration'
    pass

def p_declaration_list_2(p):
    'declaration_list : declaration'
    pass

def p_declaration(p):
    '''declaration : set_declaration
                   | gets_declaration
                   | incr_declaration
                   | puts_declaration
                   | ifs_declaration
                   | whiles_declaration
                   | fors_declaration
                   | switchs_declaration'''
    pass

def p_set_declaration(p):
    '''set_declaration : set id token_integer token_pyc
                       | set id token_double token_pyc
                       | set id token_string token_pyc
                       | set id id token_pyc
                       | set id token_dollar id token_pyc'''
    pass

def p_gets_declaration(p):
    'gets_declaration : gets stdin token_pyc'
    pass

def p_puts_declaration(p):
    '''puts_declaration : puts token_integer token_pyc
                        | puts token_double token_pyc
                        | puts token_string token_pyc
                        | puts token_dollar id token_pyc'''
    pass

def p_ifs_declaration(p):
    'ifs_declaration : if token_llave_izq boolean_expresion token_llave_der then token_llave_izq block token_llave_der elseif_declaration else_declaration'
    pass

def p_elseif_declaration(p):
    '''elseif_declaration : elseif token_llave_izq boolean_expresion token_llave_der token_llave_izq block token_llave_der elseif_declaration
                          | empty'''
    pass

def p_else_declaration(p):
    '''else_declaration : else token_llave_izq block token_llave_der
                        | empty'''
    pass

def p_boolean_expresion(p):
    '''boolean_expresion : 1 boolean_gateway
                         | 0 boolean_gateway
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

###############################################

def p_incr_declaration(p):
    'incr_declaration : incr id token_integer'
    pass

# Estructuras de control
def p_whiles_declaration(p):
    'whiles_declaration : while token_llave_izq boolean_expresion token_llave_der token_llave_izq block token_llave_der'
    pass

def p_fors_declaration(p):
    'fors_declaration : for token_llave_izq set_declaration token_llave_der token_llave_izq expression token_llave_der token_llave_izq incr_declaration token_llave_der token_llave_izq block token_llave_der'
    pass

def p_switchs_declaration(p):
    'switchs_declaration : switch token_dollar id token_llave_izq case_declaration default_declaration token_llave_der'
    pass

def p_case_declaration(p):
    'case_declaration : case token_integer token_llave_izq block token_llave_der'
    pass

def p_default_declaration(p):
    '''default_declaration : token_llave_izq block token_llave_der
                           | empty'''
    pass

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
