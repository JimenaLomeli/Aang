
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

# Comandos para correr la aplicación web
Es necesario hacer los siguientes comandos:
Primero clonar el proyecto
```bash
$ git clone https://github.com/JimenaLomeli/Aang.git
```
Despues instalar Antlr
```bash
-   $ export CLASSPATH=".:/usr/local/lib/antlr-4.7.1-complete.jar:$CLASSPATH
    
-   $ alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.7.1-complete.jar:$CLASSPATH" org.antlr.v4.Tool'
    
-   $ alias grun='java -Xmx500M -cp "/usr/local/lib/antlr-4.7.1-complete.jar:$CLASSPATH" org.antlr.v4.gui.TestRig'
    
-   $ antlr4 -Dlanguage=Python3 AangMain.g4
```
Tambien es necesario cambiar y asegurarse que el archivo AangSite/AangApp/views.py contenga las rutas correctas para su ordenador.**

Desde la ruta AangSite corra el siguiente comando:
    
```bash
$  python3 manage.py runserver
    
```
Por ultimo solo es se necesita abrir [http://127.0.0.1:8000/](http://127.0.0.1:8000/) en el navegador.
