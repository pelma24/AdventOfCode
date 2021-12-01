from HelperFunctions import readInputFile
from HelperFunctions import convertToInt

def do1(splitInput):
    
    bigger = [(x,y) for (x,y) in zip(splitInput, splitInput[1:]) if y > x]

    return len(bigger)

def do2(splitInput):
    window1 = [a + b + c for (a,b,c) in zip(splitInput, splitInput[1:], splitInput[2:])]
    window2 = [b + c + d for (b,c,d) in zip(splitInput[1:], splitInput[2:], splitInput[3:])]

    bigger = [(x,y) for (x,y) in zip(window1, window2) if y > x]

    return len(bigger)

def do():
    strInput = readInputFile(1)

    splitInput = strInput.split('\n')
    intInput = convertToInt(splitInput)
    print(do1(intInput))
    print(do2(intInput))

do()

