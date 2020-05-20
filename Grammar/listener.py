from antlr4 import *
from AangLexer import AangLexer
from AangListener import AangListener
from AangParser import AangParser
from stack import stack
from avail import avail
from quadruple import Quadruple
from Function import Function
from Function import FunctionDir
from Variable import Variable
from Variable import VariableTable
from SemanticCube import SemanticCube, Types
from memory import memory
from Constant import ConstantTable, Constant


import sys


class AangCustomListener(AangListener):
    PilaO = stack()
    PilaOper = stack()
    Avail = avail()
    PSaltos = stack()
    FilaQuads = []
    FilaQuadsMemoria = []
    PilaTipos = stack()
    memoriaGlobal = memory(10000, 20000, 30000, 40000)
    memoriaConstante = memory(90000, 100000, 110000, 0)

    # Memory address
    # global varTable
    global varIntAddr
    global varCharAddr

    functionDirectory = FunctionDir()
    varTable = VariableTable({})
    constTable = ConstantTable()

    def enterPrograma(self, ctx: AangParser.ProgramaContext):
        pass

    def exitPrograma(self, ctx: AangParser.ProgramaContext):
        for index, quad in enumerate(self.FilaQuads, 1):
            print(index, quad)
        for index, quad in enumerate(self.FilaQuadsMemoria, 1):
            print(index, quad)

    def enterE(self, ctx: AangParser.EContext):
        if ctx.MAYOR() != None:
            self.PilaOper.push(str(ctx.MAYOR()))
        if ctx.MENOR() != None:
            self.PilaOper.push(str(ctx.MENOR()))
        if ctx.IGUAL() != None:
            self.PilaOper.push(str(ctx.IGUAL()))
        if ctx.DIFERENTE() != None:
            self.PilaOper.push(str(ctx.DIFERENTE()))
        pass

    def exitExpresion(self, ctx: AangParser.ExpresionContext):
        pass

    def exitE(self, ctx: AangParser.EContext):
        if ctx.MAYOR() != None or ctx.MENOR() != None or ctx.IGUAL() != None or ctx.DIFERENTE() != None:
            operator = self.PilaOper.pop()
            leftOperand = self.PilaO.pop()
            rightOperand = self.PilaO.pop()
            Type = SemanticCube().cube[rightOperand[1],
                                       leftOperand[1], operator]
            if Type == Types().ERROR:
                raise Exception(Types().ERROR)
            self.PilaO.push((self.Avail.newElement(), Type,
                             self.memoriaGlobal.getTemporales()))
            result = self.PilaO.top()
            quad = Quadruple(
                operator, rightOperand[0], leftOperand[0], result[0])
            self.FilaQuads.append(quad)
            quad2 = Quadruple(
                operator, rightOperand[2], leftOperand[2], result[2])
            self.FilaQuadsMemoria.append(quad2)
        pass

    def enterAsignacion(self, ctx: AangParser.AsignacionContext):
        self.PilaOper.push(str(ctx.ASIGNAR()))

    def exitAsignacion(self, ctx: AangParser.AsignacionContext):
        operator = self.PilaOper.pop()
        leftOperand = self.PilaO.pop()
        rightOperand = None
        result = (str(ctx.ID()), self.varTable.vars[str(
            ctx.ID())].dataType, self.varTable.vars[str(
                ctx.ID())].memoryDir)
        if SemanticCube().cube[result[1], leftOperand[1], operator] == Types().ERROR:
            raise Exception(Types().ERROR)

        quad = Quadruple(operator, leftOperand[0], rightOperand, result[0])
        self.FilaQuads.append(quad)
        quad2 = Quadruple(
            operator, leftOperand[2], rightOperand, result[2])
        self.FilaQuadsMemoria.append(quad2)

    def enterEscribir(self, ctx: AangParser.EscribirContext):
        self.PilaOper.push(str(ctx.PRINT()))
        pass

    def exitEscribir(self, ctx: AangParser.EscribirContext):
        operator = self.PilaOper.pop()
        leftOperand = self.PilaO.pop()
        rightOperand = None
        result = None
        quad = Quadruple(operator, leftOperand[0], rightOperand, result)
        self.FilaQuads.append(quad)
        quad2 = Quadruple(operator, leftOperand[2], rightOperand, result)
        self.FilaQuadsMemoria.append(quad2)
        pass

    def enterExp(self, ctx: AangParser.ExpContext):
        # print('Entre a Exp')
        pass

    def exitExp(self, ctx: AangParser.ExpContext):
        # print('Sali de Exp')
        pass

    def enterE1(self, ctx: AangParser.E1Context):
        # print('Entre a E1')
        # print(ctx.RESTA())
        if ctx.SUMA() != None:
            self.PilaOper.push(str(ctx.SUMA()))
        if ctx.RESTA() != None:
            self.PilaOper.push(str(ctx.RESTA()))

    def exitE1(self, ctx: AangParser.E1Context):
        # print('Sali de E1')
        pass

    def enterFactor(self, ctx: AangParser.FactorContext):
        # print('Entre a Factor')
        if ctx.I_PARENTESIS() != None:
            self.PilaOper.push(str(ctx.I_PARENTESIS()))
        pass

    def exitFactor(self, ctx: AangParser.FactorContext):
        # print('Sali de Factor')
        if ctx.D_PARENTESIS() != None:
            self.PilaOper.pop()

        if(self.PilaOper.top() == '/' or self.PilaOper.top() == '*'):
            operator = str(self.PilaOper.pop())
            rightOperand = self.PilaO.pop()
            leftOperand = self.PilaO.pop()
            Type = SemanticCube().cube[rightOperand[1],
                                       leftOperand[1], operator]
            if Type == Types().ERROR:
                raise Exception(Types().ERROR)
            self.PilaO.push((self.Avail.newElement(), Type,
                             self.memoriaGlobal.getTemporales()))
            result = self.PilaO.top()
            quad = Quadruple(
                operator, leftOperand[0], rightOperand[0], result[0])
            self.FilaQuads.append(quad)
            quad2 = Quadruple(
                operator, leftOperand[2], rightOperand[2], result[2])
            self.FilaQuadsMemoria.append(quad2)

    def enterCte_var(self, ctx):
        pass

    def exitCte_var(self, ctx: AangParser.Cte_varContext):
        if ctx.CTE_INT() != None:
            if not self.constTable.get_constant(ctx.CTE_INT()):
                self.constTable.add_constant(
                    str(ctx.CTE_INT()), "int", self.memoriaConstante.getEntera())
            self.PilaO.push((int(str(ctx.CTE_INT())), "int",
                             self.constTable.constants[str(ctx.CTE_INT())].memoryDir))
        elif ctx.CTE_CHAR() != None:
            if not self.constTable.get_constant(ctx.CTE_CHAR()):
                self.constTable.add_constant(
                    str(ctx.CTE_CHAR()), "char", self.memoriaConstante.getChar())
                self.PilaO.push((str(ctx.CTE_CHAR()), "char", self.constTable.constants[str(
                    ctx.CTE_CHAR())].memoryDir))
        elif ctx.CTE_BOOL() != None:

            if not self.constTable.get_constant(ctx.CTE_BOOL()):
                self.constTable.add_constant(
                    str(ctx.CTE_BOOL()), "bool", self.memoriaConstante.getBooleanos())
                self.PilaO.push((str(ctx.CTE_BOOL()), "bool", self.constTable.constants[str(
                    ctx.CTE_BOOL())].memoryDir))
        elif ctx.ID() != None:
            self.PilaO.push(
                (str(ctx.ID()), self.varTable.vars[str(ctx.ID())].dataType, self.varTable.vars[str(ctx.ID())].memoryDir))

        # for constant in self.constTable.constants.values():
        #    print(constant.memoryDir)

    def enterTermino(self, ctx: AangParser.TerminoContext):
        # print('Entre a Termino')
        pass

    def exitTermino(self, ctx: AangParser.TerminoContext):
        # print(self.PilaO.items)
        if(self.PilaOper.top() == '-' or self.PilaOper.top() == '+'):
            operator = str(self.PilaOper.pop())
            rightOperand = self.PilaO.pop()
            leftOperand = self.PilaO.pop()
            Type = SemanticCube().cube[rightOperand[1],
                                       leftOperand[1], operator]
            if Type == Types().ERROR:
                raise Exception(Types().ERROR)
            self.PilaO.push((self.Avail.newElement(), Type,
                             self.memoriaGlobal.getTemporales()))
            result = self.PilaO.top()
            quad = Quadruple(
                operator, leftOperand[0], rightOperand[0], result[0])
            self.FilaQuads.append(quad)
            quad2 = Quadruple(
                operator, leftOperand[2], rightOperand[2], result[2])
            self.FilaQuadsMemoria.append(quad2)
        # print('Sali de Termino')

    def enterT(self, ctx: AangParser.TContext):
        # print('Entre a T')
        if ctx.MULT() != None:
            self.PilaOper.push(str(ctx.MULT()))
        if ctx.DIVISION() != None:
            self.PilaOper.push(str(ctx.DIVISION()))
        # print(self.PilaOper.items)

    def exitT(self, ctx: AangParser.TContext):
        # print('Sali de T')
        pass

    # def add_var(self, ctx):
    #    global varName
    #    # cast to string to avoid dealing with TerminalNode objects
    #    varName = str(ctx.ID())
    #    if varName != "None":
    #        if dataType == 'int':
    #            global varIntAddr
    #            VariableTable.add_variable(
    #                varName, dataType, "global", varIntAddr)
    #            varIntAddr = varIntAddr + 1
    #        else:
    #            global varCharAddr
    #            VariableTable.add_variable(
    #                varName, dataType, "global", varCharAddr)
    #            varCharAddr = varCharAddr + 1

    # def enterV(self, ctx):
    #    self.addVar(ctx)

    # def enterV1(self, ctx):
    #    self.addVar(ctx)

    # Enter a parse tree produced by AangParser#variable.
    def enterVariable(self, ctx: AangParser.VariableContext):
        # print('entre a Variable')
        pass

    # Exit a parse tree produced by AangParser#variable.
    def exitVariable(self, ctx: AangParser.VariableContext):
        # print('sali de variable')
        self.PilaTipos.pop()
        # for variable in self.varTable.vars:
        #    print(self.varTable.vars[variable].memoryDir)
        pass

    # Enter a parse tree produced by AangParser#tipo_id.
    def enterTipo_id(self, ctx: AangParser.Tipo_idContext):
        # print('entre a tipo id')
        # self.PilaTipos.push(str())
        if ctx.INT() != None:
            self.PilaTipos.push(str(ctx.INT()))
        if ctx.CHAR() != None:
            self.PilaTipos.push(str(ctx.CHAR()))
        if ctx.BOOL() != None:
            self.PilaTipos.push(str(ctx.BOOL()))
        # print(self.PilaTipos.items)

    # Exit a parse tree produced by AangParser#tipo_id.
    def exitTipo_id(self, ctx: AangParser.Tipo_idContext):
        # print('sali de Tipo id')
        pass

    # Enter a parse tree produced by AangParser#v.
    def enterV(self, ctx: AangParser.VContext):
        # print('entre a V')
        direccion = 0
        if self.PilaTipos.top() == 'int':
            direccion = self.memoriaGlobal.getEntera()
        elif self.PilaTipos.top() == 'char':
            direccion = self.memoriaGlobal.getChar()
        elif self.PilaTipos.top() == 'bool':
            direccion = self.memoriaGlobal.getBooleanos()
        self.varTable.add_variable(
            str(ctx.ID()), self.PilaTipos.top(), "global", direccion, None)
        pass

    # Exit a parse tree produced by AangParser#v.
    def exitV(self, ctx: AangParser.VContext):
        # print('sali de V')
        pass

    # Enter a parse tree produced by AangParser#v1.
    def enterV1(self, ctx: AangParser.V1Context):
        # print('entre a V1')
        if ctx.ID() != None:
            direccion = 0
            if self.PilaTipos.top() == 'int':
                direccion = self.memoriaGlobal.getEntera()
            elif self.PilaTipos.top() == 'char':
                direccion = self.memoriaGlobal.getChar()
            elif self.PilaTipos.top() == 'bool':
                direccion = self.memoriaGlobal.getBooleanos()
            self.varTable.add_variable(
                str(ctx.ID()), self.PilaTipos.top(), "global", direccion, None)

    # Exit a parse tree produced by AangParser#v1.
    def exitV1(self, ctx: AangParser.V1Context):
        # print('salir de V1')
        pass

    # Enter a parse tree produced by AangParser#v2.
    def enterV2(self, ctx: AangParser.V2Context):
        # print('entre a V2')
        pass

    # Exit a parse tree produced by AangParser#v2.
    def exitV2(self, ctx: AangParser.V2Context):
        # print('sali de V2')
        pass

    ###### Condicion ######
    def enterC1(self, ctx: AangParser.C1Context):
        if(self.PilaO.top()[1] != 'bool'):
            raise Exception(
                "El resultado del la condicion del if no es booleano")
        operator = "GotoF"
        rightOperand = self.PilaO.pop()
        leftOperand = None
        result = "vacio"
        quad = Quadruple(
            operator, rightOperand[0], leftOperand, result)
        self.FilaQuads.append(quad)
        quad2 = Quadruple(
            operator, rightOperand[2], leftOperand, result)
        self.FilaQuadsMemoria.append(quad2)
        self.PSaltos.push(len(self.FilaQuads)-1)
        pass

    def exitC1(self, ctx: AangParser.C1Context):
        pass

    # Enter a parse tree produced by AangParser#c2.
    def enterC2(self, ctx: AangParser.C2Context):
        if ctx.ELSE() == None:
            numeroQuad = self.PSaltos.pop()
            # Pila normal
            self.FilaQuads[numeroQuad].result = len(self.FilaQuads) + 1
            # Pila Direcciones
            self.FilaQuadsMemoria[numeroQuad].result = len(
                self.FilaQuadsMemoria) + 1

        else:
            operator = "Goto"
            rightOperand = None
            leftOperand = None
            result = "vacio"
            quad = Quadruple(
                operator, rightOperand, leftOperand, result)
            quad2 = Quadruple(
                operator, rightOperand, leftOperand, result)
            self.FilaQuads.append(quad)
            self.FilaQuadsMemoria.append(quad2)
            numeroQuad = self.PSaltos.pop()
            self.FilaQuads[numeroQuad].result = len(self.FilaQuads) + 1
            self.FilaQuadsMemoria[numeroQuad].result = len(
                self.FilaQuadsMemoria) + 1
            self.PSaltos.push(len(self.FilaQuads))

    # Exit a parse tree produced by AangParser#c2.

    def exitC2(self, ctx: AangParser.C2Context):
        if ctx.ELSE() != None:
            self.FilaQuads[self.PSaltos.pop(
            )-1].result = len(self.FilaQuads) + 1
        pass

    # Enter a parse tree produced by AangParser#ciclo1.
    def enterCiclo1(self, ctx: AangParser.Ciclo1Context):
        self.PSaltos.push(len(self.FilaQuads) + 1)
        pass

    # Exit a parse tree produced by AangParser#ciclo1.
    def exitCiclo1(self, ctx: AangParser.Ciclo1Context):
        pass

    # Enter a parse tree produced by AangParser#ciclo2.
    def enterCiclo2(self, ctx: AangParser.Ciclo2Context):
        if(self.PilaO.top()[1] != 'bool'):
            raise Exception(
                "El resultado del la condicion del if no es booleano")
        operator = "GotoF"
        rightOperand = self.PilaO.pop()
        leftOperand = None
        result = "vacio"
        quad = Quadruple(
            operator, rightOperand[0], leftOperand, result)
        self.FilaQuads.append(quad)
        quad2 = Quadruple(
            operator, rightOperand[2], leftOperand, result)
        self.FilaQuadsMemoria.append(quad2)
        self.PSaltos.push(len(self.FilaQuads))
        pass

    # Exit a parse tree produced by AangParser#ciclo2.
    def exitCiclo2(self, ctx: AangParser.Ciclo2Context):
        operator = "Goto"
        rightOperand = None
        leftOperand = None
        result = "vacio"
        quad = Quadruple(
            operator, rightOperand, leftOperand, result)
        quad2 = Quadruple(
            operator, rightOperand, leftOperand, result)
        self.FilaQuads.append(quad)
        self.FilaQuadsMemoria.append(quad2)
        numeroQuad = self.PSaltos.pop()
        self.FilaQuads[numeroQuad-1].result = len(self.FilaQuads) + 1
        self.FilaQuadsMemoria[numeroQuad -
                              1].result = len(self.FilaQuadsMemoria) + 1
        numeroQuad = self.PSaltos.pop()
        self.FilaQuads[len(self.FilaQuads)-1].result = numeroQuad
        self.FilaQuadsMemoria[len(self.FilaQuadsMemoria)-1].result = numeroQuad
        pass
