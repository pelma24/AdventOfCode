from HelperFunctions import inputsplit

def do1(puzzleInput):
    success, acc = execute(puzzleInput)
    
    if not success:
        return acc
    else:
        return 'error'

def do2(oldPuzzleInput):
    replacePosition = -1
    while (replacePosition < len(oldPuzzleInput)):
        replacePosition += 1
        puzzleInput = oldPuzzleInput.copy()
        
        if not replaceInstruction(replacePosition, puzzleInput):
            continue
        
        success, acc = execute(puzzleInput)

        if success:
            return acc
        
    return 'error'    

def execute(puzzleInput):
    acc = 0

    visited = [0 for x in range(len(puzzleInput))]

    position = 0
    while True:
        if position == len(puzzleInput):
            return [True, acc]
        if visited[position] == 1:
            return [False, acc]
    
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