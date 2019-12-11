from enum import IntEnum

input = """3,8,1005,8,311,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,102,1,8,28,1,1104,0,10,1006,0,71,2,1002,5,10,2,1008,5,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,102,1,8,66,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,102,1,8,87,1006,0,97,2,1002,6,10,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,102,1,8,116,1006,0,95,1,1009,10,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,102,1,8,145,1,1002,19,10,2,1109,7,10,1006,0,18,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,1001,8,0,179,3,8,102,-1,8,10,101,1,10,10,4,10,108,0,8,10,4,10,102,1,8,200,1,1105,14,10,1,1109,14,10,2,1109,11,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,102,1,8,235,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1002,8,1,257,2,101,9,10,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,101,0,8,282,2,1109,19,10,1,105,0,10,101,1,9,9,1007,9,1033,10,1005,10,15,99,109,633,104,0,104,1,21102,937268368140,1,1,21102,328,1,0,1106,0,432,21102,1,932700599052,1,21101,0,339,0,1105,1,432,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21101,0,209421601831,1,21102,1,386,0,1106,0,432,21102,235173604443,1,1,21102,1,397,0,1106,0,432,3,10,104,0,104,0,3,10,104,0,104,0,21101,825439855372,0,1,21102,1,420,0,1106,0,432,21101,0,988220907880,1,21102,431,1,0,1106,0,432,99,109,2,22101,0,-1,1,21101,40,0,2,21102,1,463,3,21102,453,1,0,1106,0,496,109,-2,2105,1,0,0,1,0,0,1,109,2,3,10,204,-1,1001,458,459,474,4,0,1001,458,1,458,108,4,458,10,1006,10,490,1102,1,0,458,109,-2,2106,0,0,0,109,4,2102,1,-1,495,1207,-3,0,10,1006,10,513,21102,0,1,-3,22102,1,-3,1,21202,-2,1,2,21102,1,1,3,21101,532,0,0,1105,1,537,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,560,2207,-4,-2,10,1006,10,560,21201,-4,0,-4,1106,0,628,22102,1,-4,1,21201,-3,-1,2,21202,-2,2,3,21102,1,579,0,1106,0,537,21202,1,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,598,21101,0,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,620,21201,-1,0,1,21102,1,620,0,105,1,495,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2105,1,0"""

class Direction(IntEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

def do(input, intInput, position, relativeBase):
    output = []   

    while True:
        modes = actionSplit(intInput[position])
        action = modes['action']
        if action == 99:
            print('finished')
            return [output, intInput, position, relativeBase, True]
        
        arg1 = getArg(intInput, modes, position, 1, relativeBase)

        if action == 3:
            inputValue = input.pop(0)
            intInput[arg1] = inputValue
            position += 2
            continue
            
        if action == 4:
            outputValue = intInput[arg1]
            output.append(outputValue)
            position += 2
            if len(output) == 2:
                return [output, intInput, position, relativeBase, False]
            continue
        
        if action == 9:
            relativeBase += intInput[arg1]
            position += 2
            continue
        
        arg2 = getArg(intInput, modes, position, 2, relativeBase)
        
        resultPos = getArg(intInput, modes, position, 3, relativeBase)

        if action == 1:
            result = intInput[arg1] + intInput[arg2]
            intInput[resultPos] = result
            position += 4
        elif action == 2:
            result = intInput[arg1] * intInput[arg2]
            intInput[resultPos] = result
            position += 4
        elif action == 5:
            if intInput[arg1] != 0:
                position = intInput[arg2]
            else:
                position += 3
        elif action == 6:
            if intInput[arg1] == 0:
                position = intInput[arg2]
            else:
                position += 3
        elif action == 7:
            if intInput[arg1] < intInput[arg2]:
                intInput[resultPos] = 1
            else:
                intInput[resultPos] = 0
            position += 4
        elif action == 8:
            if intInput[arg1] == intInput[arg2]:
                intInput[resultPos] = 1
            else:
                intInput[resultPos] = 0
            position += 4
        else:
            print(action)
            print("Failure: unknown opcode")
            return

def getArg(intInput, modes, position, number, relativeBase):
    if modes[number] == 0:
        arg = intInput[position + number]
    elif modes[number] == 2:
        arg = intInput[position + number] + relativeBase
    else:
        arg = position + number
    return arg      
        

def convertToInt(input):
    numbers = []
    for stringNumber in input:
        numbers.append(int(stringNumber))

    return numbers

def splitNumber(number):
    numbers = []
    for digit in str(number):
        numbers.append(int(digit))
    return numbers

def actionSplit(number):
    modes = {}
    modes[1] = 0
    modes[2] = 0
    modes[3] = 0
    modes['action'] = number % 100
    split = splitNumber(number)
    split.reverse()
    for i in range(2, len(split)):
        modes[i-1] = split[i]
    
    return modes

def turn(output, position, direction):
    if output == 0:
        direction = Direction((direction + 4 - 1) % 4)
    else:
        direction = Direction((direction + 1) % 4)
    
    if direction == Direction.UP:
        position = (position[0], position[1] - 1)
    elif direction == Direction.RIGHT:
        position = (position[0] + 1, position[1])
    elif direction == Direction.DOWN:
        position = (position[0], position[1] + 1)
    else:
        position = (position[0] - 1, position[1])

    return position, direction

def paint(firstField):
    intInput = convertToInt(input.split(','))
    intInput += [0 for x in range(10000)]
    result = {}
    positionOnField = (0,0)
    result[positionOnField] = firstField
    position = 0
    relativeBase = 0
    direction = Direction.UP
    while True:
        field = result.get(positionOnField, 0)
            
        output, intInput, position, relativeBase, finished = do([field], intInput, position, relativeBase)
        if finished:
            return result
        
        result[positionOnField] = output[0]

        positionOnField, direction = turn(output[1], positionOnField, direction)

def printImage(result):
    minWidth = min(x[0] for x in result.keys())
    minHeight = min(x[1] for x in result.keys())
    width = max(x[0] for x in result.keys()) - minWidth
    height = max(x[1] for x in result.keys()) - minHeight
    image = [[0 for x in range(width + 1)] for y in range(height + 1)]

    for position in result.keys():
        if result[position] == 0:
            continue
        adjustedPosition = (position[0] + minWidth, position[1] + minHeight)
        image[adjustedPosition[1]][adjustedPosition[0]] = result[position]
    
    for y in range(len(image)):
        print(image[y])



#part1
result = paint(0)
print(len(result.keys()))

#part2
result2 = paint(1)
printImage(result2)
