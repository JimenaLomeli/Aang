class memory:

    def __init__(self, enteras, booleanos, chars, temporales):
        self.enteras = enteras
        self.chars = chars
        self.booleanos = booleanos
        self.temporales = temporales

        self.i = 0
        self.b = 0
        self.c = 0
        self.t = 0

    def getEntera(self):
        self.i = self.i+1
        return self.enteras + self.i - 1

    def getBooleanos(self):
        self.b = self.b + 1
        return self.booleanos + self.b - 1

    def getChar(self):
        self.c = self.c + 1
        return self.chars + self.c - 1

    def getTemporales(self):
        self.t = self.t + 1
        return self.temporales + self.t - 1

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)
