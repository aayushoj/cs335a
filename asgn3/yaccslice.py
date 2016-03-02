# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables.   This is from O'Reilly's
# "Lex and Yacc", p. 63.
# -----------------------------------------------------------------------------

import sys
sys.path.insert(0,"../..")
nonterminals=[]
output=[]
countg = 0
revoutput=[]

tokens = (
    'NAME','NUMBER',
    )

literals = ['=','+','-','*','/', '(',')']

# Tokens
output=[]

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

# dictionary of names
names = { }

def p_statement_assign(p):
    'statement : NAME "=" expression'
    revoutput.append(p.slice)

def p_statement_expr(p):
    'statement : expression'
    revoutput.append(p.slice)

def p_expression_binop(p):
    '''expression : expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '/' expression'''
    revoutput.append(p.slice)

def p_expression_uminus(p):
    "expression : '-' expression %prec UMINUS"
    revoutput.append(p.slice)

def p_expression_group(p):
    "expression : '(' expression ')'"
    revoutput.append(p.slice)

def p_expression_number(p):
    "expression : NUMBER"
    revoutput.append(p.slice)

def p_expression_name(p):
    "expression : NAME"
    try:
        p[0] = names[p[1]]
    except LookupError:
        print "Undefined name '%s'" % p[1]
        p[0] = 0
    revoutput.append(p.slice)

def p_error(p):
    print "Syntax error at '%s'" % p.value


def rightderivation(prefx,sufx):
    global countg
    lcount=countg
    count=0
    for i in range(1,len(output[lcount])):
        if not (output[lcount][i] in nonterminals):
            count+=1
    pre=""
    for i in range(1,len(output[lcount])):
        pre=pre+str(valuate(lcount,i))
        if not(i==len(output[lcount])-1):
            pre += " "
    if(count==len(output[lcount])-1):
        countg+=1
        return pre
    print prefx + pre +sufx
    suf=""
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
        print pre +suf +sufx
    countg+=1
    return suf

def valuate(line,x):
    if output[line][x] in nonterminals:
        return output[line][x]
    else:
        return output[line][x].value



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
# print output
for i in range(len(revoutput)):
    nonterminals.append(revoutput[i][0])
for i in range(len(revoutput)-1,-1,-1):
    output.append(revoutput[i])
print output[0][0]
rightderivation("","")
        