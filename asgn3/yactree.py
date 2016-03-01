# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables.   This is from O'Reilly's
# "Lex and Yacc", p. 63.
# -----------------------------------------------------------------------------

import sys
sys.path.insert(0,"../..")

tokens = (
    'NAME','NUMBER',
    )

literals = ['=','+','-','*','/', '(',')']

# Tokens

t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print "Integer value too large", t.value
        t.value = 0
    return t

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)
    
# Build the lexer
import ply.lex as lex
lex.lex()

# Parsing rules

precedence = (
    ('left','+','-'),
    ('left','*','/'),
    ('right','UMINUS'),
    )

class Nodes:
    # def addchild(lis):
    def __init__(self, name,lis):
        self.token=name
        self.child=[]
        self.terminal=True
        if not(lis==[]):
            for x in lis:
                self.child.append(x)
            self.terminal=False

def tree(p):
    if p.child==[]:
        print p.token
        return
    for x in range(len(p.child)-1,-1,-1):
        tree(p.child[x])
    print p.token

def expand(p,prefx,sufx):
    if p.child==[]:
        return str(p.token)
    print prefx+ "<b>"+ str(p.token) +"</b>"  + sufx + "</br>"
    suf = ""
    for x in range(len(p.child)-1,-1,-1):
        pre = prefx
        for i in range(x):
            pre=pre+str(p.child[i].token)+" "
        # print "printing pre"
        # print pre
        # print "printing suf"
        # print suf
        suf = expand(p.child[x],pre,suf+sufx)+" " + suf
        if len(p.child[x].child)>1:
            print pre + suf +sufx + "</br>"
    return suf


# dictionary of names
names = { }

def p_start(p):
    'start : statement'
    # print "will print the tree"
    # tree(p[1])
    expand(p[1],"","")

def p_statement_assign(p):
    'statement : NAME "=" expression'
    names[p[1]] = p[3]
    p[1] = Nodes(p[1],[])
    p[2] = Nodes(p[2],[])
    p[0] = Nodes("statement",[p[1],p[2],p[3]])

def p_statement_expr(p):
    'statement : expression'
    p[0] = Nodes("statement",[p[1]])

def p_expression_binop(p):
    '''expression : expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '/' expression'''
    # if p[2] == '+'  : p[0] = p[1] + p[3]
    # elif p[2] == '-': p[0] = p[1] - p[3]
    # elif p[2] == '*': p[0] = p[1] * p[3]
    # elif p[2] == '/': p[0] = p[1] / p[3]
    p[2] = Nodes(p[2],[])
    p[0] = Nodes("expression",[p[1],p[2],p[3]])

def p_expression_uminus(p):
    "expression : '-' expression %prec UMINUS"
    p[1] = Nodes(p[1],[])
    p[0] = Nodes("expression",[p[1],p[2]])
    # p[0] = -p[2]

def p_expression_group(p):
    "expression : '(' expression ')'"
    p[2] = Nodes(p[2],[])
    p[4] = Nodes(p[4],[])
    p[0] = Nodes("expression",[p[1],p[2],p[3]])
    # p[0] = p[2]

def p_expression_number(p):
    "expression : NUMBER"
    # p[0] = p[1]
    p[1] = Nodes(p[1],[])
    p[0] = Nodes("expression",[p[1]])

def p_expression_name(p):
    "expression : NAME"
    try:
        p[0] = names[p[1]]
    except LookupError:
        print "Undefined name '%s'" % p[1]
        p[0] = 0
    p[1] = Nodes(p[1],[])
    p[0] = Nodes("expression",[p[1]])

def p_error(p):
    print "Syntax error at '%s'" % p.value

import ply.yacc as yacc
yacc.yacc()

a=open(sys.argv[1])
a=a.read()
a=a.split('\n')
for s in a:
    #     s = raw_input('calc > ')
    # except EOFError:
    #     break
    if not (s == ''): 
        yacc.parse(s)