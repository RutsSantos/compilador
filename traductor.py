from intermedio import intermediate_code

def translate_to_python(intermediate_code):
    python_code = []
    indent_level = 0
    indent = '    '  # Cuatro espacios para la indentación

    for line in intermediate_code:
        if line.endswith(':'):  # Si la línea termina en ':', incrementamos la indentación
            python_code.append(indent * indent_level + line)
            indent_level += 1
        else:
            python_code.append(indent * indent_level + line)
            # Si es una línea de cierre, reducimos la indentación (aunque en este caso no sería necesario)

    return "\n".join(python_code)

# Example usage
python_code = translate_to_python(intermediate_code)
print(python_code)