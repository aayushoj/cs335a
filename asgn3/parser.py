# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables.   This is from O'Reilly's
# "Lex and Yacc", p. 63.
# -----------------------------------------------------------------------------

import sys
sys.path.insert(0,"../..")

tokens = (
    'Keyword',
    'Identifier',
    'Literals', #incomplete
    'Separator',
    'Comments',
    'Operator'    # incomplete
    # 'Alphabets',
    # 'Numeric',
    # 'Alphanum',
    # 'Special',
    # 'Graphic',
    # 'IndentifierStart'
)

# Regular expression rules for simple tokens
Alphabets = r'([a-zA-Z])'
Numeric = r'([0-9])'
Alphanum = r'([a-zA-Z0-9])'
Special = r'([\]!%\^&$*()-+={}|~[\;:<>?,./#@`_])'
Graphic = r'([a-zA-Z0-9]|'+ Special + r')'
IdentifierStart = r'([0-9a-zA-Z$_])'
Identifier = r'[a-zA-Z$_][a-zA-Z0-9$_]*'

# print(Identifier)
Keyword = r'(continue|for|new|switch|assert|default|goto|boolean|do|if|private|this|break|double|protected|byte|else|import|public|case|enum|return|catch|extends|int|short|try|char|static|void|class|long|volatile|const|float|while)'+r'[^0-9a-zA-Z$_]'

Separator = r'[;,.(){}[\] \"\']'
Comments = r'(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)|(//.*)'
Operator = r'(=|<|>|<=|>=|\+|-|\*|/|==|\+\+|--|~|!|%|<<|>>|>>>|instanceof|!=|&|\^|\||&&|\|\||[+\-*/%&\^|]=|<<=|>>=|>>>=)'

FloatingLiteral=r'(([0-9]+)?\.([0-9]+)((e|E)((\+|-)?[0-9]+))?([fFdD])?|[0-9]+(e|E)(\+|-)?[0-9]+)'
IntegerLiteral=r'[0-9]+'
BooleanLiteral=r'(true|false|TRUE|FALSE)'
CharacterLiteral=r'(\'(' + Graphic + r'|\ |\\[n\\ta"\'])\')'
StringLiteral=r'(\"(' + Graphic + r'|\ |\\[n\\ta"\'])*\")'
Literals= r'('+FloatingLiteral+r'|null|'+IntegerLiteral+r'|'+BooleanLiteral+r'|'+CharacterLiteral+r'|'+StringLiteral+r')'
Illegals = r'('+IntegerLiteral + r'[a-zA-Z]+)'

# A regular expression rule with some action code
# Note addition of self parameter since we're in a class
@TOKEN(Comments)
def t_Comments(self, t):
    self.lexer.lineno+=t.value.count('\n')
    pass
@TOKEN(Illegals)
def t_Illegals(self,t):
    print("Line :: %d  Illegal entry '%s'" %(t.lexer.lineno, t.value))
    pass

@TOKEN(Keyword)
def t_Keyword(self, t):
    self.Num_Keyword+=1;
    self.lexer.lexpos-=1;
    self.Set_Keyword.add(t.value[:-1])
    return t

@TOKEN(Identifier)
def t_Identifier(self, t):
    if(t.value in self.ReservedWords):
        t.type="Literals"
        self.Num_Literals+=1
        self.Set_Literals.add(t.value)
    else:
        self.Num_Identifier+=1
        self.Set_Identifier.add(t.value)
    return t

@TOKEN(Literals)
def t_Literals(self, t):
    self.Num_Literals+=1
    self.Set_Literals.add(t.value)
    return t

@TOKEN(Separator)
def t_Separator(self, t):
    self.Num_Separator+=1
    self.Set_Separator.add(t.value)
    return t

@TOKEN(Operator)
def t_Operator(self, t):
    self.Num_Operator+=1
    self.Set_Operator.add(t.value)
    return t


# Define a rule so we can track line numbers
def t_newline(self, t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(self, t):
    print("Line :: %d  Illegal entry '%s'" %(t.lexer.lineno, t.value))
    t.lexer.skip(1)

# Build the lexer
def build(self, **kwargs):
    self.lexer = lex.lex(module=self, **kwargs)

# Test it output
def test(self, data):
    self.lexer.input(data)
    while True:
        tok = self.lexer.token()
        if not tok:
            break
        # print(tok)



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

# dictionary of names
names = { }

def p_statement_assign(p):
    'statement : NAME "=" expression'
    names[p[1]] = p[3]

def p_statement_expr(p):
    'statement : expression'
    print p[1]

def p_expression_binop(p):
    '''expression : expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '/' expression'''
    if p[2] == '+'  : p[0] = p[1] + p[3]
    elif p[2] == '-': p[0] = p[1] - p[3]
    elif p[2] == '*': p[0] = p[1] * p[3]
    elif p[2] == '/': p[0] = p[1] / p[3]

def p_expression_uminus(p):
    "expression : '-' expression %prec UMINUS"
    p[0] = -p[2]

def p_expression_group(p):
    "expression : '(' expression ')'"
    p[0] = p[2]

def p_expression_number(p):
    "expression : NUMBER"
    p[0] = p[1]

def p_expression_name(p):
    "expression : NAME"
    try:
        p[0] = names[p[1]]
    except LookupError:
        print "Undefined name '%s'" % p[1]
        p[0] = 0

def p_error(p):
    print "Syntax error at '%s'" % p.value

import ply.yacc as yacc
yacc.yacc()

while 1:
    try:
        s = raw_input('calc > ')
    except EOFError:
        break
    if not s: continue
    yacc.parse(s)