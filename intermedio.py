intermediate_code = []

from simbolos import get_from_symbol_table
from sintactico import parser


def generate_intermediate_code(node):
    if isinstance(node, tuple):
        if node[0] == 'function':
            intermediate_code.append(('FUNCTION', node[1]))
            for stmt in node[2]:
                generate_intermediate_code(stmt)
            intermediate_code.append(('ENDFUNCTION', node[1]))
        elif node[0] == 'declare':
            intermediate_code.append(('DECLARE', node[1], generate_intermediate_code(node[2])))
        elif node[0] == 'return':
            intermediate_code.append(('RETURN', generate_intermediate_code(node[1])))
        elif node[0] == 'binop':
            return f"{generate_intermediate_code(node[2])} {node[1]} {generate_intermediate_code(node[3])}"
        elif node[0] == 'num':
            return node[1]
        elif node[0] == 'id':
            return node[1]
    return None

# Example usage
ast = parser.parse("int main() { int a = 1 + 2; int b = a * 3; return 0; }")
generate_intermediate_code(ast)
print(intermediate_code)
