import sys
import pickle


Memoria = {
    "Global": {
        "Entero": {},
        "Char": {},
        "Bool": {}
    },
    "Local": {
        "Entero": {},
        "Char": {},
        "Bool": {}
    },
    "Constante": {
        "Entero": {},
        "Char": {},
        "Bool": {}
    },
    "Temporal": {
        "All": {}
    }
}


def main(argv):

    # ======= INICIAR MEMORIA ========
    LlenarMemoria(Memoria)

    # ======== IMPORTAR OBJETOS DE COMPILACION =======
    pickle_in = open("Quadruplos.pickle", "rb")
    FilaQuadsMemoria = pickle.load(pickle_in)
    functionDirectory = pickle.load(pickle_in)
    constTable = pickle.load(pickle_in)
    # for index, quad in enumerate(FilaQuadsMemoria, 1):
    #    print(index, quad)
    # functionDirectory.print_table()
    # constTable.print_table()

    # ======= POBLAR MEMORIA CONSTANTE ======
    for constantKey in constTable.constants.keys():
        memoryDir = constTable.constants[constantKey].memoryDir
        dataType = constTable.constants[constantKey].dataType
        if dataType == 'int':
            getMemorySection(memoryDir)[getStartingPoint(
                memoryDir)] = int(constantKey)
        elif dataType == 'char':
            getMemorySection(memoryDir)[
                getStartingPoint(memoryDir)] = constantKey
        elif dataType == 'bool':
            if constantKey == 'True':
                getMemorySection(memoryDir)[getStartingPoint(
                    memoryDir)] = True
            else:
                getMemorySection(memoryDir)[getStartingPoint(
                    memoryDir)] = False

    # ====== INICIAR EJECUCION ======
    i = 0

    while i < len(FilaQuadsMemoria):
        if FilaQuadsMemoria[i].operator == 'Goto':
            i = FilaQuadsMemoria[i].result - 1
            i = i - 1

        elif FilaQuadsMemoria[i].operator == '+':
            left = FilaQuadsMemoria[i].leftOp
            right = FilaQuadsMemoria[i].rightOp
            res = FilaQuadsMemoria[i].result
            getMemorySection(res)[getStartingPoint(res)] = int(getMemorySection(left)[getStartingPoint(left)] +
                                                               getMemorySection(right)[getStartingPoint(right)])

        elif FilaQuadsMemoria[i].operator == '-':
            left = FilaQuadsMemoria[i].leftOp
            right = FilaQuadsMemoria[i].rightOp
            res = FilaQuadsMemoria[i].result
            getMemorySection(res)[getStartingPoint(res)] = int(getMemorySection(left)[getStartingPoint(left)] -
                                                               getMemorySection(right)[getStartingPoint(right)])

        elif FilaQuadsMemoria[i].operator == '/':
            left = FilaQuadsMemoria[i].leftOp
            right = FilaQuadsMemoria[i].rightOp
            res = FilaQuadsMemoria[i].result
            getMemorySection(res)[getStartingPoint(res)] = int(getMemorySection(left)[getStartingPoint(left)] /
                                                               getMemorySection(right)[getStartingPoint(right)])

        elif FilaQuadsMemoria[i].operator == '*':
            left = FilaQuadsMemoria[i].leftOp
            right = FilaQuadsMemoria[i].rightOp
            res = FilaQuadsMemoria[i].result
            getMemorySection(res)[getStartingPoint(res)] = int(getMemorySection(left)[getStartingPoint(left)] *
                                                               getMemorySection(right)[getStartingPoint(right)])

        elif FilaQuadsMemoria[i].operator == '=':
            left = FilaQuadsMemoria[i].leftOp
            res = FilaQuadsMemoria[i].result
            getMemorySection(res)[getStartingPoint(res)] = getMemorySection(left)[
                getStartingPoint(left)]

        elif FilaQuadsMemoria[i].operator == '==':
            left = FilaQuadsMemoria[i].leftOp
            right = FilaQuadsMemoria[i].rightOp
            res = FilaQuadsMemoria[i].result
            if getMemorySection(left)[getStartingPoint(left)] == getMemorySection(right)[getStartingPoint(right)]:
                getMemorySection(res)[getStartingPoint(res)] = True
            else:
                getMemorySection(res)[getStartingPoint(res)] = False

        elif FilaQuadsMemoria[i].operator == '!=':
            left = FilaQuadsMemoria[i].leftOp
            right = FilaQuadsMemoria[i].rightOp
            res = FilaQuadsMemoria[i].result
            if getMemorySection(left)[getStartingPoint(left)] != getMemorySection(right)[getStartingPoint(right)]:
                getMemorySection(res)[getStartingPoint(res)] = True
            else:
                getMemorySection(res)[getStartingPoint(res)] = False

        elif FilaQuadsMemoria[i].operator == '<':
            left = FilaQuadsMemoria[i].leftOp
            right = FilaQuadsMemoria[i].rightOp
            res = FilaQuadsMemoria[i].result
            if getMemorySection(left)[getStartingPoint(left)] < getMemorySection(right)[getStartingPoint(right)]:
                getMemorySection(res)[getStartingPoint(res)] = True
            else:
                getMemorySection(res)[getStartingPoint(res)] = False

        elif FilaQuadsMemoria[i].operator == '>':
            left = FilaQuadsMemoria[i].leftOp
            right = FilaQuadsMemoria[i].rightOp
            res = FilaQuadsMemoria[i].result
            if getMemorySection(left)[getStartingPoint(left)] > getMemorySection(right)[getStartingPoint(right)]:
                getMemorySection(res)[getStartingPoint(res)] = True
            else:
                getMemorySection(res)[getStartingPoint(res)] = False

        elif FilaQuadsMemoria[i].operator == '&&':
            left = FilaQuadsMemoria[i].leftOp
            right = FilaQuadsMemoria[i].rightOp
            res = FilaQuadsMemoria[i].result
            if getMemorySection(left)[getStartingPoint(left)] and getMemorySection(right)[getStartingPoint(right)]:
                getMemorySection(res)[getStartingPoint(res)] = True
            else:
                getMemorySection(res)[getStartingPoint(res)] = False

        elif FilaQuadsMemoria[i].operator == '||':
            left = FilaQuadsMemoria[i].leftOp
            right = FilaQuadsMemoria[i].rightOp
            res = FilaQuadsMemoria[i].result
            if getMemorySection(left)[getStartingPoint(left)] or getMemorySection(right)[getStartingPoint(right)]:
                getMemorySection(res)[getStartingPoint(res)] = True
            else:
                getMemorySection(res)[getStartingPoint(res)] = False

        elif FilaQuadsMemoria[i].operator == '>':
            left = FilaQuadsMemoria[i].leftOp
            right = FilaQuadsMemoria[i].rightOp
            res = FilaQuadsMemoria[i].result
            if getMemorySection(left)[getStartingPoint(left)] > getMemorySection(right)[getStartingPoint(right)]:
                getMemorySection(res)[getStartingPoint(res)] = True
            else:
                getMemorySection(res)[getStartingPoint(res)] = False

        elif FilaQuadsMemoria[i].operator == 'print':
            left = FilaQuadsMemoria[i].leftOp
            print(getMemorySection(left)[getStartingPoint(left)])

        i = i + 1


