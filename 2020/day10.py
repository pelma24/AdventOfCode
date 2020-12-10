from HelperFunctions import inputsplit
from HelperFunctions import convertToInt

def do1(puzzleInput):
    differences = getDifferences(puzzleInput)

    return (differences.count(1)) * (differences.count(3))

def getDifferences(oldPuzzleInput):
    puzzleInput = oldPuzzleInput.copy()
    puzzleInput.insert(0,0)
    puzzleInput.insert(-1, max(puzzleInput) + 3)
    puzzleInput.sort()
    
    differences = [puzzleInput[x+1] - puzzleInput[x] for x in range(len(puzzleInput)-1)]
    
    return differences
    

def do2(puzzleInput):
    differences = getDifferences(puzzleInput)
    possibilities = 0
    sequences = []

    sequence = 0
    for difference in differences:
        if difference == 3:
            if sequence:
                sequences.append(sequence)
            sequence = 0
        else:
            sequence += 1

    dic = {1: lambda x : x, 2: lambda x : x * 2, 3: lambda x: x * 4, 4: lambda x : x * 7}
    possibilities = 1
    for sequence in sequences:
        possibilities = dic[sequence](possibilities)
    return possibilities

def do():
    with open ('Input/day10.txt') as f:
        strInput = f.read()

    splitInput = inputsplit(strInput, '\n')
    intInput = convertToInt(splitInput)

    print(do1(intInput))
    print(do2(intInput))
    
do()