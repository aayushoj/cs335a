#!/usr/bin/python
import ply.lex as lex
import sys
import ply.yacc as yacc
from latestlexer import tokens

# print tokens

def p_program(p):
    '''program : importstatements '''

def p_importstatements(p):
    '''importstatements : importstatement
                    |importstatements importstatement
    '''
def p_importstatement(p):
    '''importstatement : KEYIMPORT QualifiedName Semicolons
                    | KEYIMPORT QualifiedName '.' '*' Semicolons
    '''
def p_Semicolons(p):
    '''Semicolons : SEPSEMICOLON
                | Semicolons SEPSEMICOLON
    '''

def p_methodline(p):
    '''methodline : KEYPUBLIC KEYSTATIC KEYVOID Identifier '''

def p_error(p):
    if p == None:
        print "You missed something at the end"
    else:
        print "Syntax error in input line!"

parser = yacc.yacc()