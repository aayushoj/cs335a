#!/usr/bin/python
import ply.lex as lex
import sys
import ply.yacc as yacc
from latestlexer import tokens
import logging
# print tokens

# def p_program(p):
#     '''program : Importstatements '''

def p_CompilationUnit(p):
    '''CompilationUnit : ProgramFile
    '''

def p_ProgramFile(p):
    ''' ProgramFile : Importstatements TypeDeclarationOptSemi
                | Importstatements
                | TypeDeclarationOptSemi
    '''

def p_Importstatements(p):
    '''Importstatements : Importstatement
                    | Importstatements Importstatement
    '''
def p_Importstatement(p):
    '''Importstatement : KEYIMPORT QualifiedName Semicolons
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
#     '''ClassNameList : QualifiedName
#                  | ClassNameList SEPCOMMA QualifiedName
#     '''

def p_TypeDeclarationOptSemi(p):
    '''TypeDeclarationOptSemi : TypeDeclaration
                    | TypeDeclaration Semicolons
    '''
def p_TypeDeclaration(p):
    '''TypeDeclaration : ClassHeader SEPLEFTPARAN FieldDeclarations SEPRIGHTPARAN
                    | ClassHeader SEPLEFTPARAN SEPRIGHTPARAN
    '''
def p_ClassHeader(p):
    '''ClassHeader : Modifiers ClassWord Identifier
                | ClassWord Identifier
    '''
def p_ClassWord(p):
    '''ClassWord : KEYCLASS'''

def p_FieldDeclarations(p):
    '''FieldDeclarations : FieldDeclarationOptSemi
                    | FieldDeclarations FieldDeclarationOptSemi
    '''
def p_FieldDeclarationOptSemi(p):
    '''FieldDeclarationOptSemi : FieldDeclaration
                               | FieldDeclaration Semicolons
    '''
def p_FieldDeclaration(p):
    '''FieldDeclaration : FieldVariableDeclaration SEPSEMICOLON
                        | MethodDeclaration
                        | ConstructorDeclaration
                        | StaticInitializer
                        | NonStaticInitializer
                        | TypeDeclaration 
    '''

def p_FieldVariableDeclaration(p):
    '''FieldVariableDeclaration : Modifiers TypeSpecifier VariableDeclarators
                                | TypeSpecifier VariableDeclarators
    '''
def p_VariableDeclarators(p):
    '''VariableDeclarators : VariableDeclarator
                            | VariableDeclarators SEPCOMMA VariableDeclarator
    '''
def p_VariableDeclarator(p):
    ''' VariableDeclarator : DeclaratorName
                            | DeclaratorName OPEQUAL VariableInitializer
    '''

def p_VariableInitializer(p):
    '''VariableInitializer : Expression
                            | SEPLEFTPARAN SEPRIGHTPARAN
                            | SEPLEFTPARAN ArrayInitializers SEPRIGHTPARAN
    '''
def p_ArrayInitializers(p):
    '''ArrayInitializers : VariableInitializer
                            | ArrayInitializers SEPCOMMA VariableInitializer
                            | ArrayInitializers SEPCOMMA
    '''

def p_MethodDeclaration(p):
    '''MethodDeclaration : Modifiers TypeSpecifier MethodDeclarator        MethodBody
                        | TypeSpecifier MethodDeclarator        MethodBody
    '''

def p_MethodDeclarator(p):
    '''MethodDeclarator : DeclaratorName SEPLEFTBRACE ParameterList SEPRIGHTBRACE
                    | DeclaratorName SEPLEFTBRACE SEPRIGHTBRACE
                    | MethodDeclarator OP_DIM
    '''

def p_ParameterList(p):
    '''ParameterList : Parameter
                    | ParameterList SEPCOMMA Parameter
    '''
    
def p_Parameter(p):
    '''Parameter : TypeSpecifier DeclaratorName
       '''
def p_DeclaratorName(p):
    '''DeclaratorName : Identifier
                    | DeclaratorName OP_DIM
    '''
# def p_Throws(p):
#     '''Throws : THROWS ClassNameList'''

def p_MethodBody(p):
    '''MethodBody : Block
                | SEPSEMICOLON
    '''

