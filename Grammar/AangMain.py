
import sys
from antlr4 import *

from AangLexer import AangLexer
from AangParser import AangParser
from AangListener import AangListener
from antlr4.tree.Trees import Trees

# class AangListener(AangListener):

# 	def exitEscribir(self, ctx:AangParser.EscribirContext):
# 		print(ctx.D_PARENTESIS())

if len(sys.argv) < 2:
    print("You must provide the file you want to compile")
    exit()
try:
    aangFile = FileStream(sys.argv[1])
except Exception:
    print(f"Could not read {sys.argv[1]}")
    exit()

lexer = AangLexer(aangFile)
stream = CommonTokenStream(lexer)
parser = AangParser(stream)
	#printer = AangListener()
	#walker = ParseTreeWalker()
tree = parser.programa()
	#walker.walk(printer, tree)		
	#print(Trees.toStringTree(tree, None, parser)) # this function prints the grammar rules that were recognized
