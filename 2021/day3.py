from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt
from copy import deepcopy

def do1(splitInput):
    frequency = getFrequency(splitInput)
    
    gamma = ''
    epsilon = ''
    for position in sorted(frequency.keys()):
        if frequency[position][0] > frequency[position][1]:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'

    return int(gamma, 2) * int(epsilon, 2)

def do2(splitInput):
    maxBit = len(splitInput[0])

    # oxygen
    currentInput = deepcopy(splitInput)
    for i in range(maxBit):
        frequency = getFrequency(currentInput)
        if frequency[i][0] > frequency[i][1]:
            currentInput = [x for x in currentInput if x[i] == '0']
        else:
            currentInput = [x for x in currentInput if x[i] == '1']    
        if len(currentInput) == 1:
            break
    oxygen = int(currentInput[0],2)
    
    # CO2 scrubber
    currentInput = deepcopy(splitInput)
    for i in range(maxBit):
        frequency = getFrequency(currentInput)
        if frequency[i][1] < frequency[i][0]:
            currentInput = [x for x in currentInput if x[i] == '1']
        else:
            currentInput = [x for x in currentInput if x[i] == '0']    
        if len(currentInput) == 1:
            break
    scrubber = int(currentInput[0],2)
    
    return scrubber * oxygen

def getFrequency(splitInput):
    frequency = {}
    
    for line in splitInput:
        for position,bit in enumerate(line):
            if position not in frequency.keys():
                frequency[position] = {0: 0, 1: 0}
            frequency[position][int(bit)] += 1
    
    return frequency


def do():
    strInput = readInputFile(3)
    #strInput = readExampleInput(3)

    splitInput = strInput.split('\n')

    print(do1(splitInput))
    print(do2(splitInput))

    print('done')


do()