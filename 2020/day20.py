from HelperFunctions import inputsplit
import re

class Tile:
    def __init__(self, number=0, upper=[], lower=[], right=[], left=[], inner=[]):
        self.upper = upper.copy()
        self.lower = lower.copy()
        self.right = right.copy()
        self.left = left.copy()
        
        self.inner = inner

        self.number = number

        self.neighbors = set()

        self.leftNeighbor = 0
        self.rightNeighbor = 0
        self.upperNeighbor = 0
        self.lowerNeighbor = 0

        self.fixed = False

    def flip(self):
        if self.fixed:
            return
        tmp = self.upper.copy()
        self.upper = self.lower.copy()
        self.lower = tmp.copy()
        self.right.reverse()
        self.left.reverse()

        self.inner.reverse()     

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

            self.rotateInner()
        if angle == 180:
            self.rotate(90)
            self.rotate(90)
        if angle == 270:
            self.rotate(90)
            self.rotate(90)
            self.rotate(90)
    
    def rotateInner(self):
        newInner = []
        for x in range(len(self.inner)):
            column = []
            for y in range(len(self.inner)):
                column.append(self.inner[y][x])
            column.reverse()
            newInner.append(column)
        self.inner = newInner.copy()

    def checkForEqualSides(self, otherTile):
        if self.upper == otherTile.lower:
            if self.fixed:
                otherTile.fixed = True
                self.upperNeighbor = otherTile
                otherTile.lowerNeighbor = self
            return True
        if self.lower == otherTile.upper:
            if self.fixed:
                otherTile.fixed = True
                self.lowerNeighbor = otherTile
                otherTile.upperNeighbor = self
            return True
        if self.right == otherTile.left:
            if self.fixed:
                otherTile.fixed = True
                self.rightNeighbor = otherTile
                otherTile.leftNeighbor = self
            return True
        if self.left == otherTile.right:
            if self.fixed:
                otherTile.fixed = True
                self.leftNeighbor = otherTile
                otherTile.rightNeighbor = self
            return True
        return False

    def fixNeighbors(self):
        for neighbor in self.neighbors:            
            self.couldBeNeighbors(neighbor)

    def couldBeNeighbors(self, otherTile):
        flipped = False
        while True:
            for angle in [0, 90, 180, 270]:
                otherTile.rotate(angle)
                if self.checkForEqualSides(otherTile):
                    self.neighbors.add(otherTile)
                    return True
            otherTile.flip()
            if flipped:
                break
            flipped = True

        return False
            
def do1(puzzleInput):
    tiles = extractTiles(puzzleInput)

    neighbors = getNeighbors(tiles)

    multiplied = 1
    for key,neighbors in neighbors.items():
        if len(neighbors) == 2:
            multiplied *= key

    return multiplied

def do2(puzzleInput):
    tiles = extractTiles(puzzleInput)

    neighbors = getNeighbors(tiles)

    corners = [x for x in tiles if len(x.neighbors) == 2]
    
    arrange(tiles, neighbors, corners[0])

    corner1 = [x for x in corners if x.rightNeighbor != 0 and x.lowerNeighbor != 0][0]

    image = buildImage(tiles, corner1)
    
    notSeaMonsters = notSeaMonsterHashes(image)

    return notSeaMonsters

def notSeaMonsterHashes(image):
    imageTile = Tile(inner=image)
    
    numberOfHashes = 0    
    for line in imageTile.inner:
        numberOfHashes += line.count('#')

    middleLine = '#[\.\#]{4}##[\.\#]{4}##[\.\#]{4}###'
    upperLine = '[\.\#]{18}#[\.\#]{1}'
    lowerLine = '[\.\#]{1}#[\.\#]{2}#[\.\#]{2}#[\.\#]{2}#[\.\#]{2}#[\.\#]{2}#[\.\#]{3}'
    rotated = False
    while True:
        for rotationAngle in [0, 90, 180, 270]:
            seaMonsters = 0
            imageTile.rotate(rotationAngle)
            for index,line in enumerate(imageTile.inner):
                s = ''
                imageTile.inner[index] = s.join(line)

            for index,line in enumerate(imageTile.inner[0:-1]):
                matchMiddle = re.search(middleLine, line)
                if matchMiddle:
                    startPos = matchMiddle.start()
                    matchLower = re.fullmatch(lowerLine, imageTile.inner[index + 1][startPos:startPos + 20])
                    matchUpper = re.fullmatch(upperLine, imageTile.inner[index - 1][startPos:startPos + 20])
                    if matchLower and matchUpper:
                        seaMonsters += 1
            if seaMonsters:
                return numberOfHashes - seaMonsters * 15
        
        imageTile.flip()
        if rotated:
            break
        rotated = True

    return numberOfHashes - seaMonsters * 15

def arrange(tiles, neighbors, tile):
    tile.fixed = True
    tile.fixNeighbors()
    while any([not x.fixed for x in tiles]):
        for otherTile in [x for x in tiles if x.fixed]:
            otherTile.fixNeighbors()

def buildImage(tiles, corner1):
    image = []
    currentTile = corner1
    lowerNeighbor = currentTile.lowerNeighbor
    while lowerNeighbor:
        imageLine = currentTile.inner.copy()
        rightNeighbor = currentTile.rightNeighbor
        while rightNeighbor:
            for x,line in enumerate(imageLine):
                imageLine[x] = line + rightNeighbor.inner[x]
            rightNeighbor = rightNeighbor.rightNeighbor
        for line in imageLine:
            image.append(line)
        currentTile = lowerNeighbor
        lowerNeighbor = currentTile.lowerNeighbor
    imageLine = currentTile.inner.copy()
    rightNeighbor = currentTile.rightNeighbor
    while rightNeighbor:
        for x,line in enumerate(imageLine):
            imageLine[x] = line + rightNeighbor.inner[x]
        rightNeighbor = rightNeighbor.rightNeighbor
    for line in imageLine:
        image.append(line)

    return image

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
        
        inner = []
        for line in lines[2:-1]:
            inner.append(list(line[1:-1]))

        tiles.append(Tile(number, upper, lower, right, left, inner))

    return tiles

def getNeighbors(tiles):
    neighbors = {}
    for tile in tiles:
        neighbors[tile.number] = []
        for otherTile in tiles:
            if tile == otherTile:
                continue
            if tile.couldBeNeighbors(otherTile):
                neighbors[tile.number].append(otherTile.number)

    return neighbors

def do():
    with open ('Input/day20.txt') as f:
        strInput = f.read()

    splitInput = inputsplit(strInput, '\n\n')
    
    print(do1(splitInput))
    print(do2(splitInput))
    
do()