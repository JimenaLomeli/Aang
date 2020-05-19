from antlr4 import *


class Quadruple:
    def __init__(self, operator, leftOp, rightOp, result):
        self.operator = operator
        self.leftOp = leftOp
        self.rightOp = rightOp
        self.result = result

    def printQuad(self):
        print(f'[{self.operator}, {self.leftOp}, {self.rightOp}, {self.result}]')

    def __str__(self):
        return "[" + str(self.operator) + ", " + str(self.leftOp) + ", " + str(self.rightOp) + ", " + str(self.result) + "]"
