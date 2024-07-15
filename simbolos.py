symbol_table = {}

def add_to_symbol_table(name, value):
    symbol_table[name] = value

def get_from_symbol_table(name):
    return symbol_table.get(name, None)
