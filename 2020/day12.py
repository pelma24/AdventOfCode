from HelperFunctions import inputsplit
from enum import Enum

directions = {'east' : 0, 'south' : 1, 'west' : 2, 'north' : 3}

def do1(puzzleInput):
    east = 0
    north = 0
    direction = 0

    for movement in puzzleInput:
        action = movement[0]
        count = int(movement[1:])
        east, north, direction = move(east, north, direction, action, count)
    
    return abs(north) + abs(east)

def move(east, north, direction, action, count):
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

    return [east, north, direction]

def turn(direction, turnOrder, degrees):
    if turnOrder == 'R':
        direction = (direction + int(degrees / 90)) % 4
    elif turnOrder == 'L':
        direction = (direction + (4 - int(degrees / 90))) % 4
    
    return direction

def driveForward(east, north, direction, count):
    action = 'X'
    if direction == 0:
        action = 'E'
    elif direction == 1:
        action = 'S'
    elif direction == 2:
        action = 'W'
    elif direction == 3:
        action = 'N'
    east, north, direction = move(east, north, direction, action, count)
    
    return [east, north] 

def do2(puzzleInput):
    return 'done'

def do():
    with open ('Input/day12.txt') as f:
        strInput = f.read()

    splitInput = inputsplit(strInput, '\n')

    print(do1(splitInput))
    print(do2(splitInput))
    
do()