from HelperFunctions import inputsplit
from copy import deepcopy

def do1(puzzleInput):
    space = prepareInput(puzzleInput, 3)

    newSpace = changeState(space, 3)

    return countActiveCubes(newSpace, 3)

def do2(puzzleInput):
    space = prepareInput(puzzleInput, 4)

    newSpace = changeState(space, 4)

    return countActiveCubes(newSpace, 4)

def changeState(space, dimension):
    newSpace = deepcopy(space)

    for _ in range(6):
        space = deepcopy(newSpace)
        for x in range(1, len(space) - 1):
            for y in range(1, len(space[x]) - 1):
                for z in range(1, len(space[x][y]) - 1):
                    if dimension == 4:
                        for w in range(1, len(space[x][y][z]) - 1):
                            activeNeighbors = numberOfActiveNeighbors((x,y,z,w), space, dimension)
                            if space[x][y][z][w] == '#' and not (2 <= activeNeighbors <= 3):
                                newSpace[x][y][z][w] = '.'
                            elif space[x][y][z][w] == '.' and activeNeighbors == 3:
                                newSpace[x][y][z][w] = '#'
                    else:
                        activeNeighbors = numberOfActiveNeighbors((x,y,z), space, dimension)
                        if space[x][y][z] == '#' and not (2 <= activeNeighbors <= 3):
                            newSpace[x][y][z] = '.'
                        elif space[x][y][z] == '.' and activeNeighbors == 3:
                            newSpace[x][y][z] = '#'
        
    return newSpace

def numberOfActiveNeighbors(position, space, dimension):
    if dimension == 3:
        x,y,z = position
    else:
        x,y,z,w = position
    numberOfActiveNeighbors = 0
    step = [-1, 0, 1]
    for xStep in step:
        for yStep in step:
            for zStep in step:
                if dimension == 4:
                    for wStep in step:
                        if xStep == 0 and yStep == 0 and zStep == 0 and wStep == 0:
                            continue
                        if space[x + xStep][y + yStep][z + zStep][w + wStep] == '#':
                            numberOfActiveNeighbors += 1    
                else:
                    if xStep == 0 and yStep == 0 and zStep == 0:
                        continue
                    if space[x + xStep][y + yStep][z + zStep] == '#':
                        numberOfActiveNeighbors += 1
        
    return numberOfActiveNeighbors

def prepareInput(puzzleInput, dimension):
    size = 31
    if dimension == 3:
        space = [[['.' for z in range(size)] for y in range(size)] for x in range(size)]
    elif dimension == 4:
        space = [[[['.' for w in range(size)] for z in range(size)] for y in range(size)] for x in range(size)]
        w = int(size / 2)

    z = int(size / 2)
    x = int(size / 2 - int(len(puzzleInput) / 2))
    

    for a in range(len(puzzleInput)):
        y = int(size / 2 - int(len(puzzleInput[0]) / 2))
        for b in range(len(puzzleInput[0])):
            if dimension == 4:
                space[x][y][z][w] = puzzleInput[a][b]
            elif dimension == 3:   
                space[x][y][z] = puzzleInput[a][b]
            y += 1
        x += 1

    return space

def countActiveCubes(space, dimension):
    count = 0
    for x in range(len(space)):
        for y in range(len(space[x])):
            if dimension == 4:
                for z in range(len(space[x][y])):
                    count += space[x][y][z].count('#')
            elif dimension == 3:
                count += space[x][y].count('#')

    return count

def do():
    with open ('Input/day17.txt') as f:
        strInput = f.read()

    splitInput = inputsplit(strInput, '\n')

    print(do1(splitInput))
    print(do2(splitInput))
    
do()