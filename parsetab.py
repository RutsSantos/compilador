
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DIVIDE EQUAL ID INT LBRACE LPAREN MINUS NUMBER PLUS RBRACE RETURN RPAREN SEMICOLON TIMESprogram : functionfunction : INT ID LPAREN RPAREN LBRACE statement_list RBRACEstatement_list : statement_list statement\n                      | statementstatement : var_declaration\n                 | return_statementvar_declaration : INT ID EQUAL expression SEMICOLONreturn_statement : RETURN expression SEMICOLONexpression : expression PLUS term\n                  | expression MINUS termexpression : termterm : term TIMES factor\n            | term DIVIDE factorterm : factorfactor : NUMBERfactor : ID'
    
_lr_action_items = {'INT':([0,7,9,10,11,12,16,23,33,],[3,8,8,-4,-5,-6,-3,-8,-7,]),'$end':([1,2,15,],[0,-1,-2,]),'ID':([3,8,13,22,24,25,26,27,],[4,14,21,21,21,21,21,21,]),'LPAREN':([4,],[5,]),'RPAREN':([5,],[6,]),'LBRACE':([6,],[7,]),'RETURN':([7,9,10,11,12,16,23,33,],[13,13,-4,-5,-6,-3,-8,-7,]),'RBRACE':([9,10,11,12,16,23,33,],[15,-4,-5,-6,-3,-8,-7,]),'NUMBER':([13,22,24,25,26,27,],[20,20,20,20,20,20,]),'EQUAL':([14,],[22,]),'SEMICOLON':([17,18,19,20,21,28,29,30,31,32,],[23,-11,-14,-15,-16,33,-9,-10,-12,-13,]),'PLUS':([17,18,19,20,21,28,29,30,31,32,],[24,-11,-14,-15,-16,24,-9,-10,-12,-13,]),'MINUS':([17,18,19,20,21,28,29,30,31,32,],[25,-11,-14,-15,-16,25,-9,-10,-12,-13,]),'TIMES':([18,19,20,21,29,30,31,32,],[26,-14,-15,-16,26,26,-12,-13,]),'DIVIDE':([18,19,20,21,29,30,31,32,],[27,-14,-15,-16,27,27,-12,-13,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'function':([0,],[2,]),'statement_list':([7,],[9,]),'statement':([7,9,],[10,16,]),'var_declaration':([7,9,],[11,11,]),'return_statement':([7,9,],[12,12,]),'expression':([13,22,],[17,28,]),'term':([13,22,24,25,],[18,18,29,30,]),'factor':([13,22,24,25,26,27,],[19,19,19,19,31,32,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> function','program',1,'p_program','sintactico.py',5),
  ('function -> INT ID LPAREN RPAREN LBRACE statement_list RBRACE','function',7,'p_function','sintactico.py',9),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','sintactico.py',13),
  ('statement_list -> statement','statement_list',1,'p_statement_list','sintactico.py',14),
  ('statement -> var_declaration','statement',1,'p_statement','sintactico.py',21),
  ('statement -> return_statement','statement',1,'p_statement','sintactico.py',22),
  ('var_declaration -> INT ID EQUAL expression SEMICOLON','var_declaration',5,'p_var_declaration','sintactico.py',26),
  ('return_statement -> RETURN expression SEMICOLON','return_statement',3,'p_return_statement','sintactico.py',30),
  ('expression -> expression PLUS term','expression',3,'p_expression_binop','sintactico.py',34),
  ('expression -> expression MINUS term','expression',3,'p_expression_binop','sintactico.py',35),
  ('expression -> term','expression',1,'p_expression_term','sintactico.py',39),
  ('term -> term TIMES factor','term',3,'p_term_binop','sintactico.py',43),
  ('term -> term DIVIDE factor','term',3,'p_term_binop','sintactico.py',44),
  ('term -> factor','term',1,'p_term_factor','sintactico.py',48),
  ('factor -> NUMBER','factor',1,'p_factor_num','sintactico.py',52),
  ('factor -> ID','factor',1,'p_factor_id','sintactico.py',56),
]
