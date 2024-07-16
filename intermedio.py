intermediate_code = []

def generate_intermediate_code(node):
    if isinstance(node, tuple):
        if node[0] == 'program':
            generate_intermediate_code(node[1])
        elif node[0] == 'function':
            intermediate_code.append(f"def {node[1]}():")
            for stmt in node[2]:
                generate_intermediate_code(stmt)
        elif node[0] == 'declare':
            intermediate_code.append(f"{node[1]} = {generate_expression(node[2])}")
        elif node[0] == 'return':
            intermediate_code.append(f"return {generate_expression(node[1])}")
        elif node[0] == 'binop':
            return f"({generate_expression(node[2])} {node[1]} {generate_expression(node[3])})"
        elif node[0] == 'num':
            return str(node[1])
        elif node[0] == 'id':
            return node[1]

def generate_expression(node):
    if isinstance(node, tuple):
        if node[0] == 'binop':
            return f"({generate_expression(node[2])} {node[1]} {generate_expression(node[3])})"
        elif node[0] == 'num':
            return str(node[1])
        elif node[0] == 'id':
            return node[1]
    else:
        return str(node)
