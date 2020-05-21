from antlr4 import *

# Store the variable table structure


class Variable:
    def __init__(self, varName, dataType, scope, memoryDir):
        self.varName = varName
        self.dataType = dataType
        self.scope = scope
        self.memoryDir = memoryDir


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

    def get_local_variable(self, varName):
        return varName in self.vars.keys()

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
                  str(self.vars[variable].scope) + ', ' + str(self.vars[variable].memoryDir))
