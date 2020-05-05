from antlr4 import *
from Types import Types

class Operations:
    SUMA = "+"
    RESTA = "-"
    MULT = "*"
    DIVISION = "/"
    Y_SIMBOLO = "&&"
    O_SIMBOLO = "||"
    IGUAL = "=="
    MAYOR = ">"
    MENOR = "<"
    DIFERENTE = "!="
    ASIGNAR = "="

class Types(Enum):
    CHAR = "char"
    INT = "int"
    ERROR = "error: types do not match"

class SemanticCube: 
	cube = {
		# =========== INT == INT ===========
		(Types.INT, Types.INT, Operations.SUMA): Types.INT,
		(Types.INT, Types.INT, Operations.RESTA): Types.INT,
		(Types.INT, Types.INT, Operations.DIVISION): Types.INT,
		(Types.INT, Types.INT, Operations.MULT): Types.INT,
		(Types.INT, Types.INT, Operations.Y_SIMBOLO): Types.INT,
		(Types.INT, Types.INT, Operations.O_SIMBOLO): Types.INT,
		(Types.INT, Types.INT, Operations.IGUAL): Types.INT,
		(Types.INT, Types.INT, Operations.MAYOR): Types.INT,
		(Types.INT, Types.INT, Operations.MENOR): Types.INT,
		(Types.INT, Types.INT, Operations.DIFERENTE): Types.INT,
		(Types.INT, Types.INT, Operations.ASIGNAR): Types.INT,

		# =========== CHAR == CHAR ===========
		(Types.CHAR, Types.CHAR, Operations.SUMA): Types.ERROR,
		(Types.CHAR, Types.CHAR, Operations.RESTA): Types.ERROR,
		(Types.CHAR, Types.CHAR, Operations.MULT): Types.ERROR,
		(Types.CHAR, Types.CHAR, Operations.DIVISION): Types.ERROR,
		(Types.CHAR, Types.CHAR, Operations.Y_SIMBOLO): Types.ERROR,
		(Types.CHAR, Types.CHAR, Operations.O_SIMBOLO): Types.ERROR,
		(Types.CHAR, Types.CHAR, Operations.IGUAL): Types.INT,
		(Types.CHAR, Types.CHAR, Operations.MAYOR): Types.ERROR,
		(Types.CHAR, Types.CHAR, Operations.MENOR): Types.ERROR,
		(Types.CHAR, Types.CHAR, Operations.MENOR): Types.ERROR,
		(Types.CHAR, Types.CHAR, Operations.ASIGNAR): Types.CHAR,

		# =========== INT == CHAR ===========
		(Types.INT, Types.CHAR, Operations.SUMA): Types.ERROR,
		(Types.INT, Types.CHAR, Operations.RESTA): Types.ERROR,
		(Types.INT, Types.CHAR, Operations.MULT): Types.ERROR,
		(Types.INT, Types.CHAR, Operations.DIVISION): Types.ERROR,
		(Types.INT, Types.CHAR, Operations.Y_SIMBOLO): Types.ERROR,
		(Types.INT, Types.CHAR, Operations.O_SIMBOLO): Types.ERROR,
		(Types.INT, Types.CHAR, Operations.IGUAL): Types.ERROR,		
		(Types.INT, Types.CHAR, Operations.MAYOR): Types.ERROR,
		(Types.INT, Types.CHAR, Operations.MENOR): Types.ERROR,
		(Types.INT, Types.CHAR, Operations.DIFERENTE): Types.ERROR,
		(Types.INT, Types.CHAR, Operations.ASIGNAR): Types.ERROR,

		# =========== CHAR == INT ===========
		(Types.CHAR, Types.INT, Operations.SUMA): Types.ERROR,
		(Types.CHAR, Types.INT, Operations.RESTA): Types.ERROR,
		(Types.CHAR, Types.INT, Operations.MULT): Types.ERROR,
		(Types.CHAR, Types.INT, Operations.DIVISION): Types.ERROR,
		(Types.CHAR, Types.INT, Operations.Y_SIMBOLO): Types.ERROR,
		(Types.CHAR, Types.INT, Operations.O_SIMBOLO): Types.ERROR,
		(Types.CHAR, Types.INT, Operations.IGUAL): Types.ERROR,		
		(Types.CHAR, Types.INT, Operations.MAYOR): Types.ERROR,
		(Types.CHAR, Types.INT, Operations.MENOR): Types.ERROR,
		(Types.CHAR, Types.INT, Operations.DIFERENTE): Types.ERROR,
		(Types.CHAR, Types.INT, Operations.ASIGNAR): Types.ERROR,
	}

