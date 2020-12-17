from HelperFunctions import inputsplit
from copy import deepcopy

def do1(puzzleInput):
    points = prepareInput(puzzleInput, 3)

    points = changeState(points, 3)

    count = countActiveCubes(points)

    return count

def do2(puzzleInput):
    points = prepareInput(puzzleInput, 4)

    points = changeState(points, 4)

    count = countActiveCubes(points)

    return count

def changeState(points, dimension):
    newPoints = deepcopy(points)
    for _ in range(6):
        points = deepcopy(newPoints)
        neighbors = set()
        for point in points:
            directNeighbors = getNeighbors(point, points, dimension)
            neighbors = neighbors.union(directNeighbors)
            activeNeighbors = countActiveNeighbors(directNeighbors, points)
            if not (2 <= activeNeighbors <= 3):
                newPoints.remove(point)
        for neighbor in neighbors:
            if neighbor in points:
                continue
            activeNeighbors = countActiveNeighbors(getNeighbors(neighbor, points, dimension), points)
            if activeNeighbors == 3:
                newPoints.add(neighbor)
    return newPoints

def getNeighbors(point, points, dimension):
    neighbors = set()

    if dimension == 3:
        x,y,z = point
    elif dimension == 4:
        x,y,z,w = point

    step = [-1, 0, 1]
    for xStep in step:
        for yStep in step:
            for zStep in step:
                if dimension == 4:
                    for wStep in step:
                        if (xStep == 0 and yStep == 0 and zStep == 0 and wStep == 0):
                            continue
                        neighbors.add((x + xStep, y + yStep, z + zStep, w + wStep))
                elif dimension == 3:
                    if (xStep == 0 and yStep == 0 and zStep == 0):
                        continue
                    neighbors.add((x + xStep, y + yStep, z + zStep))

    return neighbors

def countActiveNeighbors(neighbors, points):
        
    activeNeighbors = [x for x in neighbors if x in points]
    
    return len(activeNeighbors)

def prepareInput(puzzleInput, dimension):
    points = set()

    for x,line in enumerate(puzzleInput):
        for y,cube in enumerate(line):
            if cube == '#':
                if dimension == 4:
                    points.add((x,y,0,0))
                elif dimension == 3:
                    points.add((x,y,0))

    return points

def countActiveCubes(space):
    return len(space)

def do():
    with open ('Input/day17.txt') as f:
        strInput = f.read()

    splitInput = inputsplit(strInput, '\n')

    print(do1(splitInput))
    print(do2(splitInput))
    
do()