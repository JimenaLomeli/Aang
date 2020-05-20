/*
 * Authors:
 Ana Jimena Lomeli Cantu - A00818665
 Jorge Andres Sabella - A01282292
 */

grammar Aang;

/* TOKENS */

// Operators
SUMA: '+';
RESTA: '-';
MULT: '*';
DIVISION: '/';
ASIGNAR: '=';
IGUAL: '==';
DIFERENTE: '!=';
MENOR: '<';
MAYOR: '>';
Y_SIMBOLO: '&&';
O_SIMBOLO: '||';

//Keywords
INT: 'int';
CHAR: 'char';
BOOL: 'bool';
IF: 'if';
ELSE: 'else';
WHILE: 'while';
PRINT: 'print';
RETURN: 'return';
PROGRAMA: 'programa';
EMPEZAR: 'empezar';
FIN: 'fin';

//Separators
I_PARENTESIS: '(';
D_PARENTESIS: ')';
I_CORCHETE: '{';
D_CORCHETE: '}';
PYCOMA: ';';
COMA: ',';

//Data Types
VOID: 'void';
CTE_BOOL: 'True' | 'False';
ID: [a-zA-Z]+;
CTE_INT: [1-9][0-9]*;
CTE_CHAR: [A-Za-z];

// Whitespace and comments
COMENT: '#' ~[\r\n]* -> skip;
WHITESPACE: [ \t\r\n]+ -> skip;

/* GRAMMAR */

programa: PROGRAMA ID PYCOMA p1 FIN;
p1: variable p2 | funcion | principal;
p2: funcion p2 | principal;
variable: tipo_id v;

principal: tipo_id EMPEZAR I_CORCHETE bloque D_CORCHETE;

v: ID v1 PYCOMA v2;
v1: COMA ID v1 | /* epsilon */;
v2: variable | /* epsilon */;

tipo_id: INT | CHAR | BOOL;

funcion:
	f ID I_PARENTESIS f1 D_PARENTESIS I_CORCHETE bloque D_CORCHETE;
f: VOID | tipo_id;
f1: tipo_id ID f2 | /* epsilon */;
f2: COMA tipo_id ID f2 | /* epsilon */;

bloque: variable bloque | acciones | /* epsilon */;
acciones:
	asignacion acciones
	| condicion acciones
	| ciclo1 acciones
	| escribir acciones
	| llamar_fun acciones
	| fun_regresar
	| /* epsilon */;

fun_regresar: RETURN exp PYCOMA;

asignacion: ID ASIGNAR a PYCOMA;
a: expresion | llamar_fun;

expresion: exp e;
e:
	MAYOR exp
	| MENOR exp
	| IGUAL exp
	| DIFERENTE exp
	| /* epsilon */;
exp: termino e1;
e1: SUMA termino e1 | RESTA termino e1 | /* epsilon */;

factor: I_PARENTESIS expresion D_PARENTESIS | cte_var;

termino: factor t;
t: MULT factor t | DIVISION factor t | /* epsilon */;

condicion:
	IF I_PARENTESIS expresion D_PARENTESIS c1;

c1: I_CORCHETE acciones D_CORCHETE c2;

c2: ELSE I_CORCHETE acciones D_CORCHETE | /* epsilon */;

ciclo1:
	WHILE I_PARENTESIS expresion D_PARENTESIS ciclo2;

ciclo2: I_CORCHETE acciones D_CORCHETE;

escribir: PRINT I_PARENTESIS es D_PARENTESIS PYCOMA;
es: expresion es2 | CTE_CHAR es2 | llamar_fun;
es2: COMA es | /* epsilon */;

cte_var: CTE_INT| CTE_CHAR | ID | CTE_BOOL;

llamar_fun: ID I_PARENTESIS argumentos D_PARENTESIS fc;

argumentos: exp agregar_args | /* epsilon */;
agregar_args: COMA exp agregar_args | /* epsilon */;
fc: PYCOMA | /* epsilon */;
