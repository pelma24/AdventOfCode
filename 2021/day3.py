from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt
from collections import defaultdict
from copy import deepcopy
import operator

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
    oxygen = filterByFrequency(splitInput, operator.gt)

    scrubber = filterByFrequency(splitInput, operator.le)

    return scrubber * oxygen

def getFrequency(splitInput):
    frequency = defaultdict(lambda: {0: 0, 1: 0})
    
    for line in splitInput:
        for position,bit in enumerate(line):
            frequency[position][int(bit)] += 1
    
    return frequency

def filterByFrequency(currentInput, compareOperator=operator.gt):
    maxBit = len(currentInput[0])

    for i in range(maxBit):
        frequency = getFrequency(currentInput)
        if compareOperator(frequency[i][0], frequency[i][1]):
            currentInput = [x for x in currentInput if x[i] == '0']
        else:
            currentInput = [x for x in currentInput if x[i] == '1']    
        if len(currentInput) == 1:
            break
    
    return int(currentInput[0],2)

def do():
    strInput = readInputFile(3)
    
    splitInput = strInput.split('\n')

    print(do1(splitInput))
    print(do2(splitInput))

    print('done')


do()