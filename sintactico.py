import ply.yacc as yacc
from lexico import tokens  # Asegúrate de que 'yourlexer' se refiere al archivo que contiene tu lexer

# Parsing rules
def p_program(p):
    'program : function'
    p[0] = p[1]

def p_function(p):
    'function : INT ID LPAREN RPAREN LBRACE statement_list RBRACE'
    p[0] = ('function', p[2], p[6])

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement(p):
    '''statement : var_declaration
                 | return_statement'''
    p[0] = p[1]

def p_var_declaration(p):
    'var_declaration : INT ID EQUAL expression SEMICOLON'
    p[0] = ('declare', p[2], p[4])

def p_return_statement(p):
    'return_statement : RETURN expression SEMICOLON'
    p[0] = ('return', p[2])

def p_expression_binop(p):
    '''expression : expression PLUS term
                  | expression MINUS term'''
    p[0] = ('binop', p[2], p[1], p[3])

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = ('num', p[1])

def p_factor_id(p):
    'factor : ID'
    p[0] = ('id', p[1])

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()
