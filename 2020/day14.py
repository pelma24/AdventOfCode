from HelperFunctions import inputsplit
import re

def do1(puzzleInput):
    
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
                updateValue(bitmask, position, value, memory)
            else:
                print('could not match')
    
    return sum([memory[x] for x in memory.keys() if memory[x] != 0])

def do2(puzzleInput):
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
                updateValueWithMemory(bitmask, position, value, memory)
            else:
                print('could not match')
    
    return sum([memory[x] for x in memory.keys() if memory[x] != 0])

def updateValueWithMemory(bitmask, position, value, memory):
    memoryPositions = []
    
    positionBinary = format(position, '036b')
    memoryPositions.append(positionBinary)

    for i in range(len(bitmask) - 1, -1, -1):
        if bitmask[i] == '1':
            for j in range(len(memoryPositions)):
                memoryPositions[j] = memoryPositions[j][0:i] + '1' + memoryPositions[j][i+1:]
        elif bitmask[i] == 'X':
            for j in range(len(memoryPositions)):
                memoryPositions[j] = memoryPositions[j][0:i] + '0' + memoryPositions[j][i+1:]
                memoryPosition2 = memoryPositions[j][0:i] + '1' + memoryPositions[j][i+1:]
                memoryPositions.append(memoryPosition2)

    for memoryPosition in memoryPositions:
        newMemoryPosition = int(memoryPosition, 2)
        memory[newMemoryPosition] = value

def updateValue(bitmask, position, value, memory):
    valueBinary = format(value, '036b')

    for i in range(len(bitmask) - 1, -1, -1):
        if bitmask[i] == '1':
            valueBinary = valueBinary[0:i] + '1' + valueBinary[i+1:]
        elif bitmask[i] == '0':
            valueBinary = valueBinary[0:i] + '0' + valueBinary[i+1:]
    
    newValue = int(valueBinary, 2)

    memory[position] = newValue        

def do():
    with open ('Input/day14.txt') as f:
        strInput = f.read()

    splitInput = inputsplit(strInput, '\n')

    print(do1(splitInput))
    print(do2(splitInput))
    
do()