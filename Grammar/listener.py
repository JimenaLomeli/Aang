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
import pickle


class AangCustomListener(AangListener):
    PilaO = stack()
    PilaOper = stack()
    Avail = avail()
    PSaltos = stack()
    FilaQuads = []
    FilaQuadsMemoria = []
    PilaTipos = stack()
    PilaFunc = stack()
    PilaFuncParam = stack()
    PilaArr = stack()
    ParameterCounter = 0
    TempParameters = []
    memoriaGlobal = memory(1000, 2000, 3000, 0)
    memoriaConstante = memory(7000, 8000, 9000, 0)
    memoriaTemporal = memory(10000, 11000, 12000, 0)

    # Memory address
    # global varTable
    global varIntAddr
    global varCharAddr

    functionDirectory = FunctionDir()
    varTable = VariableTable({})
    constTable = ConstantTable()
    localVarTable = VariableTable({})

# ========================== PROGRAMA ==========================

    def enterPrograma(self, ctx: AangParser.ProgramaContext):
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
        pass

    def exitPrograma(self, ctx: AangParser.ProgramaContext):
        operator = "Exit"
        rightOperand = None
        leftOperand = None
        result = None
        quad = Quadruple(
            operator, rightOperand, leftOperand, result)
        quad2 = Quadruple(
            operator, rightOperand, leftOperand, result)
        self.FilaQuads.append(quad)
        self.FilaQuadsMemoria.append(quad2)

        for index, quad in enumerate(self.FilaQuads, 1):
            print(index, quad)

        for index, quad in enumerate(self.FilaQuadsMemoria, 1):
            print(index, quad)

        # ========== CUADRUPLOS PARA VM =========
        pickle_out = open("Quadruplos.pickle", "wb")
        pickle.dump(self.FilaQuadsMemoria, pickle_out)
        pickle.dump(self.functionDirectory, pickle_out)
        pickle.dump(self.constTable, pickle_out)
        pickle_out.close()

    def enterExpresion(self, ctx: AangParser.ExpresionContext):
        if ctx.Y_SIMBOLO() != None:
            self.PilaOper.push(str(ctx.Y_SIMBOLO()))
        if ctx.O_SIMBOLO() != None:
            self.PilaOper.push(str(ctx.O_SIMBOLO()))

    def exitExpresion(self, ctx: AangParser.ExpresionContext):
        if ctx.Y_SIMBOLO() != None or ctx.O_SIMBOLO() != None:
            operator = self.PilaOper.pop()
            leftOperand = self.PilaO.pop()
            rightOperand = self.PilaO.pop()
            Type = SemanticCube().cube[rightOperand[1],
                                       leftOperand[1], operator]
            if Type == Types().ERROR:
                raise Exception(Types().ERROR)
            elif Type == Types().INT:
                self.PilaO.push((self.Avail.newElement(), Type,
                                 self.memoriaTemporal.getEntera()))
            elif Type == Types().CHAR:
                self.PilaO.push((self.Avail.newElement(), Type,
                                 self.memoriaTemporal.getChar()))
            elif Type == Types().BOOL:
                self.PilaO.push((self.Avail.newElement(), Type,
                                 self.memoriaTemporal.getBooleanos()))
            result = self.PilaO.top()
            quad = Quadruple(
                operator, rightOperand[0], leftOperand[0], result[0])
            self.FilaQuads.append(quad)
            quad2 = Quadruple(
                operator, rightOperand[2], leftOperand[2], result[2])
            self.FilaQuadsMemoria.append(quad2)

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

    def exitE(self, ctx: AangParser.EContext):
        if ctx.MAYOR() != None or ctx.MENOR() != None or ctx.IGUAL() != None or ctx.DIFERENTE() != None:
            operator = self.PilaOper.pop()
            leftOperand = self.PilaO.pop()
            rightOperand = self.PilaO.pop()
            Type = SemanticCube().cube[rightOperand[1],
                                       leftOperand[1], operator]
            if Type == Types().ERROR:
                raise Exception(Types().ERROR)
            elif Type == Types().INT:
                self.PilaO.push((self.Avail.newElement(), Type,
                                 self.memoriaTemporal.getEntera()))
            elif Type == Types().CHAR:
                self.PilaO.push((self.Avail.newElement(), Type,
                                 self.memoriaTemporal.getChar()))
            elif Type == Types().BOOL:
                self.PilaO.push((self.Avail.newElement(), Type,
                                 self.memoriaTemporal.getBooleanos()))
            result = self.PilaO.top()
            quad = Quadruple(
                operator, rightOperand[0], leftOperand[0], result[0])
            self.FilaQuads.append(quad)
            quad2 = Quadruple(
                operator, rightOperand[2], leftOperand[2], result[2])
            self.FilaQuadsMemoria.append(quad2)
        pass