def p_ConstructorDeclaration(p):
    '''ConstructorDeclaration : Modifiers ConstructorDeclarator Block
                        | ConstructorDeclarator Block
    '''

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
                | LabelStatement
                | SelectionStatement
                | IterationStatement
                | JumpStatement
                | GuardingStatement
                | Block
    '''
def p_EmptyStatement(p):
    ''' EmptyStatement : SEPSEMICOLON
    '''
def p_LabelStatement(p):
    ''' LabelStatement : Identifier SEPCOLON
                | KEYCASE ConstantExpression SEPCOLON
                | KEYDEFAULT SEPCOLON
    '''
def p_ExpressionStatement(p):
    '''ExpressionStatement : Expression
    '''
precedence = (
    ('right', 'THAN', 'KEYELSE'),
)
def p_SelectionStatement(p):
    '''SelectionStatement : KEYIF SEPLEFTBRACE Expression SEPRIGHTBRACE Statement %prec THAN
                        | KEYIF SEPLEFTBRACE Expression SEPRIGHTBRACE Statement KEYELSE Statement
    '''
def p_IterationStatement(p):
    '''IterationStatement : KEYWHILE SEPLEFTBRACE Expression SEPRIGHTBRACE Statement
                        | KEYFOR SEPLEFTBRACE ForInt ForExpr ForIncr SEPRIGHTBRACE Statement
                        | KEYFOR SEPLEFTBRACE ForInt ForExpr SEPRIGHTBRACE Statement
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
                | KEYCONTINUE Identifier SEPSEMICOLON
                | KEYCONTINUE SEPSEMICOLON
                | KEYRETURN Expression SEPSEMICOLON
                | KEYRETURN  SEPSEMICOLON
                | KEYTHROW Expression SEPSEMICOLON
    '''
def p_GuardingStatement(p):
    '''GuardingStatement : KEYTRY Block Finally
                        | KEYTRY Block Catches
                        | KEYTRY Block Catches Finally
    '''
def p_Catches(p):
    '''Catches : Catch
            | Catches Catch
    '''
def p_Catch(p):
    '''Catch : CatchHeader Block
    '''
def p_CatchHeader(p):
    '''CatchHeader : KEYCATCH SEPLEFTBRACE TypeSpecifier Identifier SEPRIGHTBRACE
                | KEYCATCH SEPLEFTBRACE TypeSpecifier SEPRIGHTBRACE
    '''
def p_Finally(p):
    '''Finally : KEYFINALLY Block
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
    '''ComplexPrimaryNoParenthesis : BooleanLiteral
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
    '''Dims : OP_DIM
            | Dims OP_DIM
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
                            | ConditionalAndExpression OPAND InclusiveOrExpression
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

# parser = yacc.yacc()

# while 1:
#     try:
#         s = raw_input('calc > ')
#     except EOFError:
#         break
#     if not s: continue
#     yacc.parse(s)
logging.basicConfig(
    level = logging.DEBUG,
    filename = "parselog.txt",
    filemode = "w"
)

log = logging.getLogger()
parser = yacc.yacc()


if __name__ == "__main__" : 

    s = open(sys.argv[1],'r')
    data = s.read()
    data+= "\n"
    s.close()
    result = parser.parse(data,debug=log)


    import re
    from collections import defaultdict

    #obtain the lines with the productions used
    outfile = open("actions.txt",'w')
    with open("parselog.txt") as f:
        for line in f:
            if re.match("INFO:root:Action(.*)", line):
                outfile.write(line)


    #clean the productions to give the required information
    infile = "actions.txt"
    outfile = "treefile.txt"

    delete_list2 = ["rule [","] with"]

    fin = open(infile)
    fout = open(outfile, "w+")
    for line in fin:
       matches = re.findall('rule \[(.*)\] with', line)
       #for word in delete_list2:
       #    matches[0] = matches[0].replace(word, "")
       fout.write(matches[0])
       #line = line[1:len(line)-2]
       #fout.write(line)    
       fout.write("\n")
    fin.close()
    fout.close()



    #use the clean productions and build the dot file
    nodes = defaultdict(list)
    #nodes = dict()
    nodeNum = 1

    infile = sys.argv[1]
    outfile = infile[0:len(infile)-3]
    outfile+=".dot"
    outfile = outfile.split("/")[-1]

    fout = open(outfile,"w")

    fout.write("""digraph G {
    graph [ordering="out"];
    """)
    fout.write("\n")

    for line in open("treefile.txt"):
        columns = line.split(" ")
        fout.write("node%d [ label = \"%s\" ]; " % (nodeNum,columns[0]))
        fout.write("\n")
        lhsNum = nodeNum
        nodeNum += 1
        edges = []
        for i in range(1,len(columns)-1):
            i = len(columns)  - i
        columns[i] = columns[i].rstrip()
        edge = ""
        if columns[i] in nodes:
            edge += "node" + str(lhsNum) + " -> node" + str(nodes[columns[i]].pop(len(nodes[columns[i]])-1)) + ";"
            if len(nodes[columns[i]]) == 0:
               del nodes[columns[i]]
        else:
            fout.write("node%d [ label = \"Token \n %s\" ]; " % (nodeNum,columns[i]))
            fout.write("\n")
            edge += "node" + str(lhsNum) + " -> node" + str(nodeNum) + ";"
            #print "node%d -> node%d;" %(lhsNum,nodeNum)
            nodeNum += 1
        edges.append(edge)
        nodes[columns[0]].append(lhsNum)
        while edges:
           fout.write(edges.pop(len(edges)-1))
           fout.write("\n")

    fout.write( "}" )
    fout.write("\n")
    fout.close()