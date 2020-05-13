from antlr4 import *
from AangLexer import AangLexer
from AangListener import AangListener
from AangParser import AangParser
from stack import stack
from avail import avail


import sys


class AangCustomListener(AangListener):
    PilaO = stack()
    PilaOper = stack()
    Avail = avail()

    def enterPrograma(self, ctx: AangParser.ProgramaContext):
        pass

    def exitFactor(self, ctx: AangParser.FactorContext):
        if(self.PilaOper.top() == '/' or self.PilaOper.top() == '*'):
            print('Operador: ' + str(self.PilaOper.pop()))
            print('Operando Derecho: ' + str(self.PilaO.pop()))
            print('Operando Izquierdo: ' + str(self.PilaO.pop()))
            self.PilaO.push(self.Avail.newElement())
            print('Resultado:' + str(self.PilaO.top()))

    def enterCte_var(self, ctx):
        pass

    def exitCte_var(self, ctx: AangParser.Cte_varContext):
        if ctx.CTE_INT() != None:
            self.PilaO.push(int(str(ctx.CTE_INT())))

    def enterTermino(self, ctx: AangParser.TerminoContext):
        pass

    def exitTermino(self, ctx: AangParser.TerminoContext):
        print(self.PilaOper.items)
        print(self.PilaO.items)
        if(self.PilaOper.top() == '-' or self.PilaOper.top() == '+'):
            print('Operador: ' + str(self.PilaOper.pop()))
            print('Operando Derecho: ' + str(self.PilaO.pop()))
            print('Operando Izquierdo: ' + str(self.PilaO.pop()))
            self.PilaO.push(self.Avail.newElement())
            print('Resultado:' + str(self.PilaO.top()))

    def enterT(self, ctx: AangParser.TContext):
        if ctx.MULT() != None:
            self.PilaOper.push(str(ctx.MULT()))
            print(self.PilaOper.items)
        if ctx.DIVISION() != None:
            self.PilaOper.push(str(ctx.DIVISION()))

    def exitT(self, ctx: AangParser.TContext):
        pass

    def enterE1(self, ctx: AangParser.E1Context):
        if ctx.SUMA() != None:
            self.PilaOper.push(str(ctx.SUMA()))
        if ctx.RESTA() != None:
            self.PilaOper.push(str(ctx.RESTA()))

    def exitE1(self, ctx: AangParser.E1Context):
        pass
