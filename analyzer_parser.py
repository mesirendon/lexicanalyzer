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
