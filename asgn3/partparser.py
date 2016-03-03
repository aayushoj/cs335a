#!/usr/bin/python
import ply.lex as lex
import sys
import ply.yacc as yacc
from latestlexer import tokens
import logging
# print tokens
nonterminals=[]
output=[]
countg = 0
revoutput=[]
finalout=[]
# def p_program(p):
#     '''program : Importstatements '''


    
def valuate(line,x):
    if output[line][x] in nonterminals:
        return output[line][x]
    else:
        return output[line][x].value

def p_CompilationUnit(p):
    '''CompilationUnit : ProgramFile
    '''
    revoutput.append(p.slice)

def p_ProgramFile(p):
    ''' ProgramFile : Importstatements TypeDeclarationOptSemi
                | Importstatements
                | TypeDeclarationOptSemi
    '''
    revoutput.append(p.slice)

def p_Importstatements(p):
    '''Importstatements : Importstatement
                    | Importstatements Importstatement
    '''
    revoutput.append(p.slice)
def p_Importstatement(p):
    '''Importstatement : KEYIMPORT QualifiedName Semicolons
                    | KEYIMPORT QualifiedName SEPDOT OPMULTIPLY Semicolons
    '''
    revoutput.append(p.slice)

def p_QualifiedName(p):
    '''QualifiedName : Identifier
                | QualifiedName SEPDOT Identifier
    '''
    revoutput.append(p.slice)

def p_Semicolons(p):
    '''Semicolons : SEPSEMICOLON
                | Semicolons SEPSEMICOLON 
    '''
    revoutput.append(p.slice)
def p_TypeSpecifier(p):
    '''TypeSpecifier : TypeName 
            | TypeName Dims              
    '''
    revoutput.append(p.slice)
#don't know what is Dims
def p_TypeName(p):
    '''TypeName : PrimitiveType
            | QualifiedName
    '''
    revoutput.append(p.slice)
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
    revoutput.append(p.slice)
# def p_ClassNameList(p):
#     '''ClassNameList : QualifiedName
#                  | ClassNameList SEPCOMMA QualifiedName
#     '''

def p_TypeDeclarationOptSemi(p):
    '''TypeDeclarationOptSemi : TypeDeclaration
                    | TypeDeclaration Semicolons
    '''
    revoutput.append(p.slice)
def p_TypeDeclaration(p):
    '''TypeDeclaration : ClassHeader SEPLEFTPARAN FieldDeclarations SEPRIGHTPARAN
                    | ClassHeader SEPLEFTPARAN SEPRIGHTPARAN
    '''
    revoutput.append(p.slice)
def p_ClassHeader(p):
    '''ClassHeader : Modifiers ClassWord Identifier
                | ClassWord Identifier
    '''
    revoutput.append(p.slice)
def p_ClassWord(p):
    '''ClassWord : KEYCLASS'''
    revoutput.append(p.slice)
def p_FieldDeclarations(p):
    '''FieldDeclarations : FieldDeclarationOptSemi
                    | FieldDeclarations FieldDeclarationOptSemi
    '''
    revoutput.append(p.slice)
def p_FieldDeclarationOptSemi(p):
    '''FieldDeclarationOptSemi : FieldDeclaration
                               | FieldDeclaration Semicolons
    '''
    revoutput.append(p.slice)
def p_FieldDeclaration(p):
    '''FieldDeclaration : FieldVariableDeclaration SEPSEMICOLON
                        | MethodDeclaration
                        | ConstructorDeclaration
                        | StaticInitializer
                        | NonStaticInitializer
                        | TypeDeclaration 
    '''
    revoutput.append(p.slice)
def p_FieldVariableDeclaration(p):
    '''FieldVariableDeclaration : Modifiers TypeSpecifier VariableDeclarators
                                | TypeSpecifier VariableDeclarators
    '''
    revoutput.append(p.slice)
def p_VariableDeclarators(p):
    '''VariableDeclarators : VariableDeclarator
                            | VariableDeclarators SEPCOMMA VariableDeclarator
    '''
    revoutput.append(p.slice)
def p_VariableDeclarator(p):
    ''' VariableDeclarator : DeclaratorName
                            | DeclaratorName OPEQUAL VariableInitializer
    '''
    revoutput.append(p.slice)

def p_VariableInitializer(p):
    '''VariableInitializer : Expression
                            | SEPLEFTPARAN SEPRIGHTPARAN
                            | SEPLEFTPARAN ArrayInitializers SEPRIGHTPARAN
    '''
    revoutput.append(p.slice)
