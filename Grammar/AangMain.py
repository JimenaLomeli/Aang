
# Authors:
# Ana Jimena Lomeli Cantu
# Jorge Andres Sabella


import sys
from antlr4 import *

from AangLexer import AangLexer
from AangParser import AangParser
from AangListener import AangListener
from antlr4.tree.Trees import Trees
from Function import Function
from Function import FunctionDir
from Variable import Variable
from Variable import VariableTable
from listener import AangCustomListener
from errorListener import myErrorListener
from errorListener import errores


# Extend the CharmsParserListener class generated by ANTLR to modify it accordingly


def main(argv):
    # Memory address
    global varTable
    global varIntAddr
    global varCharAddr

    functionDirectory = FunctionDir()


#print(SemanticCube().cube[('char', 'char', '=')])

if len(sys.argv) < 2:
    print("You must provide the file you want to compile")
    exit()
try:
    aangFile = FileStream(sys.argv[1])

except Exception:
    print(f"Could not read {sys.argv[1]}")
    exit()
#output = open("output.txt", "w")

lexer = AangLexer(aangFile)
stream = CommonTokenStream(lexer)
parser = AangParser(stream)
err = errores()
printer = AangCustomListener()
walker = ParseTreeWalker()

try:
    tree = parser.programa()
except SystemExit:
    log.write("\n")
    log.close()
    sys.exit(1)

try:
    walker.walk(printer, tree)
except SystemExit:
    if len(err.errorr) > 0:
        for elem in err.errors:
            if args.show_logs:
                print(elem.msg)
            log.write(elem.msg+"\n")
    log.write("\n")
    log.close()
    sys.exit(1)


# this function prints the grammar rules that were recognized
#print(Trees.toStringTree(tree, None, parser))
# output.close()

if __name__ == '__main__':
    main(sys.argv)