def LlenarMemoria(Memoria):
    IniciarMemoria(Memoria["Global"]["Entero"])
    IniciarMemoria(Memoria["Global"]["Char"])
    IniciarMemoria(Memoria["Global"]["Bool"])
    IniciarMemoria(Memoria["Local"]["Entero"])
    IniciarMemoria(Memoria["Local"]["Char"])
    IniciarMemoria(Memoria["Local"]["Bool"])
    IniciarMemoria(Memoria["Constante"]["Entero"])
    IniciarMemoria(Memoria["Constante"]["Char"])
    IniciarMemoria(Memoria["Constante"]["Bool"])
    IniciarMemoria(Memoria["Temporal"])


def IniciarMemoria(Memoria):
    for key in range(0, 10):
        Memoria[key] = None


def getMemoryScope(direccion):
    if direccion >= 1000 and direccion <= 3999:
        return "Global"
    elif direccion >= 4000 and direccion <= 6999:
        return "Local"
    elif direccion >= 7000 and direccion <= 9999:
        return "Constante"
    elif direccion >= 10000 and direccion <= 12999:
        return "Temporal"
    else:
        raise Exception("Out of Range")


def getMemoryType(direccion):
    if direccion >= 1000 and direccion <= 1999 or direccion >= 4000 and direccion <= 4999 or direccion >= 7000 and direccion <= 7999:
        return "Entero"
    elif direccion >= 2000 and direccion <= 2999 or direccion >= 5000 and direccion <= 5999 or direccion >= 8000 and direccion <= 8999:
        return "Char"
    elif direccion >= 3000 and direccion <= 3999 or direccion >= 6000 and direccion <= 6999 or direccion >= 9000 and direccion <= 9999:
        return "Bool"
    elif direccion >= 10000 and direccion <= 12999:
        return "All"
    else:
        raise Exception("Out of Range")


def getMemorySection(direccion):
    return Memoria[getMemoryScope(direccion)][getMemoryType(direccion)]


def getStartingPoint(direccion):
    if direccion >= 1000 and direccion <= 1999:
        return direccion - 1000
    elif direccion >= 2000 and direccion <= 2999:
        return direccion - 2000
    elif direccion >= 3000 and direccion <= 3999:
        return direccion - 3000
    elif direccion >= 4000 and direccion <= 4999:
        return direccion - 4000
    elif direccion >= 5000 and direccion <= 5999:
        return direccion - 5000
    elif direccion >= 6000 and direccion <= 6999:
        return direccion - 6000
    elif direccion >= 7000 and direccion <= 7999:
        return direccion - 7000
    elif direccion >= 8000 and direccion <= 8999:
        return direccion - 8000
    elif direccion >= 9000 and direccion <= 9999:
        return direccion - 9000
    elif direccion >= 10000 and direccion <= 12999:
        return direccion - 10000
    else:
        raise Exception("Out of Range")


if __name__ == '__main__':
    main(sys.argv)
