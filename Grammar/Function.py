from antlr4 import *
from Variable import Variable

# Store information about a function
class Function:
    def __init__(self, funcName, parameters, returnType):
        self.funcName = funcName
        self.returnType = returnType
        self.parameters = []
        self.variables = parameters
    
class FunctionDir:
    def __init__(self):
        self.dictionary = {
        }

    def get_function(self, funcName):
        if funcName not in self.dictionary:
            raise Exception("{} does not exist in the directory".format(funcName))
        else:
            self.dictionary[funcName]

    def add_function(self, funcName, parameters, returnType):
        if funcName in self.functions:
            raise Exception("The function already exists.")
        else:
            self.functions[funcName] = Function(
                funcName, returnType, {})
            self.functions[funcName].parameters = parameters
            for parameter in parameters:
                self.add_variable(
                    parameter.name, parameter.type, parameter.scope, value)