# ========================== ASIGNACION ==========================

    def enterAsignacion(self, ctx: AangParser.AsignacionContext):
        self.PilaOper.push(str(ctx.ASIGNAR()))

    def exitAsignacion(self, ctx: AangParser.AsignacionContext):
        operator = self.PilaOper.pop()
        leftOperand = self.PilaO.pop()
        rightOperand = None
        if len(self.PilaFunc.items) == 0:
            result = (str(ctx.ID()), self.varTable.vars[str(
                ctx.ID())].dataType, self.varTable.vars[str(
                    ctx.ID())].memoryDir)
        else:
            if self.localVarTable.get_local_variable(str(ctx.ID())):
                result = (str(ctx.ID()), self.localVarTable.vars[str(
                    ctx.ID())].dataType, self.localVarTable.vars[str(
                        ctx.ID())].memoryDir)
            else:
                self.varTable.exist(str(ctx.ID()))
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


# ========================== ESCRIBIR ==========================


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

    def enterE1(self, ctx: AangParser.E1Context):
        if ctx.SUMA() != None:
            self.PilaOper.push(str(ctx.SUMA()))
        if ctx.RESTA() != None:
            self.PilaOper.push(str(ctx.RESTA()))

    def enterFactor(self, ctx: AangParser.FactorContext):
        if ctx.I_PARENTESIS() != None:
            self.PilaOper.push(str(ctx.I_PARENTESIS()))
        pass

    def exitFactor(self, ctx: AangParser.FactorContext):
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
            elif Type == Types().INT:
                self.PilaO.push((self.Avail.newElement(), Type,
                                 self.memoriaTemporal.getEntera()))
            elif Type == Types().CHAR:
                self.PilaO.push((self.Avail.newElement(), Type,
                                 self.memoriaTemporal.getChar()))
            elif Type == Types().BOOL:
                self.PilaO.push((self.Avail.newElement(), Type,
                                 self.memoriaTemporal.getBooleanos()))
            result = self.PilaO.top()
            quad = Quadruple(
                operator, leftOperand[0], rightOperand[0], result[0])
            self.FilaQuads.append(quad)
            quad2 = Quadruple(
                operator, leftOperand[2], rightOperand[2], result[2])
            self.FilaQuadsMemoria.append(quad2)


