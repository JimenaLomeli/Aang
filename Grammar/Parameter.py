from antlr4 import *

# Store the variable table structure


class ParameterTable:
    def __init__(self):
        self.parameters = []

    def get_nextParameter(self, constantValue):
        return self.parameters.pop(0)

    def add_parameter(self, type):
        self.parameters.append(type)
