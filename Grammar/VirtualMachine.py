import sys
import pickle


def main(argv):
    # iniciar memoria
    MemoriaConstante = {}
    for key in range(0, 1000):
        MemoriaConstante[key] = None
    MemoriaTemporal = {}
    for key in range(0, 1000):
        MemoriaTemporal[key] = None

    memoryStartingPoint = {'temp': 4000, 'constInt': 9000,
                           'constChar': 10000, 'constBool': 11000}

    TEMPINT = 0
    TEMPCHAR = 400
    TEMPBOOL = 700

    # importar objetos de compilacion
    print("Pongame 100 Eldita mi amor")
    pickle_in = open("Quadruplos.pickle", "rb")
    FilaQuadsMemoria = pickle.load(pickle_in)
    functionDirectory = pickle.load(pickle_in)
    constTable = pickle.load(pickle_in)
    for index, quad in enumerate(FilaQuadsMemoria, 1):
        print(index, quad)
    functionDirectory.print_table()
    constTable.print_table()

    # poblar memoria constante
    for constantKey in constTable.constants.keys():
        memoryDir = constTable.constants[constantKey].memoryDir
        dataType = constTable.constants[constantKey].dataType
        if dataType == 'int':
            MemoriaConstante[memoryDir -
                             memoryStartingPoint['constInt']] = int(constantKey)

    # Iniciar ejecucion
    i = 0

    while i < len(FilaQuadsMemoria):
        if FilaQuadsMemoria[i].operator == 'Goto':
            i = FilaQuadsMemoria[i].result - 1
            i = i - 1

        elif FilaQuadsMemoria[i].operator == '+':
            leftOperandMemory = FilaQuadsMemoria[i].leftOp - \
                memoryStartingPoint['constInt']
            rightOperandMemory = FilaQuadsMemoria[i].rightOp - \
                memoryStartingPoint['constInt']
            resultMemory = FilaQuadsMemoria[i].result - \
                memoryStartingPoint['temp']
            MemoriaTemporal[resultMemory] = MemoriaConstante[leftOperandMemory] + \
                MemoriaConstante[rightOperandMemory]
            pass

        elif FilaQuadsMemoria[i].operator == '-':
            pass

        elif FilaQuadsMemoria[i].operator == '/':
            pass

        elif FilaQuadsMemoria[i].operator == '*':
            pass

        elif FilaQuadsMemoria[i].operator == 'print':
            leftOperandMemory = FilaQuadsMemoria[i].leftOp - \
                memoryStartingPoint['temp']
            print(MemoriaTemporal[leftOperandMemory])
            pass

        i = i + 1


if __name__ == '__main__':
    main(sys.argv)
