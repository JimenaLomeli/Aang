from antlr4 import *

# Store the variable table structure


class arrayNode:
    def __init__(self):
        self.inferior = 0
        self.superior = 0
        self.k = 0


class Variable:
    def __init__(self, varName, dataType, scope, memoryDir):
        self.varName = varName
        self.dataType = dataType
        self.scope = scope
        self.memoryDir = memoryDir
        self.isArray = False
        self.node = arrayNode()


class VariableTable:
    def __init__(self, vars):
        self.vars = {}
        self.keywords = ["int", "void", "char", "if", "else", "while",
                         "print", "return", "id", "programa", "empezar", "fin", "bool"]

    def get_variable(self, varName):
        if varName in self.vars.keys():
            return self.vars[varName]
        else:
            raise Exception(
                "{} does not exist in the directory".format(varName))

    def exist(self, varName):
        if varName not in self.vars.keys():
            raise Exception(
                "{} does not exist in the directory".format(varName))

    def setLSup(self, varName, limite):
        self.vars[varName].node.superior = limite

    def getLSup(self, varName):
        return self.vars[varName].node.superior

    def get_local_variable(self, varName):
        return varName in self.vars.keys()

    def setIsArray(self, varName):
        self.vars[varName].isArray = True

    def add_variable(self, varName, dataType, scope, memoryDir):
        if varName in self.vars:
            raise Exception(
                "{} already exists in the directory".format(varName))

        elif varName in self.keywords:
            raise Exception("{} is a reserved word".format(varName))

        else:
            var = Variable(varName, dataType, scope, memoryDir)
            self.vars[varName] = var

    def print_table(self):
        for variable in self.vars:
            print(str(variable) + ': ' + str(self.vars[variable].dataType) + ', ' +
                  str(self.vars[variable].scope) + ', ' + str(self.vars[variable].memoryDir) + ', ' + str(self.vars[variable].isArray) + ', ' + str(self.vars[variable].node.inferior) + ', ' + str(self.vars[variable].node.superior) + ', ' + str(self.vars[variable].node.k))
