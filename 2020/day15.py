from HelperFunctions import inputsplit

def do1(puzzleInput):
    return 'done'

def do2(puzzleInput):
    return 'done'

def do():
    with open ('Input/day15.txt') as f:
        strInput = f.read()

    splitInput = inputsplit(strInput, '\n')

    print(do1(splitInput))
    print(do2(splitInput))
    
do()