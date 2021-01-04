from HelperFunctions import inputsplit
import re

def do1(puzzleInput):

    memory = fillMemory(puzzleInput, updateValue)
    
    return sum([x for x in memory.values()])

def do2(puzzleInput):
    
    memory = fillMemory(puzzleInput, updateMemoryValue)
    
    return sum([x for x in memory.values()])

def fillMemory(puzzleInput, updateFunction):
    memory = {}

    bitmask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    for line in puzzleInput:
        match = re.match('mask = (.+)', line)
        if match:
            bitmask = match.groups()[0]
        else:
            match = re.match('mem\[([0-9]+)\] = ([0-9]+)', line)
            if match:
                position = int(match.groups()[0])
                value = int(match.groups()[1])
                updateFunction(bitmask, position, value, memory)
            else:
                print('could not match')
    return memory

def updateMemoryValue(bitmask, position, value, memory):
    memoryPositions = []
    
    positionBinary = format(position, '036b')
    memoryPositions.append(positionBinary)

    for bit in range(len(bitmask)):
        if bitmask[bit] == '1':
            for position in range(len(memoryPositions)):
                memoryPositions[position] = memoryPositions[position][0:bit] + '1' + memoryPositions[position][bit+1:]
        elif bitmask[bit] == 'X':
            for position in range(len(memoryPositions)):
                memoryPositions[position] = memoryPositions[position][0:bit] + '0' + memoryPositions[position][bit+1:]
                memoryPosition2 = memoryPositions[position][0:bit] + '1' + memoryPositions[position][bit+1:]
                memoryPositions.append(memoryPosition2)

    for memoryPosition in memoryPositions:
        intMemoryPosition = int(memoryPosition, 2)
        memory[intMemoryPosition] = value

def updateValue(bitmask, position, value, memory):
    valueBinary = format(value, '036b')

    for bit in range(len(bitmask)):
        if bitmask[bit] == '1':
            valueBinary = valueBinary[0:bit] + '1' + valueBinary[bit+1:]
        elif bitmask[bit] == '0':
            valueBinary = valueBinary[0:bit] + '0' + valueBinary[bit+1:]
    
    intValue = int(valueBinary, 2)

    memory[position] = intValue        

def do():
    with open ('Input/day14.txt') as f:
        strInput = f.read()

    splitInput = inputsplit(strInput, '\n')

    print(do1(splitInput))
    print(do2(splitInput))
    
do()