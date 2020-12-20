from HelperFunctions import inputsplit

class Tile:
    def __init__(self, number=0, upper='', lower='', right='', left=''):
        self.upper = upper.copy()
        self.lower = lower.copy()
        self.right = right.copy()
        self.left = left.copy()

        self.number = number

        self.leftNeighbor = 0
        self.rightNeighbor = 0
        self.upperNeighbor = 0
        self.lowerNeighbor = 0

        self.flipped = False
        self.fixed = False
        self.angleRotated = 0

    def flip(self):
        if self.fixed:
            return
        tmp = self.upper.copy()
        self.upper = self.lower.copy()
        self.lower = tmp.copy()
        self.right.reverse()
        self.left.reverse()

        self.flipped = not self.flipped        

    def rotate(self, angle):
        if self.fixed:
            return
        if angle == 0:
            return
        if angle == 90:
            tmp = self.upper
            self.upper = self.left.copy()
            self.upper.reverse()
            self.left = self.lower.copy()
            self.lower = self.right.copy()
            self.lower.reverse()
            self.right = tmp.copy()
            self.angleRotated = (self.angleRotated + 90) % 360
        if angle == 180:
            self.rotate(90)
            self.rotate(90)
        if angle == 270:
            self.rotate(90)
            self.rotate(90)
            self.rotate(90)
    
    def checkForEqualSides(self, otherTile):
        if self.upper == otherTile.lower or self.lower == otherTile.upper or self.right == otherTile.left or self.left == otherTile.right:
            return True
        return False

    def couldBeNeighbors(self, otherTile):
        for angle in [0, 90, 180, 270]:
            otherTile.rotate(angle)
            if self.checkForEqualSides(otherTile):
                return True
        otherTile.flip()
        for angle in [0, 90, 180, 270]:
            otherTile.rotate(angle)
            if self.checkForEqualSides(otherTile):
                return True       

        return False
            
def do1(puzzleInput):
    tiles = extractTiles(puzzleInput)

    neighbors = getNeighbors(tiles)

    multiplied = 1
    for key,neighbors in neighbors.items():
        if neighbors == 2:
            multiplied *= key

    return multiplied

def do2(puzzleInput):
    tiles = extractTiles(puzzleInput)

    neighbors = getNeighbors(tiles)

    multiplied = 1
    for key,neighbors in neighbors.items():
        if neighbors == 2:
            multiplied *= key

    return multiplied

def extractTiles(puzzleInput):
    tiles = []

    for part in puzzleInput:
        lines = part.split('\n')
        number = int(lines[0][5:9])

        upper = list(lines[1])
        lower = list(lines[-1])

        left = []
        right = []
        for line in lines[1:]:
            left.append(line[0])
            right.append(line[-1])
        
        tiles.append(Tile(number, upper, lower, right, left))

    return tiles

def getNeighbors(tiles):
    neighbors = {}

    for tile in tiles:
        neighbors[tile.number] = 0

        for otherTile in tiles:
            if tile == otherTile:
                continue
            if tile.couldBeNeighbors(otherTile):
                neighbors[tile.number] += 1

    return neighbors 

def do():
    with open ('Input/day20.txt') as f:
        strInput = f.read()

    splitInput = inputsplit(strInput, '\n\n')
    
    print(do1(splitInput))
    print(do2(splitInput))
    
do()