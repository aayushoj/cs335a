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
                | TypeName Dims               
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
def p_Block(p):
    '''Block : SEPLEFTPARAN LocalVariableDeclarationsAndStatements SEPRIGHTPARAN
            | SEPLEFTPARAN SEPRIGHTPARAN 
    '''
def p_LocalVariableDeclarationsAndStatements(p):
    '''LocalVariableDeclarationsAndStatements : LocalVariableDeclarationOrStatement
                        | LocalVariableDeclarationsAndStatements LocalVariableDeclarationOrStatement
    '''
def p_LocalVariableDeclarationOrStatement(p):
    '''LocalVariableDeclarationOrStatement : LocalVariableDeclarationStatement
                                | Statement
    '''
def p_LocalVariableDeclarationStatement(p):
    '''LocalVariableDeclarationStatement : TypeSpecifier VariableDeclarators  SEPSEMICOLON
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
                        | FOR SEPLEFTBRACE Forint Forexpr ForIncr SEPRIGHTBRACE Statement
                        | FOR SEPLEFTBRACE Forint Forexpr SEPRIGHTBRACE Statement
    '''
def p_ForInt(p):
    '''ForInt : ExpressionStatements SEPSEMICOLON
            | LocalVariableDeclarationStatement
            | SEPSEMICOLON
    '''
def p_ForExpr(p):
    '''ForExpr : Expression SEPSEMICOLON
            | SEPSEMICOLON
    '''
def p_ForIncr(p):
    '''ForIncr : ExpressionStatements
    '''
def p_ExpressionStatements(p):
    '''ExpressionStatements : ExpressionStatement
                    | ExpressionStatements SEPCOMMA ExpressionStatement
    '''
def p_JumpStatement(p):
    '''JumpStatement : KEYBREAK Identifier SEPSEMICOLON
                | KEYBREAK SEPSEMICOLON
                | KEYCONTINUE IDENTIFIER SEPSEMICOLON
                | KEYCONTINUE SEPSEMICOLON
                | KEYRETURN Expression SEPSEMICOLON
                | KEYRETURN  SEPSEMICOLON
                | KEYTHROW Expression SEPSEMICOLON
    '''
def p_PrimaryExpression(p):
    '''PrimaryExpression : QualifiedName
                    | NotJustName
    '''
def p_NotJustName(p):
    '''NotJustName : SpecialName
                | NewAllocationExpression
                | ComplexPrimary
    '''
def p_ComplexPrimary(p):
    '''ComplexPrimary : SEPLEFTBRACE Expression SEPRIGHTBRACE
            | ComplexPrimaryNoParenthesis
    '''
def p_ComplexPrimaryNoParenthesis(p):
    '''ComplexPrimaryNoParenthesis : LITERAL
                            | BooleanLiteral
                            | IntegerLiteral
                            | FloatingLiteral
                            | CharacterLiteral
                            | StringLiteral
                            | ArrayAccess
                            | FieldAccess
                            | MethodCall
    '''
def p_ArrayAccess(p):
    '''ArrayAccess : QualifiedName SEPLEFTSQBR Expression SEPRIGHTSQBR
                | ComplexPrimary SEPLEFTSQBR Expression SEPRIGHTSQBR
    '''
def p_FieldAcess(p):
    '''FieldAccess : NotJustName SEPDOT Identifier
            | RealPostfixExpression SEPDOT Identifier
            | QualifiedName SEPDOT KEYTHIS
            | QualifiedName SEPDOT KEYCLASS
            | PrimitiveType SEPDOT KEYCLASS
    '''
def p_MethodCall(p):
    ''' MethodCall : MethodAccess SEPLEFTBRACE ArgumentList SEPRIGHTBRACE
            | MethodAccess SEPLEFTBRACE SEPRIGHTBRACE
    '''
def p_MethodAccess(p):
    ''' MethodAccess : ComplexPrimaryNoParenthesis
                | SpecialName
                | QualifiedName
    '''
def p_SpecialName(p):
    '''SpecialName : KEYTHIS
    '''
def p_ArgumentList(p):
    '''ArgumentList : Expression
            | ArgumentList SEPCOMMA Expression
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