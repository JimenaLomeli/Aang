from antlr4 import *


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


class Types():
    CHAR = "char"
    INT = "int"
    ERROR = "error: types do not match"
    BOOL = "bool"


class SemanticCube:
    cube = {
        # =========== INT == INT ===========
        (Types.INT, Types.INT, Operations.SUMA): Types.INT,
        (Types.INT, Types.INT, Operations.RESTA): Types.INT,
        (Types.INT, Types.INT, Operations.DIVISION): Types.INT,
        (Types.INT, Types.INT, Operations.MULT): Types.INT,
        (Types.INT, Types.INT, Operations.Y_SIMBOLO): Types.ERROR,
        (Types.INT, Types.INT, Operations.O_SIMBOLO): Types.ERROR,
        (Types.INT, Types.INT, Operations.IGUAL): Types.BOOL,
        (Types.INT, Types.INT, Operations.MAYOR): Types.BOOL,
        (Types.INT, Types.INT, Operations.MENOR): Types.BOOL,
        (Types.INT, Types.INT, Operations.DIFERENTE): Types.BOOL,
        (Types.INT, Types.INT, Operations.ASIGNAR): Types.INT,

        # =========== CHAR == CHAR ===========
        (Types.CHAR, Types.CHAR, Operations.SUMA): Types.ERROR,
        (Types.CHAR, Types.CHAR, Operations.RESTA): Types.ERROR,
        (Types.CHAR, Types.CHAR, Operations.MULT): Types.ERROR,
        (Types.CHAR, Types.CHAR, Operations.DIVISION): Types.ERROR,
        (Types.CHAR, Types.CHAR, Operations.Y_SIMBOLO): Types.ERROR,
        (Types.CHAR, Types.CHAR, Operations.O_SIMBOLO): Types.ERROR,
        (Types.CHAR, Types.CHAR, Operations.IGUAL): Types.BOOL,
        (Types.CHAR, Types.CHAR, Operations.MAYOR): Types.ERROR,
        (Types.CHAR, Types.CHAR, Operations.MENOR): Types.ERROR,
        (Types.CHAR, Types.CHAR, Operations.DIFERENTE): Types.BOOL,
        (Types.CHAR, Types.CHAR, Operations.ASIGNAR): Types.CHAR,

        # =========== BOOL == BOOL ===========
        (Types.BOOL, Types.BOOL, Operations.SUMA): Types.ERROR,
        (Types.BOOL, Types.BOOL, Operations.RESTA): Types.ERROR,
        (Types.BOOL, Types.BOOL, Operations.MULT): Types.ERROR,
        (Types.BOOL, Types.BOOL, Operations.DIVISION): Types.ERROR,
        (Types.BOOL, Types.BOOL, Operations.Y_SIMBOLO): Types.BOOL,
        (Types.BOOL, Types.BOOL, Operations.O_SIMBOLO): Types.BOOL,
        (Types.BOOL, Types.BOOL, Operations.IGUAL): Types.BOOL,
        (Types.BOOL, Types.BOOL, Operations.MAYOR): Types.BOOL,
        (Types.BOOL, Types.BOOL, Operations.MENOR): Types.BOOL,
        (Types.BOOL, Types.BOOL, Operations.DIFERENTE): Types.BOOL,
        (Types.BOOL, Types.BOOL, Operations.ASIGNAR): Types.BOOL,


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

        # =========== INT == BOOL ===========
        (Types.INT, Types.BOOL, Operations.SUMA): Types.ERROR,
        (Types.INT, Types.BOOL, Operations.RESTA): Types.ERROR,
        (Types.INT, Types.BOOL, Operations.MULT): Types.ERROR,
        (Types.INT, Types.BOOL, Operations.DIVISION): Types.ERROR,
        (Types.INT, Types.BOOL, Operations.Y_SIMBOLO): Types.ERROR,
        (Types.INT, Types.BOOL, Operations.O_SIMBOLO): Types.ERROR,
        (Types.INT, Types.BOOL, Operations.IGUAL): Types.ERROR,
        (Types.INT, Types.BOOL, Operations.MAYOR): Types.ERROR,
        (Types.INT, Types.BOOL, Operations.MENOR): Types.ERROR,
        (Types.INT, Types.BOOL, Operations.DIFERENTE): Types.ERROR,
        (Types.INT, Types.BOOL, Operations.ASIGNAR): Types.ERROR,

        # =========== BOOL == INT ===========
        (Types.BOOL, Types.INT, Operations.SUMA): Types.ERROR,
        (Types.BOOL, Types.INT, Operations.RESTA): Types.ERROR,
        (Types.BOOL, Types.INT, Operations.MULT): Types.ERROR,
        (Types.BOOL, Types.INT, Operations.DIVISION): Types.ERROR,
        (Types.BOOL, Types.INT, Operations.Y_SIMBOLO): Types.ERROR,
        (Types.BOOL, Types.INT, Operations.O_SIMBOLO): Types.ERROR,
        (Types.BOOL, Types.INT, Operations.IGUAL): Types.ERROR,
        (Types.BOOL, Types.INT, Operations.MAYOR): Types.ERROR,
        (Types.BOOL, Types.INT, Operations.MENOR): Types.ERROR,
        (Types.BOOL, Types.INT, Operations.DIFERENTE): Types.ERROR,
        (Types.BOOL, Types.INT, Operations.ASIGNAR): Types.ERROR,

        # =========== CHAR == BOOL ===========
        (Types.CHAR, Types.BOOL, Operations.SUMA): Types.ERROR,
        (Types.CHAR, Types.BOOL, Operations.RESTA): Types.ERROR,
        (Types.CHAR, Types.BOOL, Operations.MULT): Types.ERROR,
        (Types.CHAR, Types.BOOL, Operations.DIVISION): Types.ERROR,
        (Types.CHAR, Types.BOOL, Operations.Y_SIMBOLO): Types.ERROR,
        (Types.CHAR, Types.BOOL, Operations.O_SIMBOLO): Types.ERROR,
        (Types.CHAR, Types.BOOL, Operations.IGUAL): Types.ERROR,
        (Types.CHAR, Types.BOOL, Operations.MAYOR): Types.ERROR,
        (Types.CHAR, Types.BOOL, Operations.MENOR): Types.ERROR,
        (Types.CHAR, Types.BOOL, Operations.DIFERENTE): Types.ERROR,
        (Types.CHAR, Types.BOOL, Operations.ASIGNAR): Types.ERROR,

        # =========== BOOL == CHAR ===========
        (Types.BOOL, Types.CHAR, Operations.SUMA): Types.ERROR,
        (Types.BOOL, Types.CHAR, Operations.RESTA): Types.ERROR,
        (Types.BOOL, Types.CHAR, Operations.MULT): Types.ERROR,
        (Types.BOOL, Types.CHAR, Operations.DIVISION): Types.ERROR,
        (Types.BOOL, Types.CHAR, Operations.Y_SIMBOLO): Types.ERROR,
        (Types.BOOL, Types.CHAR, Operations.O_SIMBOLO): Types.ERROR,
        (Types.BOOL, Types.CHAR, Operations.IGUAL): Types.ERROR,
        (Types.BOOL, Types.CHAR, Operations.MAYOR): Types.ERROR,
        (Types.BOOL, Types.CHAR, Operations.MENOR): Types.ERROR,
        (Types.BOOL, Types.CHAR, Operations.DIFERENTE): Types.ERROR,
        (Types.BOOL, Types.CHAR, Operations.ASIGNAR): Types.ERROR,
    }
