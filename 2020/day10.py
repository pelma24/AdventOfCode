from HelperFunctions import inputsplit
from HelperFunctions import convertToInt

def do1(puzzleInput):
    prepareInput(puzzleInput)
    
    differences = getDifferences(puzzleInput)

    return (differences.count(1)) * (differences.count(3))

def do2(puzzleInput):
    prepareInput(puzzleInput)
    
    return getNumberOfPossibilities(puzzleInput)

def prepareInput(puzzleInput):
    puzzleInput.insert(0,0)
    puzzleInput.insert(-1, max(puzzleInput) + 3)
    puzzleInput.sort()

def getDifferences(puzzleInput):
        
    differences = [puzzleInput[x+1] - puzzleInput[x] for x in range(len(puzzleInput)-1)]
    
    return differences

def getNumberOfPossibilities(puzzleInput):
    
    puzzleInput.reverse()

    possibilites = {puzzleInput[0]:1}

    for value in puzzleInput[1:]:
        sum = 0
        for i in [1,2,3]:
            sum += possibilites.get(value + i, 0)
        possibilites[value] = sum
    
    return possibilites[puzzleInput[-1]] 

def do():
    with open ('Input/day10.txt') as f:
        strInput = f.read()

    splitInput = inputsplit(strInput, '\n')
    intInput = convertToInt(splitInput)

    print(do1(intInput))
    print(do2(intInput))
    
do()