def p_ArrayInitializers(p):
    '''ArrayInitializers : VariableInitializer
                            | ArrayInitializers SEPCOMMA VariableInitializer
                            | ArrayInitializers SEPCOMMA
    '''
    revoutput.append(p.slice)
def p_MethodDeclaration(p):
    '''MethodDeclaration : Modifiers TypeSpecifier MethodDeclarator        MethodBody
                        | TypeSpecifier MethodDeclarator        MethodBody
    '''
    revoutput.append(p.slice)
def p_MethodDeclarator(p):
    '''MethodDeclarator : DeclaratorName SEPLEFTBRACE ParameterList SEPRIGHTBRACE
                    | DeclaratorName SEPLEFTBRACE SEPRIGHTBRACE
                    | MethodDeclarator OP_DIM
    '''
    revoutput.append(p.slice)
def p_ParameterList(p):
    '''ParameterList : Parameter
                    | ParameterList SEPCOMMA Parameter
    '''
    revoutput.append(p.slice)
def p_Parameter(p):
    '''Parameter : TypeSpecifier DeclaratorName
       '''
    revoutput.append(p.slice)
def p_DeclaratorName(p):
    '''DeclaratorName : Identifier
                    | DeclaratorName OP_DIM
    '''
    revoutput.append(p.slice)
# def p_Throws(p):
#     '''Throws : THROWS ClassNameList'''

def p_MethodBody(p):
    '''MethodBody : Block
                | SEPSEMICOLON
    '''
    revoutput.append(p.slice)
def p_ConstructorDeclaration(p):
    '''ConstructorDeclaration : Modifiers ConstructorDeclarator Block
                        | ConstructorDeclarator Block
    '''
    revoutput.append(p.slice)
def p_ConstructorDeclarator(p):
    '''ConstructorDeclarator : Identifier SEPLEFTBRACE ParameterList SEPRIGHTBRACE
                            | Identifier SEPLEFTBRACE SEPRIGHTBRACE
    '''

def p_StaticInitializer(p):
    '''StaticInitializer : KEYSTATIC Block
    '''

def p_NonStaticInitializer(p):
    '''NonStaticInitializer : Block
    '''



##############################################################################################3
def p_Modifiers(p):
    '''Modifiers : Modifier
                | Modifiers Modifier
    '''
    revoutput.append(p.slice)
def p_Modifier(p):
    '''Modifier : KEYPUBLIC
                | KEYPROTECTED
                | KEYPRIVATE
                | KEYSTATIC
    '''
    revoutput.append(p.slice)
def p_Block(p):
    '''Block : SEPLEFTPARAN LocalVariableDeclarationsAndStatements SEPRIGHTPARAN
            | SEPLEFTPARAN SEPRIGHTPARAN 
    '''
    revoutput.append(p.slice)
def p_LocalVariableDeclarationsAndStatements(p):
    '''LocalVariableDeclarationsAndStatements : LocalVariableDeclarationOrStatement
                        | LocalVariableDeclarationsAndStatements LocalVariableDeclarationOrStatement
    '''
    revoutput.append(p.slice)
def p_LocalVariableDeclarationOrStatement(p):
    '''LocalVariableDeclarationOrStatement : LocalVariableDeclarationStatement
                                | Statement
    '''
    revoutput.append(p.slice)
def p_LocalVariableDeclarationStatement(p):
    '''LocalVariableDeclarationStatement : TypeSpecifier VariableDeclarators  SEPSEMICOLON
    '''
    revoutput.append(p.slice)
def p_Statement(p):
    '''Statement : EmptyStatement
                | ExpressionStatement SEPSEMICOLON
                | SelectionStatement
                | IterationStatement
                | JumpStatement
                | Block
    '''
    revoutput.append(p.slice)
def p_EmptyStatement(p):
    ''' EmptyStatement : SEPSEMICOLON
    '''
    revoutput.append(p.slice)
def p_ExpressionStatement(p):
    '''ExpressionStatement : Expression
    '''
    
def p_SelectionStatement(p):
    '''SelectionStatement : KEYIF SEPLEFTBRACE Expression SEPRIGHTBRACE Statement 
                        | KEYIF SEPLEFTBRACE Expression SEPRIGHTBRACE Statement KEYELSE Statement
    '''
    revoutput.append(p.slice)
