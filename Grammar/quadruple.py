from antlr4 import *
from Function import *
from Variable import *
from AangMain import *

class Quadruple:
    def __init__(self, operator, leftOp, rightOp, result):
        self.operator = operator
        self.leftOp = leftOp
        self.rightOp = rightOp
        self.result = result

       def printQuad(self):
        print(self.operator, '\t', self.leftOp, '\t', self.rightOp, '\t', self.result)