# ========================== CONSTANTES ==========================


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
            # if str(ctx.ID()) == 'b':
            #    print(self.PilaFunc.items)
            if len(self.PilaFunc.items) == 0:
                self.varTable.exist(str(ctx.ID()))
                self.PilaO.push(
                    (str(ctx.ID()), self.varTable.vars[str(ctx.ID())].dataType, self.varTable.vars[str(ctx.ID())].memoryDir))
            else:
                if self.localVarTable.get_local_variable(str(ctx.ID())):
                    self.PilaO.push(
                        (str(ctx.ID()), self.localVarTable.vars[str(ctx.ID())].dataType, self.localVarTable.vars[str(ctx.ID())].memoryDir))
                else:
                    self.varTable.exist(str(ctx.ID()))
                    self.PilaO.push(
                        (str(ctx.ID()), self.varTable.vars[str(ctx.ID())].dataType, self.varTable.vars[str(ctx.ID())].memoryDir))

    def exitTermino(self, ctx: AangParser.TerminoContext):
        if(self.PilaOper.top() == '-' or self.PilaOper.top() == '+'):
            operator = str(self.PilaOper.pop())
            rightOperand = self.PilaO.pop()
            leftOperand = self.PilaO.pop()
            Type = SemanticCube().cube[rightOperand[1],
                                       leftOperand[1], operator]
            if Type == Types().ERROR:
                raise Exception(Types().ERROR)
            elif Type == Types().INT:
                self.PilaO.push((self.Avail.newElement(), Type,
                                 self.memoriaTemporal.getEntera()))
            elif Type == Types().CHAR:
                self.PilaO.push((self.Avail.newElement(), Type,
                                 self.memoriaTemporal.getChar()))
            elif Type == Types().BOOL:
                self.PilaO.push((self.Avail.newElement(), Type,
                                 self.memoriaTemporal.getBooleanos()))
            result = self.PilaO.top()
            quad = Quadruple(
                operator, leftOperand[0], rightOperand[0], result[0])
            self.FilaQuads.append(quad)
            quad2 = Quadruple(
                operator, leftOperand[2], rightOperand[2], result[2])
            self.FilaQuadsMemoria.append(quad2)

    def enterT(self, ctx: AangParser.TContext):
        if ctx.MULT() != None:
            self.PilaOper.push(str(ctx.MULT()))
        if ctx.DIVISION() != None:
            self.PilaOper.push(str(ctx.DIVISION()))