def p_IterationStatement(p):
    '''IterationStatement : KEYWHILE SEPLEFTBRACE Expression SEPRIGHTBRACE Statement
                        | KEYFOR SEPLEFTBRACE ForInt ForExpr ForIncr SEPRIGHTBRACE Statement
                        | KEYFOR SEPLEFTBRACE ForInt ForExpr SEPRIGHTBRACE Statement
    '''
    revoutput.append(p.slice)
def p_ForInt(p):
    '''ForInt : ExpressionStatements SEPSEMICOLON
            | LocalVariableDeclarationStatement
            | SEPSEMICOLON
    '''
    revoutput.append(p.slice)
def p_ForExpr(p):
    '''ForExpr : Expression SEPSEMICOLON
            | SEPSEMICOLON
    '''
    revoutput.append(p.slice)
def p_ForIncr(p):
    '''ForIncr : ExpressionStatements
    '''
    revoutput.append(p.slice)
def p_ExpressionStatements(p):
    '''ExpressionStatements : ExpressionStatement
                    | ExpressionStatements SEPCOMMA ExpressionStatement
    '''
    revoutput.append(p.slice)
def p_JumpStatement(p):
    '''JumpStatement : KEYBREAK Identifier SEPSEMICOLON
                | KEYBREAK SEPSEMICOLON
                | KEYCONTINUE Identifier SEPSEMICOLON
                | KEYCONTINUE SEPSEMICOLON
                | KEYRETURN Expression SEPSEMICOLON
                | KEYRETURN  SEPSEMICOLON
                | KEYTHROW Expression SEPSEMICOLON
    '''
    revoutput.append(p.slice)
def p_PrimaryExpression(p):
    '''PrimaryExpression : QualifiedName
                    | NotJustName
    '''
    revoutput.append(p.slice)
def p_NotJustName(p):
    '''NotJustName : SpecialName
                | NewAllocationExpression
                | ComplexPrimary
    '''
    revoutput.append(p.slice)
def p_ComplexPrimary(p):
    '''ComplexPrimary : SEPLEFTBRACE Expression SEPRIGHTBRACE
            | ComplexPrimaryNoParenthesis
    '''
    revoutput.append(p.slice)
def p_ComplexPrimaryNoParenthesis(p):
    '''ComplexPrimaryNoParenthesis : BooleanLiteral
                            | IntegerLiteral
                            | FloatingLiteral
                            | CharacterLiteral
                            | StringLiteral
                            | ArrayAccess
                            | FieldAccess
                            | MethodCall
    '''
    revoutput.append(p.slice)
def p_ArrayAccess(p):
    '''ArrayAccess : QualifiedName SEPLEFTSQBR Expression SEPRIGHTSQBR
                | ComplexPrimary SEPLEFTSQBR Expression SEPRIGHTSQBR
    '''
    revoutput.append(p.slice)
def p_FieldAcess(p):
    '''FieldAccess : NotJustName SEPDOT Identifier
            | RealPostfixExpression SEPDOT Identifier
            | QualifiedName SEPDOT KEYTHIS
            | QualifiedName SEPDOT KEYCLASS
            | PrimitiveType SEPDOT KEYCLASS
    '''
    revoutput.append(p.slice)
def p_MethodCall(p):
    ''' MethodCall : MethodAccess SEPLEFTBRACE ArgumentList SEPRIGHTBRACE
            | MethodAccess SEPLEFTBRACE SEPRIGHTBRACE
    '''
    revoutput.append(p.slice)
def p_MethodAccess(p):
    ''' MethodAccess : ComplexPrimaryNoParenthesis
                | SpecialName
                | QualifiedName
    '''
    revoutput.append(p.slice)
def p_SpecialName(p):
    '''SpecialName : KEYTHIS
    '''
    revoutput.append(p.slice)
def p_ArgumentList(p):
    '''ArgumentList : Expression
            | ArgumentList SEPCOMMA Expression
    '''
    revoutput.append(p.slice)
def p_NewAllocationExpression(p):
    '''NewAllocationExpression : PlainNewAllocationExpression
                    | QualifiedName SEPDOT PlainNewAllocationExpression
    '''
    revoutput.append(p.slice)
def p_PlainNewAllocationExpression(p):
    '''PlainNewAllocationExpression :  ArrayAllocationExpression
                        | ClassAllocationExpression
                        | ArrayAllocationExpression SEPLEFTPARAN SEPRIGHTPARAN
                        | ClassAllocationExpression SEPLEFTPARAN SEPRIGHTPARAN
                        | ArrayAllocationExpression SEPLEFTPARAN ArrayInitializers SEPRIGHTPARAN
                        | ClassAllocationExpression SEPLEFTPARAN FieldDeclarations SEPRIGHTPARAN
    '''
    revoutput.append(p.slice)
