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
    '''declaration : set_declaration token_pyc
                   | gets_declaration token_pyc
                   | puts_declaration token_pyc
                   | token_cor_izq execution_list token_cor_der token_pyc
                   | ifs_declaration
                   | fors_declaration
                   | incr_declaration
                   | break token_pyc
                   | continue token_pyc
                   | whiles_declaration
                   | switchs_declaration
                   | procs
                   | empty'''
    pass

def p_execution_list(p):
    '''execution_list : array size id
                      | array exists id
                      | id args
                      | gets_declaration
                      | exprs'''
    pass

def p_procs(p):
    'procs : proc id token_llave_izq args token_llave_der token_llave_izq declaration_list returns_declaration token_llave_der'
    pass

def p_args(p):
    '''args : token_llave_izq args_list token_llave_der args
            | token_llave_izq token_cor_izq execution_list token_cor_der token_llave_der args
            | token_llave_izq execution_list token_llave_der args
            | token_llave_izq token_dollar id token_par_izq token_cor_izq execution_list token_cor_der token_par_der token_llave_der args
            | empty'''
    pass

def p_args_list(p):
    '''args_list : number
                 | token_dollar id token_par_izq token_integer token_par_der
                 | token_dollar id
                 | token_string'''
    pass

def p_returns_declaration(p):
    '''returns_declaration : return elem token_pyc returns_declaration
                           | return token_cor_izq execution_list token_cor_der token_pyc returns_declaration
                           | return token_dollar id token_pyc returns_declaration
                           | return token_pyc returns_declaration
                           | empty'''
    pass

def p_exprs(p):
    '''exprs : expr token_llave_izq expression token_llave_der'''
    pass

def p_set_declaration(p):
    '''set_declaration : set id token_integer
                       | set id token_double
                       | set id token_string
                       | set id token_cor_izq gets_declaration token_cor_der
                       | set id token_cor_izq execution_list token_cor_der
                       | set id id
                       | set id token_cor_izq id args token_cor_der
                       | set id token_dollar id
                       | set id token_par_izq token_integer token_par_der elem
                       | set id token_par_izq token_integer token_par_der token_cor_izq execution_list token_cor_der
                       | set id token_par_izq token_cor_izq exprs token_cor_der token_par_der exprs
                       | set id token_par_izq token_cor_izq exprs token_cor_der token_par_der elem'''
    pass

def p_gets_declaration(p):
    'gets_declaration : gets stdin'
    pass

def p_puts_declaration(p):
    '''puts_declaration : puts token_integer
                        | puts token_double
                        | puts token_string
                        | puts token_dollar id token_par_izq elem token_par_der
                        | puts token_dollar id
                        | puts token_cor_izq execution_list token_cor_der'''
    pass

def p_ifs_declaration(p):
    'ifs_declaration : if token_llave_izq boolean_expresion token_llave_der then token_llave_izq declaration_list token_llave_der elseif_declaration else_declaration'
    pass

def p_elseif_declaration(p):
    '''elseif_declaration : elseif token_llave_izq boolean_expresion token_llave_der then token_llave_izq declaration_list token_llave_der elseif_declaration
                          | empty'''
    pass

def p_else_declaration(p):
    '''else_declaration : else token_llave_izq declaration_list token_llave_der
                        | empty'''
    pass

def p_fors_declaration(p):
    'fors_declaration : for token_llave_izq set id token_integer token_llave_der token_llave_izq boolean_expresion token_llave_der token_llave_izq incr_declaration token_llave_der token_llave_izq declaration_list token_llave_der'
    pass

def p_incr_declaration(p):
    '''incr_declaration : incr id token_integer
                        | incr id'''
    pass

def p_whiles_declaration(p):
    'whiles_declaration : while token_llave_izq boolean_expresion token_llave_der token_llave_izq declaration_list token_llave_der'
    pass

def p_switchs_declaration(p):
    'switchs_declaration : switch token_dollar id token_llave_izq case_declaration default_declaration token_llave_der'
    pass

def p_case_declaration(p):
    '''case_declaration : case token_integer token_llave_izq declaration_list token_llave_der case_declaration
                        | empty'''
    pass

def p_default_declaration(p):
    '''default_declaration : default token_llave_izq declaration_list token_llave_der
                           | empty'''
    pass

def p_boolean_expresion(p):
    '''boolean_expresion : token_integer boolean_gateway
                         | expression boolean_operator expression boolean_gateway
                         | expression'''
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

###############################################
def p_empty(p):
    'empty :'
    pass

def p_error(p):
    #print str(dir(p))
    #print str(dir(cminus_lexer))
    if VERBOSE:
        if p is not None:
            # print "Syntax error at line " + str(p.lexer.lineno) + " Unexpected token  " + str(p.value)
            raise Exception('syntax', str(p.lexer.lineno), str(p.value), str(p))
        else:
            print "Syntax error at line: " + str(analyzer_simple.lexer.lineno)
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
    try:
        parser.parse(data, tracking=True)
        print "El analisis sintactico ha finalizado correctamente."
    except Exception as things:
        print things.args
