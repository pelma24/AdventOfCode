import itertools

input = """3,8,1001,8,10,8,105,1,0,0,21,34,51,76,101,114,195,276,357,438,99999,3,9,1001,9,3,9,1002,9,3,9,4,9,99,3,9,101,4,9,9,102,4,9,9,1001,9,5,9,4,9,99,3,9,1002,9,4,9,101,3,9,9,102,5,9,9,1001,9,2,9,1002,9,2,9,4,9,99,3,9,1001,9,3,9,102,2,9,9,101,4,9,9,102,3,9,9,101,2,9,9,4,9,99,3,9,102,2,9,9,101,4,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,99"""

def inputSplit(input):
    return input.split(',')

def do(input, intInput, position):
    output = input[0]

    while True:
        modes = actionSplit(intInput[position])
        action = modes['action']
        if action == 9:
            print('Finished')
            return [output, intInput, position, True]
        
        arg1 = getArg(intInput, modes, position, 1)
        
        if action == 3:
            inputValue = input.pop(0)
            intInput[intInput[position + 1]] = inputValue
            position += 2
            continue

        if action == 4:
            output = arg1
            position += 2
            return [output, intInput, position, False]    
        
        arg2 = getArg(intInput, modes, position, 2)
        
        resultPos = intInput[position + 3]

        if action == 1:
            result = arg1 + arg2
            intInput[resultPos] = result
            position += 4
        elif action == 2:
            result = arg1 * arg2
            intInput[resultPos] = result
            position += 4
        elif action == 5:
            if arg1 != 0:
                position = arg2
            else:
                position += 3
        elif action == 6:
            if arg1 == 0:
                position = arg2
            else:
                position += 3
        elif action == 7:
            if arg1 < arg2:
                intInput[resultPos] = 1
            else:
                intInput[resultPos] = 0
            position += 4
        elif action == 8:
            if arg1 == arg2:
                intInput[resultPos] = 1
            else:
                intInput[resultPos] = 0
            position += 4
        else:
            print(action)
            print("Failure")
            return

        

def getArg(intInput, modes, position, number):
    if modes[number] == 0:
        arg = intInput[intInput[position + number]]
    else:
        arg = intInput[position + number]
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

    split = splitNumber(number)
    modes['action'] = split[-1]
    split.reverse()
    for i in range(2, len(split)):
        modes[i-1] = split[i]
    
    return modes
 

intInput = convertToInt(input.split(','))
permutations = itertools.permutations([5,6,7,8,9], 5)
position = 0


results = []

loop = True

for permutation in list(permutations):
    saves = {}
    loop = True
    input2 = 0
    for a in range(5):
        machineInput = [permutation[a], input2]
        input2, inputSave, positionSave, finished = do(machineInput, intInput.copy(), position)
        saves[a] = [inputSave, positionSave]
    
    while loop:
        for a in range(5):
            #print(a)
            input2, inputSave, positionSave, finished = do([input2], saves[a][0], saves[a][1])
            if finished:
                results.append(input2)
                loop = False
            saves[a] = [inputSave, positionSave]
    
        
        
print(max(results))