def p_ClassAllocationExpression(p):
    '''ClassAllocationExpression : KEYNEW TypeName SEPLEFTBRACE ArgumentList SEPRIGHTBRACE
                        | KEYNEW TypeName SEPLEFTBRACE SEPRIGHTBRACE
    '''
    revoutput.append(p.slice)
def p_ArrayAllocationExpression(p):
    '''ArrayAllocationExpression : KEYNEW TypeName DimExprs Dims
                            | KEYNEW TypeName DimExprs
                            | KEYNEW TypeName Dims
    '''
    revoutput.append(p.slice)
def p_DimExprs(p):
    '''DimExprs : DimExpr
                | DimExprs DimExpr
    '''
    revoutput.append(p.slice)
def p_DimExpr(p):
    '''DimExpr : SEPLEFTSQBR Expression SEPRIGHTSQBR
    '''
    revoutput.append(p.slice)
def p_Dims(p):
    '''Dims : OP_DIM
            | Dims OP_DIM
    '''
    revoutput.append(p.slice)
def p_PostfixExpression(p):
    '''PostfixExpression : PrimaryExpression
                    | RealPostfixExpression
    '''
    revoutput.append(p.slice)
def p_RealPostfixExpression(p):
    '''RealPostfixExpression : PostfixExpression OPINCREMENT
                    | PostfixExpression OPDECREMENT
    '''
    revoutput.append(p.slice)
def p_UnaryExpression(p):
    '''UnaryExpression : OPINCREMENT UnaryExpression
                | OPDECREMENT UnaryExpression
                | ArithmeticUnaryOperator CastExpression
                | LogicalUnaryExpression
    '''
    revoutput.append(p.slice)
def p_LogicalUnaryExpression(p):
    '''LogicalUnaryExpression : PostfixExpression
                        | LogicalUnaryOperator UnaryExpression
    '''
    revoutput.append(p.slice)
def p_LogicalUnaryOperator(p):
    '''LogicalUnaryOperator : OPTILDE
                         | OPNOT 
    '''
    revoutput.append(p.slice)
def p_ArithmeticUnaryOperator(p):
    '''ArithmeticUnaryOperator : OPPLUS
                            | OPMINUS
    '''
    revoutput.append(p.slice)
def p_CastExpression(p) :
    ''' CastExpression : UnaryExpression
                | SEPLEFTBRACE PrimitiveTypeExpression SEPRIGHTBRACE CastExpression
                | SEPLEFTBRACE ClassTypeExpression SEPRIGHTBRACE CastExpression
                | SEPLEFTBRACE Expression SEPRIGHTBRACE LogicalUnaryExpression
    '''
    revoutput.append(p.slice)
def p_PrimitiveTypeExpression(p):
    '''PrimitiveTypeExpression : PrimitiveType
                    | PrimitiveType Dims
    '''
    revoutput.append(p.slice)
def p_ClassTypeExpression(p):
    '''ClassTypeExpression : QualifiedName Dims
    '''
    revoutput.append(p.slice)
def p_MultiplicativeExpression(p):
    '''MultiplicativeExpression : CastExpression
                    | MultiplicativeExpression OPMULTIPLY CastExpression
                    | MultiplicativeExpression OPDIVIDE CastExpression
                    | MultiplicativeExpression OPMOD CastExpression
    '''
    revoutput.append(p.slice)
def p_AdditiveExpression(p):
    '''AdditiveExpression : MultiplicativeExpression
                        | AdditiveExpression OPPLUS MultiplicativeExpression
                        | AdditiveExpression OPMINUS MultiplicativeExpression
    '''
    revoutput.append(p.slice)
def p_ShiftExpression(p):
    '''ShiftExpression : AdditiveExpression
                    | ShiftExpression OPLEFTSHIFT AdditiveExpression
                    | ShiftExpression OPRIGHTSHIFT AdditiveExpression
                    | ShiftExpression OPLOGICALSHIFT AdditiveExpression
    '''
    revoutput.append(p.slice)
def p_RelationalExpression(p):
    '''RelationalExpression : ShiftExpression
                        | RelationalExpression OPLESSER ShiftExpression
                        | RelationalExpression OPGREATER ShiftExpression
                        | RelationalExpression OPLESSEQ ShiftExpression
                        | RelationalExpression OPGREATEQ ShiftExpression
                        | RelationalExpression OPINSTANCEOF TypeSpecifier
    '''
    revoutput.append(p.slice)
