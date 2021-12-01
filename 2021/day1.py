from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt

def do1(splitInput):
    
    bigger = [(x,y) for (x,y) in zip(splitInput, splitInput[1:]) if y > x]

    return len(bigger)

def do2(splitInput):
    
    window = [a + b + c for (a,b,c) in zip(splitInput, splitInput[1:], splitInput[2:])]
    
    return do1(window)

def do():
    strInput = readInputFile(1)

    splitInput = strInput.split('\n')
    intInput = convertToInt(splitInput)
    print(do1(intInput))
    print(do2(intInput))

do()

