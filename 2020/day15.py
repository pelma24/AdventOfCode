from HelperFunctions import inputsplit
from HelperFunctions import convertToInt

def do1(puzzleInput):
    numbers, lastNumber = prepareInput(puzzleInput)
        
    resultNumber = play(numbers, lastNumber, 2020)
    
    return resultNumber

def do2(puzzleInput):
    numbers, lastNumber = prepareInput(puzzleInput)
        
    resultNumber = play(numbers, lastNumber, 30000000)
    
    return resultNumber

def prepareInput(puzzleInput):
    intNumbers = convertToInt(puzzleInput)

    numbers = {}

    for i, number in enumerate(intNumbers):
        numbers[number] = [1, [i + 1]]
        lastNumber = number
    
    return [numbers, lastNumber]

def play(numbers, lastNumber, maxIterations):
    i = 1 + numbers[lastNumber][1][-1]
    while (i < maxIterations + 1):
        oldLastNumber = lastNumber
        
        if numbers[oldLastNumber][0] == 1:
            lastNumber = 0
        else:
            lastNumber = numbers[oldLastNumber][1][-1] - numbers[oldLastNumber][1][-2]
        
        if lastNumber not in numbers.keys():
            numbers[lastNumber] = [0, []]

        numbers[lastNumber][0] += 1
        numbers[lastNumber][1].append(i)
        i += 1
    return lastNumber    

def do():
    with open ('Input/day15.txt') as f:
        strInput = f.read()

    splitInput = inputsplit(strInput, ',')

    print(do1(splitInput))
    print(do2(splitInput))
    
do()