from HelperFunctions import inputsplit
import copy


def do1(puzzleInput):
    seatPlan = prepareInput(puzzleInput)

    newSeatPlan = updateSeatPlan(seatPlan, newSeatState1)
                
    return countOccupiedSeats(newSeatPlan)

def do2(puzzleInput):
    seatPlan = prepareInput(puzzleInput)

    newSeatPlan = updateSeatPlan(seatPlan, newSeatState2)
                
    return countOccupiedSeats(newSeatPlan)

def updateSeatPlan(seatPlan, stateFunction):
    newSeatPlan = copy.deepcopy(seatPlan)

    seatsChanged = True
    while seatsChanged:
        seatPlan = copy.deepcopy(newSeatPlan)
        seatsChanged = False
        for row in range(1, len(seatPlan) - 1):
            for column in range(1, len(seatPlan[0]) - 1):
                changed = stateFunction((row, column), newSeatPlan, seatPlan)
                seatsChanged = seatsChanged or changed
    
    return newSeatPlan

def prepareInput(puzzleInput):
    seatPlan = [['.' for x in puzzleInput[0]] for y in puzzleInput]
    for i in range(len(puzzleInput)):
        for j in range(len(puzzleInput[0])):
            seatPlan[i][j] = puzzleInput[i][j]

    floor = ['.' for x in puzzleInput[0]]

    seatPlan.insert(0, floor)
    seatPlan.append(floor)

    for i in range(len(seatPlan)):
        seatPlan[i] = ['.'] + seatPlan[i] + ['.']
    
    return seatPlan

def countOccupiedSeats(seatPlan):
    count = 0
    for i in range(len(seatPlan)):
        count += seatPlan[i].count('#')

    return count

def newSeatState1(seatPosition, newSeatPlan, seatPlan):
    row, column = seatPosition
    seatState = seatPlan[row][column]
    occupiedAdjacentSeats = occupiedSeats(seatPosition, seatPlan)
    if  seatState == 'L' and occupiedAdjacentSeats == 0:
        newSeatPlan[row][column] = '#'
        return True
    elif seatState == '#' and occupiedAdjacentSeats > 3:
        newSeatPlan[row][column] = 'L'
        return True

    return False

def newSeatState2(seatPosition, newSeatPlan, seatPlan):
    row, column = seatPosition
    seatState = seatPlan[row][column]
    occupiedAdjacentSeats = occupiedVisibleSeats(seatPosition, seatPlan)
    if  seatState == 'L' and occupiedAdjacentSeats == 0:
        newSeatPlan[row][column] = '#'
        return True
    elif seatState == '#' and occupiedAdjacentSeats > 4:
        newSeatPlan[row][column] = 'L'
        return True

    return False

def occupiedSeats(seatPosition, seatPlan):
    numberOfOccupiedSeats = 0

    row, column = seatPosition

    for x in range(row - 1, row + 2):
        for y in range(column - 1, column + 2):
            if x == row and y == column:
                continue
            if seatPlan[x][y] == '#':
                numberOfOccupiedSeats += 1
    return numberOfOccupiedSeats

def occupiedVisibleSeats(seatPosition, seatPlan):
    numberOfOccupiedSeats = 0
    
    row, column = seatPosition

    left = seatPlan[row][0:column]
    left.reverse()
    right = seatPlan[row][column + 1:]    
    up = []
    for x in range(row - 1, -1, -1):
        up.append(seatPlan[x][column])
    down = []
    for x in range(row + 1, len(seatPlan)):
        down.append(seatPlan[x][column])
    
    leftUpDiag = []
    rightUpDiag = []
    y1 = column
    y2 = column
    for x in range(row - 1, -1, -1):
        y1 = y1 - 1
        y2 = y2 + 1
        if y1 >= 0:
            leftUpDiag.append(seatPlan[x][y1])
        if y2 < len(seatPlan[0]):
            rightUpDiag.append(seatPlan[x][y2])
    
    leftDownDiag = []
    rightDownDiag = []
    y1 = column
    y2 = column
    for x in range(row + 1, len(seatPlan), 1):
        y1 = y1 - 1
        y2 = y2 + 1
        if y1 >= 0:
            leftDownDiag.append(seatPlan[x][y1])
        if y2 < len(seatPlan[0]):
            rightDownDiag.append(seatPlan[x][y2])
        
    if occupiedSeatVisible(left):
        numberOfOccupiedSeats += 1
    if occupiedSeatVisible(right):
        numberOfOccupiedSeats += 1
    if occupiedSeatVisible(up):
        numberOfOccupiedSeats += 1
    if occupiedSeatVisible(down):
        numberOfOccupiedSeats += 1
    if occupiedSeatVisible(leftUpDiag):
        numberOfOccupiedSeats += 1
    if occupiedSeatVisible(rightUpDiag):
        numberOfOccupiedSeats += 1
    if occupiedSeatVisible(leftDownDiag):
        numberOfOccupiedSeats += 1
    if occupiedSeatVisible(rightDownDiag):
        numberOfOccupiedSeats += 1
    
    return numberOfOccupiedSeats
    
def occupiedSeatVisible(seatLine):
    for seat in seatLine:
        if seat == '#':
            return True
        elif seat == 'L':
            return False
    return False


def do():
    with open ('Input/day11.txt') as f:
        strInput = f.read()

    splitInput = inputsplit(strInput, '\n')

    print(do1(splitInput))
    print(do2(splitInput))
    
do()