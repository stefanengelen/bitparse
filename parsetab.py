
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '[\x1c\xabN\xac\xd20b\xc5\x87\xd4_\x1c\x88\xa7\xd4'
    
_lr_action_items = {'BITSTR':([5,6,7,8,9,10,14,16,22,39,40,50,51,52,53,54,55,],[-27,-28,19,-4,-9,-10,-5,-7,-8,-6,-15,-28,-28,19,19,-17,-16,]),'TIMES':([25,27,28,30,31,32,43,44,45,46,47,48,49,],[-25,36,-26,36,36,36,-24,-23,-21,-22,-20,-18,-19,]),'UNEQUAL':([25,27,28,30,31,32,43,44,45,46,47,48,49,],[-25,33,-26,33,33,33,-24,-23,-21,-22,-20,-18,-19,]),'DIVIDE':([25,27,28,30,31,32,43,44,45,46,47,48,49,],[-25,34,-26,34,34,34,-24,-23,-21,-22,-20,-18,-19,]),'FOR':([5,6,7,8,9,10,14,16,22,39,40,50,51,52,53,54,55,],[-27,-28,11,-4,-9,-10,-5,-7,-8,-6,-15,-28,-28,11,11,-17,-16,]),'RCURLY':([5,6,7,8,9,10,14,16,22,39,40,42,50,52,54,55,],[-27,-28,12,-4,-9,-10,-5,-7,-8,-6,-15,51,-28,54,-17,-16,]),'RPAREN':([25,28,29,30,31,32,43,44,45,46,47,48,49,],[-25,-26,40,41,42,43,-24,-23,-21,-22,-20,-18,-19,]),'ALIGN':([5,6,7,8,9,10,14,16,22,39,40,50,51,52,53,54,55,],[-27,-28,16,-4,-9,-10,-5,-7,-8,-6,-15,-28,-28,16,16,-17,-16,]),'NUMBER':([13,17,18,19,20,23,24,26,33,34,35,36,37,38,],[-12,-11,-14,-13,25,25,25,25,25,25,25,25,25,25,]),'EQUAL':([25,27,28,30,31,32,43,44,45,46,47,48,49,],[-25,35,-26,35,35,35,-24,-23,-21,-22,-20,-18,-19,]),'LCURLY':([3,8,9,10,14,16,22,39,40,41,51,53,54,55,],[5,-4,-9,-10,-5,-7,-8,-6,-15,50,-28,55,-17,-16,]),'STUFF':([5,6,7,8,9,10,14,16,22,39,40,50,51,52,53,54,55,],[-27,-28,13,-4,-9,-10,-5,-7,-8,-6,-15,-28,-28,13,13,-17,-16,]),'UINT':([5,6,7,8,9,10,14,16,22,39,40,50,51,52,53,54,55,],[-27,-28,17,-4,-9,-10,-5,-7,-8,-6,-15,-28,-28,17,17,-17,-16,]),'LPAREN':([11,13,15,17,18,19,20,21,23,24,26,33,34,35,36,37,38,],[23,-12,24,-11,-14,-13,26,29,26,26,26,26,26,26,26,26,26,]),'PLUS':([25,27,28,30,31,32,43,44,45,46,47,48,49,],[-25,37,-26,37,37,37,-24,-23,-21,-22,-20,-18,-19,]),'RPCHOF':([5,6,7,8,9,10,14,16,22,39,40,50,51,52,53,54,55,],[-27,-28,18,-4,-9,-10,-5,-7,-8,-6,-15,-28,-28,18,18,-17,-16,]),'IF':([5,6,7,8,9,10,14,16,22,39,40,50,51,52,53,54,55,],[-27,-28,15,-4,-9,-10,-5,-7,-8,-6,-15,-28,-28,15,15,-17,-16,]),'MINUS':([25,27,28,30,31,32,43,44,45,46,47,48,49,],[-25,38,-26,38,38,38,-24,-23,-21,-22,-20,-18,-19,]),'ID':([0,1,2,4,5,6,7,8,9,10,12,13,14,16,17,18,19,20,22,23,24,25,26,27,28,33,34,35,36,37,38,39,40,43,44,45,46,47,48,49,50,51,52,53,54,55,],[-28,3,-1,-2,-27,-28,21,-4,-9,-10,-3,-12,-5,-7,-11,-14,-13,28,-8,28,28,-25,28,39,-26,28,28,28,28,28,28,-6,-15,-24,-23,-21,-22,-20,-18,-19,-28,-28,21,21,-17,-16,]),'$end':([0,1,2,4,12,],[-28,0,-1,-2,-3,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'forloop':([7,52,53,],[10,10,10,]),'ifcond':([7,52,53,],[9,9,9,]),'fields':([6,50,51,],[7,52,53,]),'new_scope':([5,],[6,]),'expression':([20,23,24,26,33,34,35,36,37,38,],[27,30,31,32,44,45,46,47,48,49,]),'field':([7,52,53,],[14,14,14,]),'empty':([0,6,50,51,],[2,8,8,8,]),'type':([7,52,53,],[20,20,20,]),'structures':([0,],[1,]),'structure':([1,],[4,]),'structcall':([7,52,53,],[22,22,22,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> structures","S'",1,None,None,None),
  ('structures -> empty','structures',1,'p_structures','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',16),
  ('structures -> structures structure','structures',2,'p_structures','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',17),
  ('structure -> ID LCURLY new_scope fields RCURLY','structure',5,'p_structure','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',26),
  ('fields -> empty','fields',1,'p_fields','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',32),
  ('fields -> fields field','fields',2,'p_fields','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',33),
  ('field -> type expression ID','field',3,'p_field','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',43),
  ('field -> ALIGN','field',1,'p_field','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',44),
  ('field -> structcall','field',1,'p_field','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',45),
  ('field -> ifcond','field',1,'p_field','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',46),
  ('field -> forloop','field',1,'p_field','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',47),
  ('type -> UINT','type',1,'p_type','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',55),
  ('type -> STUFF','type',1,'p_type','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',56),
  ('type -> BITSTR','type',1,'p_type','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',57),
  ('type -> RPCHOF','type',1,'p_type','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',58),
  ('structcall -> ID LPAREN RPAREN','structcall',3,'p_structcall','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',64),
  ('ifcond -> IF LPAREN expression RPAREN RCURLY fields LCURLY','ifcond',7,'p_ifcond','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',68),
  ('forloop -> FOR LPAREN expression RPAREN LCURLY fields RCURLY','forloop',7,'p_forloop','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',72),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',76),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',77),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',78),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',79),
  ('expression -> expression EQUAL expression','expression',3,'p_expression_binop','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',80),
  ('expression -> expression UNEQUAL expression','expression',3,'p_expression_binop','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',81),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',90),
  ('expression -> NUMBER','expression',1,'p_expression_number','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',94),
  ('expression -> ID','expression',1,'p_expression_name','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',98),
  ('new_scope -> <empty>','new_scope',0,'p_new_scope','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',103),
  ('empty -> <empty>','empty',0,'p_empty','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',108),
]
