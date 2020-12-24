from HelperFunctions import inputsplit
from copy import deepcopy

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
    skip = False
    for line in puzzleInput:
        x = 0
        y = 0
        z = 0
        for index in range(len(line)):
            if skip:
                skip = False
                continue
            direction = line[index]
            if direction == 'e':
                x += 1
                y -= 1
            elif direction == 'w':
                x -= 1
                y += 1
            elif direction == 's':
                skip = True
                secondPart = line[index+1]
                if secondPart == 'e':
                    z +=1
                    y -= 1
                elif secondPart == 'w':
                    x -= 1
                    z += 1
                else:
                    print('error')
            elif direction == 'n':
                skip = True
                secondPart = line[index+1]
                if secondPart == 'e':
                    z -= 1
                    x += 1
                elif secondPart == 'w':
                    z -= 1
                    y += 1
                else:
                    print('error')
        if (x,y,z) in tiles:
            tiles.remove((x,y,z))
        else:
            tiles.add((x,y,z))

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
    neighbors = set()
    
    x,y,z = tile
    
    neighbors.add((x + 1, y - 1, z))
    neighbors.add((x - 1, y + 1, z))
    neighbors.add((x, y - 1, z + 1))
    neighbors.add((x - 1, y, z + 1))
    neighbors.add((x + 1, y, z - 1))
    neighbors.add((x, y + 1, z - 1))

    return neighbors

def countBlackNeighbors(neighbors, tiles):
    count = 0
    for neighbor in neighbors:
        if neighbor in tiles:
            count += 1
    return count

def do():
    with open ('Input/day24.txt') as f:
        strInput = f.read()

    puzzleInput = strInput.split('\n')

    print(do1(puzzleInput))
    print(do2(puzzleInput))
    
do()