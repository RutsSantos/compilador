from intermedio import intermediate_code

def translate_to_python(intermediate_code):
    python_code = ""
    for instruction in intermediate_code:
        if instruction[0] == 'FUNCTION':
            python_code += f"def {instruction[1]}():\n"
        elif instruction[0] == 'DECLARE':
            python_code += f"    {instruction[1]} = {instruction[2]}\n"
        elif instruction[0] == 'RETURN':
            python_code += f"    return {instruction[1]}\n"
        elif instruction[0] == 'ENDFUNCTION':
            python_code += "\n"
    return python_code

# Example usage
python_code = translate_to_python(intermediate_code)
print(python_code)