# ========================== VARIABLES ==========================


    def exitVariable(self, ctx: AangParser.VariableContext):
        self.PilaTipos.pop()
        pass

    def enterTipo_id(self, ctx: AangParser.Tipo_idContext):
        if ctx.INT() != None:
            self.PilaTipos.push(str(ctx.INT()))
        if ctx.CHAR() != None:
            self.PilaTipos.push(str(ctx.CHAR()))
        if ctx.BOOL() != None:
            self.PilaTipos.push(str(ctx.BOOL()))

    def enterV(self, ctx: AangParser.VContext):
        if ctx.ID() != None:
            if self.PilaFunc.top() == None:
                direccion = 0
                if self.PilaTipos.top() == 'int':
                    direccion = self.memoriaGlobal.getEntera()
                elif self.PilaTipos.top() == 'char':
                    direccion = self.memoriaGlobal.getChar()
                elif self.PilaTipos.top() == 'bool':
                    direccion = self.memoriaGlobal.getBooleanos()
                self.varTable.add_variable(
                    str(ctx.ID()), self.PilaTipos.top(), "global", direccion)
            else:
                direccion = 0
                if self.PilaTipos.top() == 'int':
                    direccion = self.functionDirectory.getNextInt(
                        self.PilaFunc.top())
                elif self.PilaTipos.top() == 'char':
                    direccion = self.functionDirectory.getNextBool(
                        self.PilaFunc.top())
                elif self.PilaTipos.top() == 'bool':
                    direccion = self.functionDirectory.getNextChar(
                        self.PilaFunc.top())
                self.localVarTable.add_variable(
                    str(ctx.ID()), self.PilaTipos.top(), "local", direccion)
            if ctx.I_LLAVE() != None:
                self.PilaArr.push(str(ctx.ID()))
                if self.PilaFunc.top() == None:
                    self.varTable.setIsArray(str(ctx.ID()))
                else:
                    self.localVarTable.setIsArray(str(ctx.ID()))
        pass

    def enterV3(self, ctx: AangParser.VContext):
        if self.PilaArr.top() != None:
            if self.PilaFunc.top() == None:
                # El limite superior es igual al tamaño del arreglo menos 1
                self.varTable.setLSup(
                    self.PilaArr.top(), self.PilaO.pop()[0])
                if self.PilaTipos.top() == 'int':
                    self.memoriaGlobal.i = self.memoriaGlobal.i + \
                        self.varTable.getLSup(self.PilaArr.top()) - 1
                if self.PilaTipos.top() == 'bool':
                    self.memoriaGlobal.b = self.memoriaGlobal.b + \
                        self.varTable.getLSup(self.PilaArr.top()) - 1
                if self.PilaTipos.top() == 'char':
                    self.memoriaGlobal.c = self.memoriaGlobal.c + \
                        self.varTable.getLSup(self.PilaArr.top()) - 1
            else:
                # El limite superior es igual al tamaño del arreglo menos 1
                self.localVarTable.setLSup(
                    str(ctx.ID()), self.PilaO.pop()[0])
                self.localVarTable.setLSup(
                    self.PilaArr.top(), self.PilaO.pop()[0])
                if self.PilaTipos.top() == 'int':
                    self.memoriaGlobal.i = self.memoriaGlobal.i + \
                        self.localVarTable.getLSup(self.PilaArr.top()) - 1
                if self.PilaTipos.top() == 'bool':
                    self.memoriaGlobal.b = self.memoriaGlobal.b + \
                        self.localVarTable.getLSup(self.PilaArr.top()) - 1
                if self.PilaTipos.top() == 'char':
                    self.memoriaGlobal.c = self.memoriaGlobal.c + \
                        self.localVarTable.getLSup(self.PilaArr.top()) - 1
            self.PilaArr.pop()

    def enterV1(self, ctx: AangParser.V1Context):
        if ctx.ID() != None:
            if self.PilaFunc.top() == None:
                direccion = 0
                if self.PilaTipos.top() == 'int':
                    direccion = self.memoriaGlobal.getEntera()
                elif self.PilaTipos.top() == 'char':
                    direccion = self.memoriaGlobal.getChar()
                elif self.PilaTipos.top() == 'bool':
                    direccion = self.memoriaGlobal.getBooleanos()
                self.varTable.add_variable(
                    str(ctx.ID()), self.PilaTipos.top(), "global", direccion)
            else:
                direccion = 0
                if self.PilaTipos.top() == 'int':
                    direccion = self.functionDirectory.getNextInt(
                        self.PilaFunc.top())
                elif self.PilaTipos.top() == 'char':
                    direccion = self.functionDirectory.getNextBool(
                        self.PilaFunc.top())
                elif self.PilaTipos.top() == 'bool':
                    direccion = self.functionDirectory.getNextChar(
                        self.PilaFunc.top())
                self.localVarTable.add_variable(
                    str(ctx.ID()), self.PilaTipos.top(), "local", direccion)
            if ctx.I_LLAVE() != None:
                self.PilaArr.push(str(ctx.ID()))
                if self.PilaFunc.top() == None:
                    self.varTable.setIsArray(str(ctx.ID()))
                else:
                    self.localVarTable.setIsArray(str(ctx.ID()))


# ========================== CONDICION ==========================


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

    def exitC2(self, ctx: AangParser.C2Context):
        if ctx.ELSE() != None:
            salto = self.PSaltos.pop()-1
            self.FilaQuads[salto].result = len(self.FilaQuads) + 1
            self.FilaQuadsMemoria[salto].result = len(self.FilaQuads) + 1


