from HelperFunctions import inputsplit
from enum import Enum

def do1(puzzleInput):
    east = 0
    north = 0
    direction = 0

    for movement in puzzleInput:
        action = movement[0]
        count = int(movement[1:])
        east, north, direction = move(east, north, action, count, direction)
    
    return abs(north) + abs(east)

def do2(puzzleInput):
    wayNorth = 1
    wayEast = 10

    east = 0
    north = 0

    for movement in puzzleInput:
        action = movement[0]
        count = int(movement[1:])
        wayNorth, wayEast, east, north = moveWithWaypoint(wayNorth, wayEast, east, north, action, count)

    return abs(north) + abs(east)

def moveWithWaypoint(wayNorth, wayEast, east, north, action, count):
    if action == 'N':
        wayNorth += count
    elif action == 'S':
        wayNorth -= count
    elif action == 'E':
        wayEast += count
    elif action == 'W':
        wayEast -= count
    elif action == 'L':
        wayNorth, wayEast = turnWaypoint(wayNorth, wayEast, 'L', count)
    elif action == 'R':
        wayNorth, wayEast = turnWaypoint(wayNorth, wayEast, 'R', count)
    elif action == 'F':
        east, north = driveToWaypoint(east, north, wayNorth, wayEast, count)

    return [wayNorth, wayEast, east, north]

def turnWaypoint(wayNorth, wayEast, turnOrder, count):
    if turnOrder == 'R':
        if count == 90:
            wayNorthtmp = wayNorth
            wayNorth = -wayEast
            wayEast = wayNorthtmp
        elif count == 180:
            wayNorth = -wayNorth
            wayEast = -wayEast
        elif count == 270:
            wayNorthtmp = wayNorth
            wayNorth = wayEast
            wayEast = -wayNorthtmp
    elif turnOrder == 'L':
        return turnWaypoint(wayNorth, wayEast, 'R', 360 - count)
    
    return [wayNorth, wayEast]

def driveToWaypoint(east, north, wayNorth, wayEast, count):

    for _ in range(count):
        east, north,_ = move(east, north, 'N', wayNorth)
        east, north,_ = move(east, north, 'E', wayEast)

    return [east, north]

def move(east, north, action, count, direction=0):
    if action == 'N':
        north += count
    elif action == 'S':
        north -= count
    elif action == 'E':
        east += count
    elif action == 'W':
        east -= count
    elif action == 'L':
        direction = turn(direction, 'L', count)
    elif action == 'R':
        direction = turn(direction, 'R', count)
    elif action == 'F':
        east, north = driveForward(east, north, direction, count)
    else:
        print('error')

    return [east, north, direction]

def turn(direction, turnOrder, degrees):
    if turnOrder == 'R':
        direction = (direction + int(degrees / 90)) % 4
    elif turnOrder == 'L':
        direction = (direction + (4 - int(degrees / 90))) % 4
    
    return direction

def driveForward(east, north, direction, count):
    actions = {0: 'E', 1: 'S', 2: 'W', 3: 'N'}
    
    action = actions.get(direction, 'X')
    
    east, north, _ = move(east, north, action, count, direction)
    
    return [east, north] 

def do():
    with open ('Input/day12.txt') as f:
        strInput = f.read()

    splitInput = inputsplit(strInput, '\n')

    print(do1(splitInput))
    print(do2(splitInput))
    
do()