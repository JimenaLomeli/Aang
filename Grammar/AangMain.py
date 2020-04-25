
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

# Extend the CharmsParserListener class generated by ANTLR to modify it accordingly
class AangPrintListener(AangListener):
	def add_var(self, ctx):
		global varName
		varName = str(ctx.ID()) # cast to string to avoid dealing with TerminalNode objects
		if varName != "None":
			if dataType == 'int':
				global varIntAddr
				varTable.add_variable(varName, dataType, "global", varIntAddr)
				varIntAddr = varIntAddr + 1
			else:
				global varCharAddr
				varTable.add_variable(varName, dataType, "global", varCharAddr)
				varCharAddr = varCharAddr + 1

	def enterV(self, ctx):
		self.addVar(ctx)

	def enterV1(self, ctx):
		self.addVar(ctx)

def main(argv):

	# Memory address
	global varTable
	global varIntAddr
	global varCharAddr

	functionDirectory = FunctionDir()
	varTable = VariableTable({}, ["int", "void", "char", "if", "else", "while", "print", "return", "id", "programa", "empezar", "fin"])


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

