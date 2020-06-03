from antlr4 import *


class MatrizColores:
    def __init__(self):
        self.Matriz = []
        self.context = {}
        self.x = 4
        self.y = 4
        self.color = 'black'
        self.direction = 0
        for i in range(0, 9):
            self.Matriz.append([])
        for i in range(0, 9):
            for j in range(0, 9):
                self.Matriz[j].append([])
        for i in range(1, 82):
            self.context['color' + str(i)] = 'white'

    def Paint(self):
        if len(self.Matriz[self.x][self.y]) == 0:
            self.Matriz[self.x][self.y].append(self.color)
        else:
            self.Matriz[self.x][self.y][0] = self.color

    def Mover(self, num):
        if self.direction == 3:
            if self.y - num <= 0:
                self.y = 0
            else:
                self.y = self.y - num
        elif self.direction == 2:
            if num + self.y >= 8:
                self.y = 8
            else:
                self.y = self.y + num
        elif self.direction == 1:
            if num + self.x >= 8:
                self.x = 8
            else:
                self.x = self.x + num
        elif self.direction == 0:
            if self.x - num <= 0:
                self.x = 0
            else:
                self.x = self.x - num

    def Cambiar(self, direction):
        if direction == 'Arriba':
            self.direction = 0
        if direction == 'Abajo':
            self.direction = 1
        if direction == 'Derecha':
            self.direction = 2
        if direction == 'Izquierda':
            self.direction = 3

    def printMat(self):
        for x in range(0, 9):
            print(self.Matriz[x])

    def translate(self):
        j = 1
        for x in range(0, 9):
            for y in range(0, 9):
                if len(self.Matriz[x][y]) > 0:
                    self.context["color" + str(j)] = self.Matriz[x][y][0]
                j = j + 1

    def Color(self, color):
        self.color = color
