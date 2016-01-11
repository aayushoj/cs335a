import ply.lex as lex
import sys
from ply.lex import TOKEN


class MyLexer(object):
    # List of token names.   This is always required
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
    Special = r'([\]!%\^&*()-+={}|~[\;:"<>?,./#@`_])' + r'|' + r'\''
    Graphic = r'([a-zA-Z0-9]|'+ Special + r')'
    IdentifierStart = r'([0-9a-zA-Z$_])'
    Identifier = r'[a-zA-z$_][a-zA-Z0-9$_]*'

    # print(Identifier)
    Keyword = r'(continue|for|new|switch|assert|default|goto|boolean|do|if|private|this|break|double|protected|byte|else|import|public|case|enum|return|catch|extends|int|short|try|char|static|void|class|long|volatile|const|float|while)'

    Separator = r'[;,.(){}[\] \"\']'
    Comments = r'//[^\n]* | /[*].*[*]/'
    # incomplete
    Operator = r'(=|<|>|<=|>=|\+|-|\*|/|==|\+\+|--|~|!|%|<<|>>|>>>|instanceof|!=|&|\^|\||&&|\|\||[+\-*/%&\^|]=|<<=|>>=|>>>=)'

    IntegerLiteral=r'[0-9]+'
    FloatingLiteral=r'([0-9]+(e|E)(\+|-)?[0-9]+|([0-9]+)?\.([0-9]+)((e|E)((\+|-)?[0-9]+))?)'
    BooleanLiteral=r'(true|false|TRUE|FALSE)'
    CharacterLiteral=r'(\'(' + Graphic + r'|\ |\\[n\\ta])\')|\''
    StringLiteral=r'(\"(' + Graphic + r'|\ |\\[n\\ta])*\")|\"'
    Literals= r'('+IntegerLiteral+r'|null|'+FloatingLiteral+r'|'+BooleanLiteral+r'|'+CharacterLiteral+r'|'+StringLiteral+r')'


    # A regular expression rule with some action code
    # Note addition of self parameter since we're in a class
    @TOKEN(Keyword)
    def t_Keyword(self, t):
        return t

    @TOKEN(Identifier)
    def t_Identifier(self, t):
        return t
    @TOKEN(Literals)
    def t_Literals(self, t):
        return t

    @TOKEN(Separator)
    def t_Separator(self, t):
        return t

    @TOKEN(Comments)
    def t_Comments(self, t):
        pass

    @TOKEN(Operator)
    def t_Operator(self, t):
        return t


    # Define a rule so we can track line numbers
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # A string containing ignored characters (spaces and tabs)
    t_ignore = ' \t'

    # Error handling rule
    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
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
            print(tok)

# Build the lexer and try it out
m = MyLexer()
m.build()           # Build the lexer
filename = sys.argv[1]
f = open(filename, 'r')
data = f.read()
# print(data)
m.test(data)     # Test it
