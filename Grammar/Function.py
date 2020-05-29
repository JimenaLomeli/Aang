from antlr4 import *
from Variable import Variable
from memory import memory

# Store information about a function


class Function:
    def __init__(self, funcName):
        self.funcName = funcName
        self.startPosition = 0
        self.returnType = None
        self.memory = memory(4000, 5000, 6000, 0)
        self.parameters = []
        self.localVariables = 0
        self.temporalVariables = 0


class FunctionDir:
    def __init__(self):
        self.dictionary = {
        }

    def setStartPosition(self, funcName, startPosition):
        self.dictionary[funcName].startPosition = startPosition

    def getStartPosition(self, funcName):
        return self.dictionary[funcName].startPosition

    def setReturnType(self, funcName, returnType):
        self.dictionary[funcName].returnType = returnType

    def getReturnType(self, funcName):
        return self.dictionary[funcName].returnType

    def addParameter(self, funcName, parameter):
        self.dictionary[funcName].parameters.append(parameter)

    def ParameterList(self, funcName):
        return self.dictionary[funcName].parameters.copy()

    def numOfParameters(self, funcName):
        return len(self.dictionary[funcName].parameters)

    def checkVoid(self, funcName):
        return self.dictionary[funcName].returnType == "void"

    def setLocalVariables(self, funcName, localVariables):
        self.dictionary[funcName].localVariables = localVariables

    def setTemporalVariables(self, funcName, temporalVariables):
        self.dictionary[funcName].temporalVariables = temporalVariables

    def get_function(self, funcName):
        if funcName not in self.dictionary:
            raise Exception(
                "{} does not exist in the directory".format(funcName))
        else:
            self.dictionary[funcName]

    def exist(self, funcName):
        if funcName not in self.dictionary:
            raise Exception(
                "{} does not exist in the directory".format(funcName))
        return True

    def getNextInt(self, funcName):
        return self.dictionary[funcName].memory.getEntera()

    def getNextBool(self, funcName):
        return self.dictionary[funcName].memory.getBooleanos()

    def getNextChar(self, funcName):
        return self.dictionary[funcName].memory.getChar()

    def getNextTemp(self, funcName):
        return self.dictionary[funcName].memory.getTemporales()

    def add_function(self, funcName):
        if funcName in self.dictionary:
            raise Exception("The function already exists.")
        else:
            self.dictionary[funcName] = Function(
                funcName)

    def print_table(self):
        for func in self.dictionary:
            print(str(func) + ': ' + str(self.dictionary[func].startPosition) + ", " + str(self.dictionary[func].returnType) + ", " + str(len(self.dictionary[func].parameters)) + ", " + str(
                self.dictionary[func].localVariables) + ", " + str(self.dictionary[func].temporalVariables))
            print(self.dictionary[func].parameters)
