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
                    | importstatements importstatement
    '''
def p_importstatement(p):
    '''importstatement : KEYIMPORT QualifiedName Semicolons
                    | KEYIMPORT QualifiedName SEPDOT OPMULTIPLY Semicolons
    '''
def p_QualifiedName(p):
    '''QualifiedName : Identifier
                | QualifiedName SEPDOT Identifier
    '''
def p_Semicolons(p):
    '''Semicolons : SEPSEMICOLON
                | Semicolons SEPSEMICOLON
    '''
def p_TypeSpecifier(p):
    '''TypeSpecifier : TypeName               
    '''
#don't know what is Dims
def p_Semicolons(p):
    '''Semicolons : SEPSEMICOLON
                | Semicolons SEPSEMICOLON
    '''
def p_TypeName(p):
    '''TypeName : PrimitiveType
            | QualifiedName
    '''
def p_PrimitiveType(p):
    '''PrimitiveType : KEYBOOLEAN
                | KEYCHAR
                | KEYDOUBLE
                | KEYBYTE
                | KEYSHORT
                | KEYINT
                | KEYLONG
                | KEYVOID
                | KEYFLOAT
    '''
# def p_ClassNameList(p):
#     '''
#     '''
def p_error(p):
    if p == None:
        print "You missed something at the end"
    else:
        print "Syntax error in input line!"

parser = yacc.yacc()

while 1:
    try:
        s = raw_input('calc > ')
    except EOFError:
        break
    if not s: continue
    yacc.parse(s)