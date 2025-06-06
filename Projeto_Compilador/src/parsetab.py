
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftNOTnonassocLTLEGTGEEQUALNOTEQUALleftPLUSMINUSleftTIMESDIVIDEDIVMODrightUMINUSAND ASSIGN BEGIN BOOLEAN COLON COMMA COMMENT DIV DIVIDE DO DOT DOWNTO ELSE END EQUAL FALSE FOR GE GT ID IF INTEGER LE LPAREN LT MINUS MOD MODOP NOT NOTEQUAL NUMBER OR PLUS PROGRAM READLN RPAREN SEMI STRING THEN TIMES TO TRUE VAR WHILE WRITE WRITELNprogram : PROGRAM ID SEMI declarations compound_stmt DOT\n| PROGRAM ID SEMI compound_stmt DOTdeclarations : VAR var_decl_list\n| emptyvar_decl_list : var_decl SEMI\n| var_decl SEMI var_decl_listvar_decl : id_list COLON typeid_list : ID\n| ID COMMA id_listtype : INTEGER\n| BOOLEANcompound_stmt : BEGIN stmt_list ENDstmt_list : stmt\n| stmt SEMI stmt_liststmt : assignment\n| if_stmt\n| while_stmt\n| for_stmt\n| readln_stmt\n| writeln_stmt\n| compound_stmt\n| emptyassignment : ID ASSIGN exprif_stmt : IF expr THEN stmt\n| IF expr THEN stmt ELSE stmtwhile_stmt : WHILE expr DO stmtfor_stmt : FOR ID ASSIGN expr TO expr DO stmtreadln_stmt : READLN LPAREN ID RPARENwriteln_stmt : WRITELN LPAREN writeln_args RPAREN\n| WRITE LPAREN writeln_args RPAREN\n| WRITELN LPAREN RPAREN\n| WRITE LPAREN RPARENwriteln_args : arg\n| arg COMMA writeln_argsarg : expr\n| STRINGexpr : simple_expr\n| simple_expr relop simple_exprrelop : EQUAL\n| NOTEQUAL\n| LT\n| GT\n| LE\n| GEsimple_expr : term\n| simple_expr addop termaddop : PLUS\n| MINUS\n| ORterm : factor\n| term mulop factormulop : TIMES\n| DIVIDE\n| DIV\n| MOD\n| ANDfactor : ID\n| NUMBER\n| LPAREN expr RPAREN\n| NOT factor\n| TRUE\n| FALSE\n| MINUS factor %prec UMINUSempty :'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,11,33,],[0,-2,-1,]),'ID':([2,7,9,27,28,29,34,36,38,39,46,47,50,53,54,55,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,84,85,103,105,106,110,],[3,15,26,44,44,52,15,15,26,44,44,44,44,86,44,44,26,44,44,-39,-40,-41,-42,-43,-44,-47,-48,-49,44,-52,-53,-54,-55,-56,26,44,44,26,44,26,]),'SEMI':([3,9,13,17,18,19,20,21,22,23,24,25,37,38,41,42,43,44,45,48,49,57,58,59,62,63,82,83,84,88,93,94,95,96,97,98,99,101,102,104,105,108,110,111,],[4,-64,34,38,-15,-16,-17,-18,-19,-20,-21,-22,-12,-64,-37,-45,-50,-57,-58,-61,-62,-7,-10,-11,-23,-64,-60,-63,-64,-31,-32,-24,-38,-46,-51,-59,-26,-28,-29,-30,-64,-25,-64,-27,]),'VAR':([4,],[7,]),'BEGIN':([4,5,8,9,12,34,38,56,63,84,105,110,],[9,9,-4,9,-3,-5,9,-6,9,9,9,9,]),'DOT':([6,10,37,],[11,33,-12,]),'IF':([9,38,63,84,105,110,],[27,27,27,27,27,27,]),'WHILE':([9,38,63,84,105,110,],[28,28,28,28,28,28,]),'FOR':([9,38,63,84,105,110,],[29,29,29,29,29,29,]),'READLN':([9,38,63,84,105,110,],[30,30,30,30,30,30,]),'WRITELN':([9,38,63,84,105,110,],[31,31,31,31,31,31,]),'WRITE':([9,38,63,84,105,110,],[32,32,32,32,32,32,]),'END':([9,16,17,18,19,20,21,22,23,24,25,37,38,41,42,43,44,45,48,49,61,62,63,82,83,84,88,93,94,95,96,97,98,99,101,102,104,105,108,110,111,],[-64,37,-13,-15,-16,-17,-18,-19,-20,-21,-22,-12,-64,-37,-45,-50,-57,-58,-61,-62,-14,-23,-64,-60,-63,-64,-31,-32,-24,-38,-46,-51,-59,-26,-28,-29,-30,-64,-25,-64,-27,]),'COLON':([14,15,60,],[35,-8,-9,]),'COMMA':([15,41,42,43,44,45,48,49,82,83,89,90,91,95,96,97,98,],[36,-37,-45,-50,-57,-58,-61,-62,-60,-63,103,-35,-36,-38,-46,-51,-59,]),'ELSE':([18,19,20,21,22,23,24,25,37,41,42,43,44,45,48,49,62,63,82,83,84,88,93,94,95,96,97,98,99,101,102,104,105,108,110,111,],[-15,-16,-17,-18,-19,-20,-21,-22,-12,-37,-45,-50,-57,-58,-61,-62,-23,-64,-60,-63,-64,-31,-32,105,-38,-46,-51,-59,-26,-28,-29,-30,-64,-25,-64,-27,]),'ASSIGN':([26,52,],[39,85,]),'NUMBER':([27,28,39,46,47,50,54,55,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,85,103,106,],[45,45,45,45,45,45,45,45,45,45,-39,-40,-41,-42,-43,-44,-47,-48,-49,45,-52,-53,-54,-55,-56,45,45,45,]),'LPAREN':([27,28,30,31,32,39,46,47,50,54,55,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,85,103,106,],[46,46,53,54,55,46,46,46,46,46,46,46,46,-39,-40,-41,-42,-43,-44,-47,-48,-49,46,-52,-53,-54,-55,-56,46,46,46,]),'NOT':([27,28,39,46,47,50,54,55,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,85,103,106,],[47,47,47,47,47,47,47,47,47,47,-39,-40,-41,-42,-43,-44,-47,-48,-49,47,-52,-53,-54,-55,-56,47,47,47,]),'TRUE':([27,28,39,46,47,50,54,55,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,85,103,106,],[48,48,48,48,48,48,48,48,48,48,-39,-40,-41,-42,-43,-44,-47,-48,-49,48,-52,-53,-54,-55,-56,48,48,48,]),'FALSE':([27,28,39,46,47,50,54,55,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,85,103,106,],[49,49,49,49,49,49,49,49,49,49,-39,-40,-41,-42,-43,-44,-47,-48,-49,49,-52,-53,-54,-55,-56,49,49,49,]),'MINUS':([27,28,39,41,42,43,44,45,46,47,48,49,50,54,55,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,85,95,96,97,98,103,106,],[50,50,50,73,-45,-50,-57,-58,50,50,-61,-62,50,50,50,50,50,-39,-40,-41,-42,-43,-44,-47,-48,-49,50,-52,-53,-54,-55,-56,-60,-63,50,73,-46,-51,-59,50,50,]),'INTEGER':([35,],[58,]),'BOOLEAN':([35,],[59,]),'THEN':([40,41,42,43,44,45,48,49,82,83,95,96,97,98,],[63,-37,-45,-50,-57,-58,-61,-62,-60,-63,-38,-46,-51,-59,]),'DO':([41,42,43,44,45,48,49,51,82,83,95,96,97,98,109,],[-37,-45,-50,-57,-58,-61,-62,84,-60,-63,-38,-46,-51,-59,110,]),'RPAREN':([41,42,43,44,45,48,49,54,55,81,82,83,86,87,89,90,91,92,95,96,97,98,107,],[-37,-45,-50,-57,-58,-61,-62,88,93,98,-60,-63,101,102,-33,-35,-36,104,-38,-46,-51,-59,-34,]),'TO':([41,42,43,44,45,48,49,82,83,95,96,97,98,100,],[-37,-45,-50,-57,-58,-61,-62,-60,-63,-38,-46,-51,-59,106,]),'EQUAL':([41,42,43,44,45,48,49,82,83,96,97,98,],[66,-45,-50,-57,-58,-61,-62,-60,-63,-46,-51,-59,]),'NOTEQUAL':([41,42,43,44,45,48,49,82,83,96,97,98,],[67,-45,-50,-57,-58,-61,-62,-60,-63,-46,-51,-59,]),'LT':([41,42,43,44,45,48,49,82,83,96,97,98,],[68,-45,-50,-57,-58,-61,-62,-60,-63,-46,-51,-59,]),'GT':([41,42,43,44,45,48,49,82,83,96,97,98,],[69,-45,-50,-57,-58,-61,-62,-60,-63,-46,-51,-59,]),'LE':([41,42,43,44,45,48,49,82,83,96,97,98,],[70,-45,-50,-57,-58,-61,-62,-60,-63,-46,-51,-59,]),'GE':([41,42,43,44,45,48,49,82,83,96,97,98,],[71,-45,-50,-57,-58,-61,-62,-60,-63,-46,-51,-59,]),'PLUS':([41,42,43,44,45,48,49,82,83,95,96,97,98,],[72,-45,-50,-57,-58,-61,-62,-60,-63,72,-46,-51,-59,]),'OR':([41,42,43,44,45,48,49,82,83,95,96,97,98,],[74,-45,-50,-57,-58,-61,-62,-60,-63,74,-46,-51,-59,]),'TIMES':([42,43,44,45,48,49,82,83,96,97,98,],[76,-50,-57,-58,-61,-62,-60,-63,76,-51,-59,]),'DIVIDE':([42,43,44,45,48,49,82,83,96,97,98,],[77,-50,-57,-58,-61,-62,-60,-63,77,-51,-59,]),'DIV':([42,43,44,45,48,49,82,83,96,97,98,],[78,-50,-57,-58,-61,-62,-60,-63,78,-51,-59,]),'MOD':([42,43,44,45,48,49,82,83,96,97,98,],[79,-50,-57,-58,-61,-62,-60,-63,79,-51,-59,]),'AND':([42,43,44,45,48,49,82,83,96,97,98,],[80,-50,-57,-58,-61,-62,-60,-63,80,-51,-59,]),'STRING':([54,55,103,],[91,91,91,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declarations':([4,],[5,]),'compound_stmt':([4,5,9,38,63,84,105,110,],[6,10,24,24,24,24,24,24,]),'empty':([4,9,38,63,84,105,110,],[8,25,25,25,25,25,25,]),'var_decl_list':([7,34,],[12,56,]),'var_decl':([7,34,],[13,13,]),'id_list':([7,34,36,],[14,14,60,]),'stmt_list':([9,38,],[16,61,]),'stmt':([9,38,63,84,105,110,],[17,17,94,99,108,111,]),'assignment':([9,38,63,84,105,110,],[18,18,18,18,18,18,]),'if_stmt':([9,38,63,84,105,110,],[19,19,19,19,19,19,]),'while_stmt':([9,38,63,84,105,110,],[20,20,20,20,20,20,]),'for_stmt':([9,38,63,84,105,110,],[21,21,21,21,21,21,]),'readln_stmt':([9,38,63,84,105,110,],[22,22,22,22,22,22,]),'writeln_stmt':([9,38,63,84,105,110,],[23,23,23,23,23,23,]),'expr':([27,28,39,46,54,55,85,103,106,],[40,51,62,81,90,90,100,90,109,]),'simple_expr':([27,28,39,46,54,55,64,85,103,106,],[41,41,41,41,41,41,95,41,41,41,]),'term':([27,28,39,46,54,55,64,65,85,103,106,],[42,42,42,42,42,42,42,96,42,42,42,]),'factor':([27,28,39,46,47,50,54,55,64,65,75,85,103,106,],[43,43,43,43,82,83,43,43,43,43,97,43,43,43,]),'type':([35,],[57,]),'relop':([41,],[64,]),'addop':([41,95,],[65,65,]),'mulop':([42,96,],[75,75,]),'writeln_args':([54,55,103,],[87,92,107,]),'arg':([54,55,103,],[89,89,89,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID SEMI declarations compound_stmt DOT','program',6,'p_program','compilador.py',101),
  ('program -> PROGRAM ID SEMI compound_stmt DOT','program',5,'p_program','compilador.py',102),
  ('declarations -> VAR var_decl_list','declarations',2,'p_declarations','compilador.py',111),
  ('declarations -> empty','declarations',1,'p_declarations','compilador.py',112),
  ('var_decl_list -> var_decl SEMI','var_decl_list',2,'p_var_decl_list','compilador.py',116),
  ('var_decl_list -> var_decl SEMI var_decl_list','var_decl_list',3,'p_var_decl_list','compilador.py',117),
  ('var_decl -> id_list COLON type','var_decl',3,'p_var_decl','compilador.py',121),
  ('id_list -> ID','id_list',1,'p_id_list','compilador.py',129),
  ('id_list -> ID COMMA id_list','id_list',3,'p_id_list','compilador.py',130),
  ('type -> INTEGER','type',1,'p_type','compilador.py',134),
  ('type -> BOOLEAN','type',1,'p_type','compilador.py',135),
  ('compound_stmt -> BEGIN stmt_list END','compound_stmt',3,'p_compound_stmt','compilador.py',139),
  ('stmt_list -> stmt','stmt_list',1,'p_stmt_list','compilador.py',143),
  ('stmt_list -> stmt SEMI stmt_list','stmt_list',3,'p_stmt_list','compilador.py',144),
  ('stmt -> assignment','stmt',1,'p_stmt','compilador.py',151),
  ('stmt -> if_stmt','stmt',1,'p_stmt','compilador.py',152),
  ('stmt -> while_stmt','stmt',1,'p_stmt','compilador.py',153),
  ('stmt -> for_stmt','stmt',1,'p_stmt','compilador.py',154),
  ('stmt -> readln_stmt','stmt',1,'p_stmt','compilador.py',155),
  ('stmt -> writeln_stmt','stmt',1,'p_stmt','compilador.py',156),
  ('stmt -> compound_stmt','stmt',1,'p_stmt','compilador.py',157),
  ('stmt -> empty','stmt',1,'p_stmt','compilador.py',158),
  ('assignment -> ID ASSIGN expr','assignment',3,'p_assignment','compilador.py',162),
  ('if_stmt -> IF expr THEN stmt','if_stmt',4,'p_if_stmt','compilador.py',172),
  ('if_stmt -> IF expr THEN stmt ELSE stmt','if_stmt',6,'p_if_stmt','compilador.py',173),
  ('while_stmt -> WHILE expr DO stmt','while_stmt',4,'p_while_stmt','compilador.py',183),
  ('for_stmt -> FOR ID ASSIGN expr TO expr DO stmt','for_stmt',8,'p_for_stmt','compilador.py',189),
  ('readln_stmt -> READLN LPAREN ID RPAREN','readln_stmt',4,'p_readln_stmt','compilador.py',221),
  ('writeln_stmt -> WRITELN LPAREN writeln_args RPAREN','writeln_stmt',4,'p_writeln_stmt','compilador.py',231),
  ('writeln_stmt -> WRITE LPAREN writeln_args RPAREN','writeln_stmt',4,'p_writeln_stmt','compilador.py',232),
  ('writeln_stmt -> WRITELN LPAREN RPAREN','writeln_stmt',3,'p_writeln_stmt','compilador.py',233),
  ('writeln_stmt -> WRITE LPAREN RPAREN','writeln_stmt',3,'p_writeln_stmt','compilador.py',234),
  ('writeln_args -> arg','writeln_args',1,'p_writeln_args','compilador.py',247),
  ('writeln_args -> arg COMMA writeln_args','writeln_args',3,'p_writeln_args','compilador.py',248),
  ('arg -> expr','arg',1,'p_arg','compilador.py',255),
  ('arg -> STRING','arg',1,'p_arg','compilador.py',256),
  ('expr -> simple_expr','expr',1,'p_expr','compilador.py',264),
  ('expr -> simple_expr relop simple_expr','expr',3,'p_expr','compilador.py',265),
  ('relop -> EQUAL','relop',1,'p_relop','compilador.py',273),
  ('relop -> NOTEQUAL','relop',1,'p_relop','compilador.py',274),
  ('relop -> LT','relop',1,'p_relop','compilador.py',275),
  ('relop -> GT','relop',1,'p_relop','compilador.py',276),
  ('relop -> LE','relop',1,'p_relop','compilador.py',277),
  ('relop -> GE','relop',1,'p_relop','compilador.py',278),
  ('simple_expr -> term','simple_expr',1,'p_simple_expr','compilador.py',282),
  ('simple_expr -> simple_expr addop term','simple_expr',3,'p_simple_expr','compilador.py',283),
  ('addop -> PLUS','addop',1,'p_addop','compilador.py',291),
  ('addop -> MINUS','addop',1,'p_addop','compilador.py',292),
  ('addop -> OR','addop',1,'p_addop','compilador.py',293),
  ('term -> factor','term',1,'p_term','compilador.py',297),
  ('term -> term mulop factor','term',3,'p_term','compilador.py',298),
  ('mulop -> TIMES','mulop',1,'p_mulop','compilador.py',306),
  ('mulop -> DIVIDE','mulop',1,'p_mulop','compilador.py',307),
  ('mulop -> DIV','mulop',1,'p_mulop','compilador.py',308),
  ('mulop -> MOD','mulop',1,'p_mulop','compilador.py',309),
  ('mulop -> AND','mulop',1,'p_mulop','compilador.py',310),
  ('factor -> ID','factor',1,'p_factor','compilador.py',314),
  ('factor -> NUMBER','factor',1,'p_factor','compilador.py',315),
  ('factor -> LPAREN expr RPAREN','factor',3,'p_factor','compilador.py',316),
  ('factor -> NOT factor','factor',2,'p_factor','compilador.py',317),
  ('factor -> TRUE','factor',1,'p_factor','compilador.py',318),
  ('factor -> FALSE','factor',1,'p_factor','compilador.py',319),
  ('factor -> MINUS factor','factor',2,'p_factor','compilador.py',320),
  ('empty -> <empty>','empty',0,'p_empty','compilador.py',345),
]
