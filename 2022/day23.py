from collections import namedtuple
from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt

directions = ['n', 's', 'w', 'e']

Neighbors = namedtuple('Neighbors', ['NW', 'N', 'NE', 'W', 'E', 'SW', 'S', 'SE'])

def do1(splitInput):
	elves = extractElves(splitInput)
	
	directionPos = 0

	for _ in range(10):
		newElves = {}
		for elf in elves:
			neighbors = getNeighbors(elf, elves)
			if not neighbors.N and not neighbors.NE and not neighbors.NW and not neighbors.W and not neighbors.E and not neighbors.SW and not neighbors.S and not neighbors.SE:
				continue
			for i in range(4):
				direction = directions[(directionPos + i) % 4]
				match direction:
					case 'n':
						if not neighbors.N and not neighbors.NE and not neighbors.NW:
							newElves[elf] = (elf[0] - 1, elf[1])
							break
					case 's':
						if not neighbors.S and not neighbors.SE and not neighbors.SW:
							newElves[elf] = (elf[0] + 1, elf[1])
							break
					case 'w':
						if not neighbors.W and not neighbors.NW and not neighbors.SW:
							newElves[elf] = (elf[0], elf[1] - 1)
							break
					case 'e':
						if not neighbors.E and not neighbors.NE and not neighbors.SE:
							newElves[elf] = (elf[0], elf[1] + 1)
							break
		directionPos = (directionPos + 1) % 4

		newPositions = list(newElves.values())
		for elf,newPos in newElves.items():
			if newPositions.count(newPos) == 1:
				elves.remove(elf)
				elves.append(newPos)

	xMin = min([elf[0] for elf in elves])
	xMax = max([elf[0] for elf in elves])
	yMin = min([elf[1] for elf in elves])
	yMax = max([elf[1] for elf in elves])

	freeTiles = 0
	for x in range(xMin, xMax + 1):
		for y in range(yMin, yMax + 1):
			if (x,y) not in elves:
				freeTiles += 1

	return freeTiles

def do2(splitInput):
	elves = extractElves(splitInput)
	
	directionPos = 0

	round = 0
	while True:
		round += 1
		newElves = {}
		for elf in elves:
			neighbors = getNeighbors(elf, elves)
			if not neighbors.N and not neighbors.NE and not neighbors.NW and not neighbors.W and not neighbors.E and not neighbors.SW and not neighbors.S and not neighbors.SE:
				continue
			for i in range(4):
				direction = directions[(directionPos + i) % 4]
				match direction:
					case 'n':
						if not neighbors.N and not neighbors.NE and not neighbors.NW:
							newElves[elf] = (elf[0] - 1, elf[1])
							break
					case 's':
						if not neighbors.S and not neighbors.SE and not neighbors.SW:
							newElves[elf] = (elf[0] + 1, elf[1])
							break
					case 'w':
						if not neighbors.W and not neighbors.NW and not neighbors.SW:
							newElves[elf] = (elf[0], elf[1] - 1)
							break
					case 'e':
						if not neighbors.E and not neighbors.NE and not neighbors.SE:
							newElves[elf] = (elf[0], elf[1] + 1)
							break
		directionPos = (directionPos + 1) % 4

		newPositions = list(newElves.values())
		if not newPositions:
			return round
		for elf,newPos in newElves.items():
			if newPositions.count(newPos) == 1:
				elves.remove(elf)
				elves.append(newPos)

def extractElves(splitInput):
	elves = []
	for lineNumber,line in enumerate(splitInput):
		for position,tile in enumerate(line):
			if tile == '#':
				elves.append((lineNumber,position))
	
	return elves

def getNeighbors(elf, elves):
	elfX,elfY = elf

	neighbors = []

	for xDiff in [-1, 0, 1]:
		for yDiff in [-1, 0, 1]:
			if xDiff == 0 and yDiff == 0:
				continue
			if (elfX + xDiff, elfY + yDiff) in elves:
				neighbors.append(True)
			else:
				neighbors.append(False)
	
	return Neighbors(NW=neighbors[0],N=neighbors[1],NE=neighbors[2],W=neighbors[3],E=neighbors[4],SW=neighbors[5],S=neighbors[6],SE=neighbors[7])
	



def do():
	strInput = readInputFile(23)
	#strInput = readExampleInput(23)

	splitInput = strInput.split('\n')

	print(do1(splitInput))
	print(do2(splitInput))

	print('done')


do()