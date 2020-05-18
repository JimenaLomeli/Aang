from antlr4 import *
from AangLexer import AangLexer
from AangListener import AangListener
from AangParser import AangParser
from stack import stack
from avail import avail
from quadruple import Quadruple


import sys


class AangCustomListener(AangListener):
    PilaO = stack()
    PilaOper = stack()
    Avail = avail()
    PSaltos = stack()
    quads = []

    def enterPrograma(self, ctx: AangParser.ProgramaContext):
        pass

    def enterE(self, ctx: AangParser.EContext):
        # if ctx.MAYOR() != None:
        #     self.PilaOper.push(str(ctx.MAYOR()))
        # if ctx.MENOR() != None:
        #     self.PilaOper.push(str(ctx.MENOR()))
        # if ctx.IGUAL() != None:
        #     self.PilaOper.push(str(ctx.IGUAL()))
        # if ctx.DIFERENTE() != None:
        #     self.PilaOper.push(str(ctx.DIFERENTE()))
        pass

    def exitExpresion(self, ctx: AangParser.ExpresionContext):
        pass

    def exitE(self, ctx: AangParser.EContext):
        # print(self.PilaO.items)
        # operator = self.PilaOper.pop()
        # leftOperand = self.PilaO.pop()
        # rightOperand = self.PilaO.pop()
        # self.PilaO.push(self.Avail.newElement())
        # result = str(self.PilaO.top())
        # quad = Quadruple(operator, leftOperand, rightOperand, result)
        # quad.printQuad()
        pass

    def enterAsignacion(self, ctx: AangParser.AsignacionContext):
        self.PilaOper.push(str(ctx.ASIGNAR()))

    def exitAsignacion(self, ctx: AangParser.AsignacionContext):
        operator = self.PilaOper.pop()
        leftOperand = self.PilaO.pop()
        rightOperand = None
        result = str(ctx.ID())
        quad = Quadruple(operator, leftOperand, rightOperand, result)
        quad.printQuad()

    def enterEscribir(self, ctx: AangParser.EscribirContext):
        self.PilaOper.push(str(ctx.PRINT()))
        pass

    def exitEscribir(self, ctx: AangParser.EscribirContext):
        operator = self.PilaOper.pop()
        leftOperand = self.PilaO.pop()
        rightOperand = None
        result = None
        quad = Quadruple(operator, leftOperand, rightOperand, result)
        quad.printQuad()
        pass

    def enterExp(self, ctx: AangParser.ExpContext):
        #print('Entre a Exp')
        pass

    def exitExp(self, ctx: AangParser.ExpContext):
        #print('Sali de Exp')
        pass

    def enterE1(self, ctx: AangParser.E1Context):
        #print('Entre a E1')
        # print(ctx.RESTA())
        if ctx.SUMA() != None:
            self.PilaOper.push(str(ctx.SUMA()))
        if ctx.RESTA() != None:
            self.PilaOper.push(str(ctx.RESTA()))

    def exitE1(self, ctx: AangParser.E1Context):
        #print('Sali de E1')
        pass

    def enterFactor(self, ctx: AangParser.FactorContext):
        #print('Entre a Factor')
        pass

    def exitFactor(self, ctx: AangParser.FactorContext):
        #print('Sali de Factor')
        if(self.PilaOper.top() == '/' or self.PilaOper.top() == '*'):
            operator = str(self.PilaOper.pop())
            rightOperand = str(self.PilaO.pop())
            leftOperand = str(self.PilaO.pop())
            self.PilaO.push(self.Avail.newElement())
            result = str(self.PilaO.top())
            quad = Quadruple(operator, leftOperand, rightOperand, result)
            quad.printQuad()

    def enterCte_var(self, ctx):
        pass

    def exitCte_var(self, ctx: AangParser.Cte_varContext):
        if ctx.CTE_INT() != None:
            self.PilaO.push(int(str(ctx.CTE_INT())))
        if ctx.ID() != None:
            self.PilaO.push(str(ctx.ID()))
        # print(self.PilaO.items)

    def enterTermino(self, ctx: AangParser.TerminoContext):
        #print('Entre a Termino')
        pass

    def exitTermino(self, ctx: AangParser.TerminoContext):
        # print(self.PilaO.items)
        if(self.PilaOper.top() == '-' or self.PilaOper.top() == '+'):
            operator = str(self.PilaOper.pop())
            rightOperand = str(self.PilaO.pop())
            leftOperand = str(self.PilaO.pop())
            self.PilaO.push(self.Avail.newElement())
            result = str(self.PilaO.top())
            quad = Quadruple(operator, leftOperand, rightOperand, result)
            #print('Operador: ' + operator)
            #print('Operando Izquierdo: ' + leftOperand)
            #print('Operando Derecho: ' + rightOperand)
            #print('Resultado:' + result)
            #print(f'[{operator}, {leftOperand}, {rightOperand}, {result}]')
            quad.printQuad()
        #print('Sali de Termino')

    def enterT(self, ctx: AangParser.TContext):
        #print('Entre a T')
        if ctx.MULT() != None:
            self.PilaOper.push(str(ctx.MULT()))
        if ctx.DIVISION() != None:
            self.PilaOper.push(str(ctx.DIVISION()))
        # print(self.PilaOper.items)

    def exitT(self, ctx: AangParser.TContext):
        #print('Sali de T')
        pass
