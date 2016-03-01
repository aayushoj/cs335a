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
def p_NewAllocationExpression(p):
    '''NewAllocationExpression : PlainNewAllocationExpression
                    | QualifiedName SEPDOT PlainNewAllocationExpression
    '''
def p_PlainNewAllocationExpression(p):
    '''PlainNewAllocationExpression :  ArrayAllocationExpression
                        | ClassAllocationExpression
                        | ArrayAllocationExpression SEPLEFTPARAN SEPRIGHTPARAN
                        | ClassAllocationExpression SEPLEFTPARAN SEPRIGHTPARAN
                        | ArrayAllocationExpression SEPLEFTPARAN ArrayInitializers SEPRIGHTPARAN
                        | ClassAllocationExpression SEPLEFTPARAN FieldDeclarations SEPRIGHTPARAN
    '''
def p_ClassAllocationExpression(p):
    '''ClassAllocationExpression : KEYNEW TypeName SEPLEFTBRACE ArgumentList SEPRIGHTBRACE
                        | KEYNEW TypeName SEPLEFTBRACE SEPRIGHTBRACE
    '''
def p_ArrayAllocationExpression(p):
    '''ArrayAllocationExpression : KEYNEW TypeName DimExprs Dims
                            | KEYNEW TypeName DimExprs
                            | KEYNEW TypeName Dims
    '''
def p_DimExprs(p):
    '''DimExprs : DimExpr
                | DimExprs DimExpr
    '''
def p_DimExpr(p):
    '''DimExpr : SEPLEFTSQBR Expression SEPRIGHTSQBR
    '''
def p_Dims(p):
    '''Dims : SEPLEFTSQBR SEPRIGHTSQBR
            | Dims SEPLEFTSQBR SEPRIGHTSQBR
    '''
def p_PostfixExpression(p):
    '''PostfixExpression : PrimaryExpression
                    | RealPostfixExpression
    '''
def p_RealPostfixExpression(p):
    '''RealPostfixExpression : PostfixExpression OPINCREMENT
                    | PostfixExpression OPDECREMENT
    '''
def p_UnaryExpression(p):
    '''UnaryExpression : OPINCREMENT UnaryExpression
                | OPDECREMENT UnaryExpression
                | ArithmeticUnaryOperator CastExpression
                | LogicalUnaryExpression
    '''
def p_LogicalUnaryExpression(p):
    '''LogicalUnaryExpression : PostfixExpression
                        | LogicalUnaryOperator UnaryExpression
    '''
def p_LogicalUnaryOperator(p):
    '''LogicalUnaryOperator : OPTILDE
                         | OPNOT 
    '''
def p_ArithmeticUnaryOperator(p):
    '''ArithmeticUnaryOperator : OPPLUS
                            | OPMINUS
    '''
def p_CastExpression(p) :
    ''' CastExpression : UnaryExpression
                | SEPLEFTBRACE PrimitiveTypeExpression SEPRIGHTBRACE CastExpression
                | SEPLEFTBRACE ClassTypeExpression SEPRIGHTBRACE CastExpression
                | SEPLEFTBRACE Expression SEPRIGHTBRACE LogicalUnaryExpression
    '''
def p_PrimitiveTypeExpression(p):
    '''PrimitiveTypeExpression : PrimitiveType
                    | PrimitiveType Dims
    '''
def p_ClassTypeExpression(p):
    '''ClassTypeExpression : QualifiedName Dims
    '''
def p_MultiplicativeExpression(p):
    '''MultiplicativeExpression : CastExpression
                    | MultiplicativeExpression OPMULTIPLY CastExpression
                    | MultiplicativeExpression OPDIVIDE CastExpression
                    | MultiplicativeExpression OPMOD CastExpression
    '''
def p_AdditiveExpression(p):
    '''AdditiveExpression : MultiplicativeExpression
                        | AdditiveExpression OPPLUS MultiplicativeExpression
                        | AdditiveExpression OPMINUS MultiplicativeExpression
    '''
def p_ShiftExpression(p):
    '''ShiftExpression : AdditiveExpression
                    | ShiftExpression OPLEFTSHIFT AdditiveExpression
                    | ShiftExpression OPRIGHTSHIFT AdditiveExpression
                    | ShiftExpression OPLOGICALSHIFT AdditiveExpression
    '''
def p_RelationalExpression(p):
    '''RelationalExpression : ShiftExpression
                        | RelationalExpression OPLESSER ShiftExpression
                        | RelationalExpression OPGREATER ShiftExpression
                        | RelationalExpression OPLESSEQ ShiftExpression
                        | RelationalExpression OPGREATEQ ShiftExpression
                        | RelationalExpression OPINSTANCEOF TypeSpecifier
    '''
def p_EqualityExpression(p):
    '''EqualityExpression : RelationalExpression
                        | EqualityExpression OPCHECKEQ RelationalExpression
                        | EqualityExpression OPNOTEQ RelationalExpression
    '''
def p_AndExpression(p):
    '''AndExpression : EqualityExpression
                    | AndExpression OPBINAND EqualityExpression
    '''
def p_ExclusiveOrExpression(p):
    '''ExclusiveOrExpression : AndExpression
                    | ExclusiveOrExpression OPXOR AndExpression
    '''
def p_InclusiveOrExpression(p):
    '''InclusiveOrExpression : ExclusiveOrExpression
                        | InclusiveOrExpression OPBINOR ExclusiveOrExpression
    '''
def p_ConditionalAndExpression(p):
    '''ConditionalAndExpression : InclusiveOrExpression
                            | ConditionalAndExpression OPBINANDEQ InclusiveOrExpression
    '''
def p_ConditionalOrExpression(p):
    '''ConditionalOrExpression : ConditionalAndExpression
                        | ConditionalOrExpression OPOR ConditionalAndExpression
    '''
def p_ConditionalExpression(p):
    ''' ConditionalExpression : ConditionalOrExpression
                        | ConditionalOrExpression OPTERNARY Expression SEPCOLON ConditionalExpression
    '''
def p_AssignmentExpression(p):
    '''AssignmentExpression : ConditionalExpression
                        | UnaryExpression AssignmentOperator AssignmentExpression
    '''
def p_AssignmentOperator(p):
    ''' AssignmentOperator : OPEQUAL
                        | OPMULTIPLYEQ
                        | OPDIVIDEEQ
                        | OPMODEQ
                        | OPPLUSEQ
                        | OPMINUSEQ
                        | OPLEFTSHIFTEQ
                        | OPRIGHTSHIFTEQ
                        | OPLOGICALSHIFTEQ
                        | OPBINANDEQ
                        | OPXOREQ
                        | OPBINOREQ
    '''
def p_Expression(p):
    '''Expression : AssignmentExpression
    '''
def p_ConstantExpression(p):
    '''ConstantExpression : ConditionalExpression
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