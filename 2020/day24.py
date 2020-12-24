from HelperFunctions import inputsplit
from copy import deepcopy

directions = {'e': (1,-1,0), 'w': (-1,1,0), 'se': (0,-1,1), 'sw': (-1,0,1), 'ne': (1,0,-1), 'nw': (0,1,-1)}

def do1(puzzleInput):
    tiles = set()
    
    rotate(puzzleInput, tiles)

    return len(tiles)    

def do2(puzzleInput):
    tiles = set()
    
    rotate(puzzleInput, tiles)

    newTiles = gameOfLife(tiles, 100)
    
    return len(newTiles)

def rotate(puzzleInput, tiles):
    for line in puzzleInput:
        tile = (0,0,0)
        direction = ''
        for thing in line:
            direction += thing
            if direction in directions:
                xStep,yStep,zStep = directions[direction]
                x,y,z = tile
                tile = (x + xStep, y + yStep, z + zStep)
                direction = ''
        if tile in tiles:
            tiles.remove(tile)
        else:
            tiles.add(tile)

def gameOfLife(tiles, rounds):
    newTiles = deepcopy(tiles)
    for _ in range(rounds):
        tiles = deepcopy(newTiles)
        neighbors = set()
        for tile in tiles:
            allNeighbors = getNeighbors(tile, tiles)
            neighbors = neighbors.union(allNeighbors)
            blackNeighbors = countBlackNeighbors(allNeighbors, tiles)
            if blackNeighbors == 0 or blackNeighbors > 2:
                newTiles.remove(tile)
        for neighbor in neighbors:
            if neighbor in tiles:
                continue
            blackNeighbors = countBlackNeighbors(getNeighbors(neighbor, tiles), tiles)
            if blackNeighbors == 2:
                newTiles.add(neighbor)    
    return newTiles

def getNeighbors(tile, tiles):
    x,y,z = tile
    
    neighbors = set([(x + xStep, y + yStep, z + zStep) for xStep,yStep,zStep in directions.values()])

    return neighbors

def countBlackNeighbors(neighbors, tiles):
    count = len([neighbor for neighbor in neighbors if neighbor in tiles])
    return count

def do():
    with open ('Input/day24.txt') as f:
        strInput = f.read()

    puzzleInput = strInput.split('\n')

    print(do1(puzzleInput))
    print(do2(puzzleInput))
    
do()