# ========================== CICLO ==========================


    def enterCiclo1(self, ctx: AangParser.Ciclo1Context):
        self.PSaltos.push(len(self.FilaQuads) + 1)
        pass

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

    def enterFuncion(self, ctx: AangParser.FuncionContext):
        self.functionDirectory.add_function(str(ctx.ID()))
        self.PilaFunc.push(str(ctx.ID()))
        self.localVarTable = VariableTable({})
        self.functionDirectory.setStartPosition(
            self.PilaFunc.top(), len(self.FilaQuadsMemoria) + 1)
        pass

    def exitFuncion(self, ctx: AangParser.FuncionContext):
        self.functionDirectory.setLocalVariables(
            self.PilaFunc.top(), len(self.localVarTable.vars))
        self.functionDirectory.setTemporalVariables(
            self.PilaFunc.top(), self.memoriaGlobal.t)
        self.PilaFunc.pop()
        operator = "EndFunc"
        rightOperand = None
        leftOperand = None
        result = None
        quad = Quadruple(
            operator, rightOperand, leftOperand, result)
        quad2 = Quadruple(
            operator, rightOperand, leftOperand, result)
        self.FilaQuads.append(quad)
        self.FilaQuadsMemoria.append(quad2)
        # self.memoriaGlobal.resetTemporales()

    def exitF(self, ctx: AangParser.FContext):
        if ctx.VOID() != None:
            self.functionDirectory.setReturnType(
                self.PilaFunc.top(), str(ctx.VOID()))
        else:
            self.functionDirectory.setReturnType(
                self.PilaFunc.top(), self.PilaTipos.pop())
        pass

    def exitF1(self, ctx: AangParser.F1Context):
        if ctx.ID() != None:
            tipo = self.PilaTipos.pop()
            self.functionDirectory.addParameter(
                self.PilaFunc.top(), tipo)
            if tipo == "int":
                self.localVarTable.add_variable(
                    str(ctx.ID()), tipo, "local", self.functionDirectory.getNextInt(self.PilaFunc.top()))
            elif tipo == "bool":
                self.localVarTable.add_variable(
                    str(ctx.ID()), tipo, "local", self.functionDirectory.getNextBool(self.PilaFunc.top()))
            elif tipo == "char":
                self.localVarTable.add_variable(
                    str(ctx.ID()), tipo, "local", self.functionDirectory.getNextChar(self.PilaFunc.top()))

    def exitF2(self, ctx: AangParser.F2Context):
        if ctx.ID() != None:
            tipo = self.PilaTipos.pop()
            self.functionDirectory.addParameter(
                self.PilaFunc.top(), tipo)
            if tipo == "int":
                self.localVarTable.add_variable(
                    str(ctx.ID()), tipo, "local", self.functionDirectory.getNextInt(self.PilaFunc.top()))
            elif tipo == "bool":
                self.localVarTable.add_variable(
                    str(ctx.ID()), tipo, "local", self.functionDirectory.getNextBool(self.PilaFunc.top()))
            elif tipo == "char":
                self.localVarTable.add_variable(
                    str(ctx.ID()), tipo, "local", self.functionDirectory.getNextChar(self.PilaFunc.top()))

    def exitFun_regresar(self, ctx: AangParser.Fun_regresarContext):
        if self.PilaO.top()[1] == self.functionDirectory.getReturnType(self.PilaFunc.top()):
            operator = "RETURN"
            rightOperand = None
            leftOperand = None
            result = self.PilaO.pop()
            quad = Quadruple(
                operator, rightOperand, leftOperand, result[0])
            quad2 = Quadruple(
                operator, rightOperand, leftOperand, result[2])
            self.FilaQuads.append(quad)
            self.FilaQuadsMemoria.append(quad2)
        else:
            raise Exception("The return type does not match with the function {}".format(
                self.PilaFunc.top()))
        pass


# ========================== PROGRAMA MAIN ==========================


    def enterPrincipal(self, ctx: AangParser.PrincipalContext):
        self.FilaQuads[0].result = len(self.FilaQuads) + 1
        self.FilaQuadsMemoria[0].result = len(
            self.FilaQuadsMemoria) + 1
        self.varTable.print_table()
        pass

