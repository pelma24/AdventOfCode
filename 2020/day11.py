from HelperFunctions import inputsplit
import copy


def do1(puzzleInput):
    seatPlan = prepareInput(puzzleInput)

    newSeatPlan = updateSeatPlan(seatPlan, False, 3)
                
    return countOccupiedSeats(newSeatPlan)

def do2(puzzleInput):
    seatPlan = prepareInput(puzzleInput)

    newSeatPlan = updateSeatPlan(seatPlan, True, 4)
                
    return countOccupiedSeats(newSeatPlan)

def updateSeatPlan(seatPlan, wholeLine, maxAdjacentSeats):
    newSeatPlan = copy.deepcopy(seatPlan)

    seatsChanged = True
    while seatsChanged:
        seatPlan = copy.deepcopy(newSeatPlan)
        seatsChanged = False
        for row in range(1, len(seatPlan) - 1):
            for column in range(1, len(seatPlan[0]) - 1):
                changed = newSeatState((row, column), newSeatPlan, seatPlan, wholeLine, maxAdjacentSeats)
                seatsChanged = seatsChanged or changed
    
    return newSeatPlan

def prepareInput(puzzleInput):
    seatPlan = [[] for x in puzzleInput]
    for i in range(len(puzzleInput)):
        for j in range(len(puzzleInput[0])):
            seatPlan[i].append(puzzleInput[i][j])
        seatPlan[i] = ['.'] + seatPlan[i] + ['.']
        
    floor = ['.'] + ['.' for x in puzzleInput[0]] + ['.']

    seatPlan.insert(0, floor)
    seatPlan.append(floor)   
    
    return seatPlan

def countOccupiedSeats(seatPlan):
    count = 0
    for row in seatPlan:
        count += row.count('#')

    return count

def newSeatState(seatPosition, newSeatPlan, seatPlan, wholeLine, maxAdjacentSeats):
    row, column = seatPosition
    seatState = seatPlan[row][column]
    occupiedAdjacentSeats = occupiedSeats(seatPosition, seatPlan, wholeLine)
    if  seatState == 'L' and occupiedAdjacentSeats == 0:
        newSeatPlan[row][column] = '#'
        return True
    elif seatState == '#' and occupiedAdjacentSeats > maxAdjacentSeats:
        newSeatPlan[row][column] = 'L'
        return True

    return False

def occupiedSeats(seatPosition, seatPlan, wholeLine):
    numberOfOccupiedSeats = 0
    
    for stepX in [-1, 0, 1]:
        for stepY in [-1, 0, 1]:
            if stepX == 0 and stepY == 0:
                continue
            if lookForOccupiedSeats(seatPlan, seatPosition, stepX, stepY, wholeLine):
                numberOfOccupiedSeats += 1
    
    return numberOfOccupiedSeats

def lookForOccupiedSeats(seatPlan, seatPosition, stepX, stepY, wholeLine):
    row, column = seatPosition
    posX = row + stepX
    posY = column + stepY
    
    if wholeLine:
        xEndLow = 0
        yEndLow = 0
        xEndHigh = len(seatPlan)
        yEndHigh = len(seatPlan[0])
    else:
        xEndLow =  row - 1
        xEndHigh = row + 2
        yEndLow = column - 1
        yEndHigh = column + 2

    while xEndLow <= posX < xEndHigh and yEndLow <= posY < yEndHigh:
        if seatPlan[posX][posY] == 'L':
            return False
        if seatPlan[posX][posY] == '#':
            return True
        posX = posX + stepX
        posY = posY + stepY
    return False

def do():
    with open ('Input/day11.txt') as f:
        strInput = f.read()

    splitInput = inputsplit(strInput, '\n')

    print(do1(splitInput))
    print(do2(splitInput))
    
do()