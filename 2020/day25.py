from HelperFunctions import inputsplit

def do1(puzzleInput):
    cardPublic = int(puzzleInput[0])
    doorPublic = int(puzzleInput[1])

    loopSizeCard = getLoopSize(cardPublic, 7)
    
    return calculateEncryptionKey(loopSizeCard, doorPublic)

def do2(puzzleInput):
    return 'done'

def getLoopSize(publicKey, subjectNumber):
    value = 1
    loop = 0
    while value != publicKey:
        loop += 1
        value = value * subjectNumber
        value = value % 20201227

    return loop

def calculateEncryptionKey(loopSize, subjectNumber):
    value = 1
    for _ in range(loopSize):
        value = value * subjectNumber
        value = value % 20201227
    
    return value

def do():
    with open ('Input/day25.txt') as f:
        strInput = f.read()

    puzzleInput = strInput.split('\n')

    print(do1(puzzleInput))
    print(do2(puzzleInput))
    
do()