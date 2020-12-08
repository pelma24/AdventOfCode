from HelperFunctions import inputsplit

def do1(puzzleInput):
    acc = 0

    visited = [0 for x in range(len(puzzleInput))]

    position = 0
    while (visited[position] != 1):
        instructions = puzzleInput[position].split(' ')

        if instructions[0] == 'nop':
            visited[position] = 1
            position += 1
            continue
        if instructions[0] == 'acc':
            visited[position] = 1
            acc += int(instructions[1])
            position += 1
            continue
        if instructions[0] == 'jmp':
            visited[position] = 1
            position += int(instructions[1])
            continue

    return acc

def do2(oldPuzzleInput):
    replacePosition = -1
    while (replacePosition < len(oldPuzzleInput)):
        replacePosition += 1
        puzzleInput = oldPuzzleInput.copy()
        
        if not replaceInstruction(replacePosition, puzzleInput):
            continue

        acc = 0

        visited = [0 for x in range(len(puzzleInput))]

        position = 0
        while True:
            if position == len(puzzleInput):
                return acc
            if visited[position] == 1:
                break
        
            instructions = puzzleInput[position].split(' ')

            if instructions[0] == 'nop':
                visited[position] = 1
                position += 1
                continue
            if instructions[0] == 'acc':
                visited[position] = 1
                acc += int(instructions[1])
                position += 1
                continue
            if instructions[0] == 'jmp':
                visited[position] = 1
                position += int(instructions[1])
                continue

    return 'error'    

def replaceInstruction(position, puzzleInput):
    if 'acc' in puzzleInput[position]:
        return False
    else:
        instructions = puzzleInput[position].split(' ')
        if instructions[0] == 'jmp':
            puzzleInput[position] = 'nop ' + instructions[1]
        else:
            puzzleInput[position] = 'jmp ' + instructions[1]
    return True

def do():
    with open ('Input/day8.txt') as f:
        strInput = f.read()

    splitInput = inputsplit(strInput, '\n')

    print(do1(splitInput))
    print(do2(splitInput))
    
do()