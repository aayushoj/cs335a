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
def p_ClassNameList(p):
    '''ClassNameList : QualifiedName
                 | ClassNameList SEPCOMMA QualifiedName
    '''
# def p_CompliationUnit(p):
#     '''CompliationUnit : ProgramFile
#     '''
# def p_ProgramFile(p):
#     ''' ProgramFile : PackageStatement ImportStatements TypeDeclarations
#                 | PackageStatement ImportStatements
#                 | PackageStatement TypeDeclarations
#                 | ImportStatements TypeDeclarations
#                 | PackageStatement
#                 | ImportStatements
#                 | TypeDeclarations
#     '''
# def p_PackageStatement(p):
#     '''PackageStatement : PACKAGE QualifiedName Semicolons
#     '''
# def p_TypeDeclarations(p):
#     '''TypeDeclarations : TypeDeclarationOptSemi
#                     | TypeDeclarations TypeDeclarationOptSemi
#     '''
# def p_TypeDeclarationOptSemi(p):
#     '''TypeDeclarationOptSemi : TypeDeclaration
#                     | TypeDeclaration SemiColons
#     '''
# def p_TypeDeclaration(p):
#     '''TypeDeclaration : ClassHeader SEPLEFTPARAN FieldDeclarations SEPRIGHTPARAN
#                     | ClassHeader SEPLEFTPARAN SEPRIGHTPARAN
#     '''
# def p_ClassHeader(p):
#     '''ClassHeader : Modifiers ClassWord Identifier Extends Interfaces
#                 | Modifiers ClassWord Identifier Extends
#                 | Modifiers ClassWord Identifier Interfaces
#                 | ClassWord Identifier Extends Interfaces
#                 | Modifiers ClassWord Identifier
#                 | ClassWord Identifier Extends
#                 | ClassWord Identifier Interfaces
#                 | ClassWord Identifier
#     '''
def p_Modifiers(p):
    '''Modifiers : Modifier
                | Modifiers Modifier
    '''
def p_Modifier(p):
    '''Modifier : KEYPUBLIC
                | KEYPROTECTED
                | KEYPRIVATE
                | KEYSTATIC
    '''
def p_Statement(p):
    '''Statement : EmptyStatement
                | ExpressionStatement SEPSEMICOLON
                | SelectionStatement
                | IterationStatement
                | JumpStatement
                | Block
    '''
def p_EmptyStatement(p):
    ''' EmptyStatement : SEPSEMICOLON
    '''
def p_ExpressionStatement(p):
    '''ExpressionStatement : Expression
    '''
def p_SelectionStatement(p):
    '''SelectionStatement : KEYIF SEPLEFTBRACE Expression SEPRIGHTBRACE Statement
                        | KEYIF SEPLEFTBRACE Expression SEPRIGHTBRACE Statement KEYELSE Statement
    '''
def p_IterationStatement(p):
    '''IterationStatement : KEYWHILE SEPLEFTBRACE Expression SEPRIGHTBRACE Statement
    '''
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