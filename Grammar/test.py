import sys
from antlr4 import *

def main(argv):
    if len(sys.argv) < 2:
        print("You must provide the file you want to compile")
        exit()
    try:
        aangFile = FileStream(sys.argv[1])
        print(aangFile)

    except Exception:
        print(f"Could not read {sys.argv[1]}")
        exit()
        
if __name__ == '__main__':
    main(sys.argv)