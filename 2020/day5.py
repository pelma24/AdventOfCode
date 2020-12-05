from HelperFunctions import inputsplit

def do1(puzzleInput):

    seatIDs = getSeatIDs(puzzleInput)
    
    return max(seatIDs)

def do2(puzzleInput):
    seatIDs = getSeatIDs(puzzleInput)
    
    seatIDs.sort()

    seatBeforeMissingSeat = [x for x in range(len(seatIDs) - 1) if seatIDs[x + 1] - seatIDs[x] > 1]

    return seatIDs[seatBeforeMissingSeat[0]] + 1

def getSeatIDs(puzzleInput):
    
    seatIDs = []

    for boardingPass in puzzleInput:
        seatID = calculateSeatID(boardingPass)
        seatIDs.append(seatID)

    return seatIDs

def calculateSeatID(boardingPass):
    seatID = 0
    
    rowCalc = boardingPass[0:7]
    columnCalc = boardingPass[7:]

    row = calculatePosition(rowCalc, 127)
    column = calculatePosition(columnCalc, 7)
    seatID = row * 8 + column
    return seatID

def calculatePosition(instructions, upper):
    lower = 0

    for instruction in instructions:
        if instruction in ['F', 'L']:
            upper = lower + int((upper - lower) / 2)
        else:
            lower = lower + int((upper - lower) / 2) + 1
    return upper

def do():
    with open ('Input/day5.txt') as f:
        strInput = f.read()

    splitInput = inputsplit(strInput, '\n')

    print(do1(splitInput))
    print(do2(splitInput))
    
do()