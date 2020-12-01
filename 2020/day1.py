from HelperFunctions import inputsplit
from HelperFunctions import convertToInt

def do1(intInput):
    
    multiply = set([x*y for x in intInput for y in intInput if (x + y) == 2020])

    return multiply

def do2(intInput):
    
    multiply = set([x*y*z for x in intInput for y in intInput for z in intInput if (x + y + z) == 2020])
    return multiply


def do():
    with open ('Input/day1.txt') as f:
        strInput = f.read()

    splitInput = inputsplit(strInput)
    intInput = convertToInt(splitInput)

    print(do1(intInput))
    print(do2(intInput))

do()