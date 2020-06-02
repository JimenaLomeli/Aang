# Aang
Nuestra visión es hacer un lenguaje de programación que sea sencillo de usar para todas las personas que quieran aprender a programar. El objetivo es enseñar a los estudiantes los conceptos de programación de manera que puedan mover el personaje e ir creando una figura en el camino. 

# Equipo 

- Jorge Andrés Sabella

- Ana Jimena Lomeli Cantu
  
# Requerimientos
  
- Python 3.7.2
- Antlr4
 
# Como correr Aang
Para compilar la gramatica utilizar el siguiente comando dentro de la carpeta de Grammar:
```bash
  $ antlr4 -Dlanguage=Python3 Aang.g4
```
  
Para correr el programa Aang (Es necesario compilar primero la gramatica):
```bash
  $ python3 AangMain.py Grammar/Examples/<file-name>
```