def p_EqualityExpression(p):
    '''EqualityExpression : RelationalExpression
                        | EqualityExpression OPCHECKEQ RelationalExpression
                        | EqualityExpression OPNOTEQ RelationalExpression
    '''
    revoutput.append(p.slice)
def p_AndExpression(p):
    '''AndExpression : EqualityExpression
                    | AndExpression OPBINAND EqualityExpression
    '''
    revoutput.append(p.slice)
def p_ExclusiveOrExpression(p):
    '''ExclusiveOrExpression : AndExpression
                    | ExclusiveOrExpression OPXOR AndExpression
    '''
    revoutput.append(p.slice)
def p_InclusiveOrExpression(p):
    '''InclusiveOrExpression : ExclusiveOrExpression
                        | InclusiveOrExpression OPBINOR ExclusiveOrExpression
    '''
    revoutput.append(p.slice)
def p_ConditionalAndExpression(p):
    '''ConditionalAndExpression : InclusiveOrExpression
                            | ConditionalAndExpression OPAND InclusiveOrExpression
    '''
    revoutput.append(p.slice)
def p_ConditionalOrExpression(p):
    '''ConditionalOrExpression : ConditionalAndExpression
                        | ConditionalOrExpression OPOR ConditionalAndExpression
    '''
    revoutput.append(p.slice)
def p_ConditionalExpression(p):
    ''' ConditionalExpression : ConditionalOrExpression
                        | ConditionalOrExpression OPTERNARY Expression SEPCOLON ConditionalExpression
    '''
    revoutput.append(p.slice)
def p_AssignmentExpression(p):
    '''AssignmentExpression : ConditionalExpression
                        | UnaryExpression AssignmentOperator AssignmentExpression
    '''
    revoutput.append(p.slice)
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
    revoutput.append(p.slice)
def p_Expression(p):
    '''Expression : AssignmentExpression
    '''
    revoutput.append(p.slice)
def p_error(p):
    if p == None:
        print "You missed something at the end"
    else:
        print "Syntax error in input line!"

def rightderivation(prefx,sufx):
    global finalout
    global countg
    lcount=countg
    count=0
    last=-1
    for i in range(1,len(output[lcount])):
        if not (output[lcount][i] in nonterminals):
            count+=1
        else:
            last=max(last,i)
    pre=" "
    for i in range(1,len(output[lcount])):
        if(i==last):
            pre=pre+"<b> "+str(valuate(lcount,i))  +" </b>"
        else:
            pre=pre+str(valuate(lcount,i))
        if not(i==len(output[lcount])-1):
            pre += " "
    if(count==len(output[lcount])-1):
        countg+=1
        return pre
    finalout.append(prefx + pre +sufx)
    suf=" "
    for x in range(len(output[lcount])-1,0,-1):
        if not (output[lcount][x] in nonterminals):
            suf = valuate(lcount,x)+suf
            continue
        pre = prefx
        for i in range(1,x):
            pre=pre+str(valuate(lcount,i))+" "
        countg+=1
        suf = str(rightderivation(pre,suf+sufx)) + suf
        countg-=1
        finalout.append(pre +suf +sufx)
    countg+=1
    return suf

def truncfinal():
    global finalout
    i=0
    while i < len(finalout)-1:
        if(removeempty(finalout[i].split(' '))==removeempty(finalout[i+1].split(' '))):
            del finalout[i+1]
        else:
            i+=1


def removeempty(lis):
    i=0
    while i < len(lis):
        if(lis[i]=='' or lis[i]=='<br>' or lis[i]=='</br>'):
            del lis[i]
        else:
            i+=1
    return lis

yacc.yacc()

# while 1:
#     try:
#         s = raw_input('calc > ')
#     except EOFError:
#         break
#     if not s: continue
#     yacc.parse(s)

a=open(sys.argv[1])
a=a.read()
a=a.split('\n')
for s in a:
    #     s = raw_input('calc > ')
    # except EOFError:
    #     break
    if not (s == ''): 
        yacc.parse(s)
for i in range(len(revoutput)):
    nonterminals.append(revoutput[i][0])
for i in range(len(revoutput)-1,-1,-1):
    output.append(revoutput[i])
print  "<b> "+ str(output[0][0])+"</b> "
rightderivation("","")
truncfinal()
for i in finalout:
    sp=i.split(' ')
    st=""
    for j in range(len(sp)):
        if sp[j]=='':
            continue
        else:
            st+=sp[j]+ " "
    print st + "</br>"


        