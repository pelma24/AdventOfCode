from HelperFunctions import inputsplit
from HelperFunctions import convertToInt
from itertools import islice

def do1(puzzleInput, preambelLength):
    
    for position in range(preambelLength, len(puzzleInput) - preambelLength):
        
        splitArray = puzzleInput[(position - preambelLength):position]

        possibleSums = [(x,y) for x in splitArray for y in splitArray if (x + y) == puzzleInput[position]]

        if len(possibleSums) == 0:
            return puzzleInput[position]

    return 'nothing found'

def do2(puzzleInput, invalidNumber):
    
    sliceSize = 2

    while True:
        for i in range(len(puzzleInput)):
            arraySlice = puzzleInput[slice(i, i + sliceSize, 1)]
            
            if (sum(arraySlice) == invalidNumber):
                return min(arraySlice) + max(arraySlice)
    
        sliceSize += 1
        
    return 'nothing found'

def do():
    with open ('Input/day9.txt') as f:
        strInput = f.read()

    splitInput = inputsplit(strInput, '\n')
    intInput = convertToInt(splitInput)
    preambelLength = 25

    result1 = do1(intInput, preambelLength)
    print(result1)
    print(do2(intInput, result1))
    
do()