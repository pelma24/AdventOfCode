from HelperFunctions import inputsplit
from HelperFunctions import convertToInt

def do1(puzzleInput):
    differences = getDifferences(puzzleInput)

    return (differences.count(1)) * (differences.count(3))

def getDifferences(puzzleInput):
    currentJolts = 0
    maxAdapter = max(puzzleInput)
    differences = []
    
    while currentJolts != maxAdapter:
        for i in range(1, 4):
            if (currentJolts + i) in puzzleInput:
                currentJolts = currentJolts + i
                differences.append(i)
                break
    differences.append(3)
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

    possibilities = 1
    for sequence in sequences:
        if sequence == 2:
            possibilities *= 2
        if sequence == 3:
            possibilities *= 4
        if sequence == 4:
            possibilities *= 7

    return possibilities

def nextAvailableAdapters(adapters, jolts):
    possibleAdapters = []
    for i in range(1,4):
        if (jolts + i) in adapters:
            possibleAdapters.append(jolts + i)
    return possibleAdapters

def do():
    with open ('Input/day10.txt') as f:
        strInput = f.read()

    splitInput = inputsplit(strInput, '\n')
    intInput = convertToInt(splitInput)

    print(do1(intInput))
    print(do2(intInput))
    
do()