from antlr4 import *

# Store the variable table structure


class Constant:
    def __init__(self, dataType, memoryDir):
        self.dataType = dataType
        self.memoryDir = memoryDir


class ConstantTable:
    def __init__(self):
        self.constants = {}

    def get_constant(self, constantValue):
        return constantValue in self.constants

    def add_constant(self, constantValue, dataType, memoryDir):
        if constantValue not in self.constants:
            const = Constant(dataType, memoryDir)
            self.constants[constantValue] = const

    def print_table(self):
        print(self.constants)