# ========================== LLAMAR FUNCION  ==========================

    def enterLlamar_fun(self, ctx: AangParser.Llamar_funContext):
        if self.functionDirectory.exist(str(ctx.ID())):
            self.PilaFuncParam.push(str(ctx.ID()))
            operator = "ERA"
            rightOperand = None
            leftOperand = None
            result = str(ctx.ID())
            quad = Quadruple(
                operator, rightOperand, leftOperand, result)
            quad2 = Quadruple(
                operator, rightOperand, leftOperand, result)
            self.FilaQuads.append(quad)
            self.FilaQuadsMemoria.append(quad2)
            self.ParameterCounter = self.functionDirectory.numOfParameters(
                str(ctx.ID()))

            self.TempParameters = self.functionDirectory.ParameterList(
                str(ctx.ID()))

        pass

    def exitLlamar_fun(self, ctx: AangParser.Llamar_funContext):
        if self.ParameterCounter > 0:
            raise Exception(
                "Less Arguments Passed in to {} Function".format(self.PilaFuncParam.top()))
        pass


# ========================== ARGUMENTOS ==========================


    def exitArgumentos(self, ctx: AangParser.ArgumentosContext):
        if ctx.exp() != None:

            if self.ParameterCounter < 0:
                raise Exception(
                    "More Arguments Passed in to {} Function".format(self.PilaFuncParam.top()))
            Result = self.PilaO.pop()
            if Result[1] != self.TempParameters.pop(0):
                raise Exception(
                    "Types not match between Function call and Function parameter")

        pass

    def enterAgregar_args(self, ctx: AangParser.Agregar_argsContext):
        self.ParameterCounter = self.ParameterCounter - 1
        Result = self.PilaO.top()
        operator = "PARAMETER"
        rightOperand = Result[2]
        leftOperand = None
        result = ("Par" +
                  str(self.functionDirectory.numOfParameters(
                      self.PilaFuncParam.top()) - (self.ParameterCounter)))
        quad = Quadruple(
            operator, Result[0], leftOperand, result)
        quad2 = Quadruple(
            operator, rightOperand, leftOperand, result)
        self.FilaQuads.append(quad)
        self.FilaQuadsMemoria.append(quad2)
        pass

    def exitAgregar_args(self, ctx: AangParser.Agregar_argsContext):
        if ctx.COMA() != None:
            if self.ParameterCounter < 0:
                raise Exception(
                    "More Arguments Passed in to {} Function".format(self.PilaFuncParam.top()))
            Result = self.PilaO.pop()
            if Result[1] != self.TempParameters.pop(0):
                raise Exception(
                    "Types not match between Function call and Function parameter")
        pass

    def enterFc(self, ctx: AangParser.FcContext):
        operator = "GOSUB"
        rightOperand = self.PilaFuncParam.top()
        leftOperand = None
        result = None
        quad = Quadruple(
            operator, rightOperand, leftOperand, result)
        quad2 = Quadruple(
            operator, rightOperand, leftOperand, result)
        self.FilaQuads.append(quad)
        self.FilaQuadsMemoria.append(quad2)
        if not self.functionDirectory.checkVoid(self.PilaFuncParam.top()):
            operator = "=*"
            rightOperand = self.PilaFuncParam.top()
            leftOperand = None
            Type = self.functionDirectory.getReturnType(
                self.PilaFuncParam.top())
            # self.PilaO.push((self.Avail.newElement(), Type, self.memoriaGlobal.getTemporales()))
            if Type == Types().INT:
                self.PilaO.push((self.Avail.newElement(), Type,
                                 self.memoriaTemporal.getEntera()))
            elif Type == Types().CHAR:
                self.PilaO.push((self.Avail.newElement(), Type,
                                 self.memoriaTemporal.getChar()))
            elif Type == Types().BOOL:
                self.PilaO.push((self.Avail.newElement(), Type,
                                 self.memoriaTemporal.getBooleanos()))
            result = self.PilaO.top()
            quad = Quadruple(
                operator, rightOperand, leftOperand, result[0])
            quad2 = Quadruple(
                operator, rightOperand, leftOperand, result[2])
            self.FilaQuads.append(quad)
            self.FilaQuadsMemoria.append(quad2)
        self.PilaFuncParam.pop()
        pass
