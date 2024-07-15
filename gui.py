import tkinter as tk
from tkinter import filedialog
import ply.lex as lex
import ply.yacc as yacc

from lexico import lexer
from sintactico import parser
from intermedio import generate_intermediate_code
from intermedio import intermediate_code
from traductor import translate_to_python

def open_file():
    filepath = filedialog.askopenfilename()
    with open(filepath, 'r') as file:
        code = file.read()
    input_text.delete(1.0, tk.END)
    input_text.insert(tk.END, code)

def compile_code():
    code = input_text.get(1.0, tk.END)
    
    lexer.input(code)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(tok)
    
    ast = parser.parse(code)
    
    intermediate_code.clear()
    generate_intermediate_code(ast)
    python_code = translate_to_python(intermediate_code)
    
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, "Tokens:\n" + str(tokens) + "\n\n")
    output_text.insert(tk.END, "AST:\n" + str(ast) + "\n\n")
    output_text.insert(tk.END, "Intermediate Code:\n" + str(intermediate_code) + "\n\n")
    output_text.insert(tk.END, "Python Code:\n" + python_code + "\n\n")

root = tk.Tk()
root.title("C++ to Python Compiler")

open_button = tk.Button(root, text="Open File", command=open_file)
open_button.pack()

input_text = tk.Text(root, height=40, width=80)
input_text.pack()

compile_button = tk.Button(root, text="Compile", command=compile_code)
compile_button.pack()

output_text = tk.Text(root, height=40, width=150)
output_text.pack()

root.mainloop()