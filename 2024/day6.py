from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt
from collections import defaultdict

directions = {'<': (-1,0), '>':(1,0), 'v':(0,1), '^':(0,-1)}

def createMap(strInput):
	
	map = {}

	lines = strInput.split('\n')
	for y,line in enumerate(lines):
		for x,value in enumerate(line):
			map[(x,y)] = value

	return map

def turnRight(direction):
	match (direction):
		case (-1,0):
			return (0,-1)
		case (1,0):
			return (0,1)
		case (0,1):
			return (-1,0)
		case (0,-1):
			return (1,0)
		
def do1(strInput):
	
	map = createMap(strInput)

	currentPos = [x for x in map.keys() if map[x] in ['>','<','v','^']][0]
	currentDirection = directions[map[currentPos]]
	map[currentPos] = 'X'

	while currentPos in map.keys():
		possibleNewPos = (currentPos[0] + currentDirection[0], currentPos[1] + currentDirection[1])
		if not(possibleNewPos in map):
			break
		if map[possibleNewPos] == '#':
			currentDirection = turnRight(currentDirection)		
		else:
			currentPos = possibleNewPos
			map[currentPos] = 'X'

	result = sum([1 for x in map if map[x] == 'X'])
	return result

def do2(strInput):
	
	loops = 0
	map = createMap(strInput)
	
	for key in map.keys():
		isLoop = False
		currentMap = map.copy()
		if currentMap[key] in ['#','>','<','v','^']:
			continue
		currentMap[key] = '#'	
		mapDirections = defaultdict(list)
		currentPos = [x for x in currentMap.keys() if currentMap[x] in ['>','<','v','^']][0]
		currentDirection = directions[currentMap[currentPos]]
		currentMap[currentPos] = 'X'
		mapDirections[currentPos].append(currentDirection)

		while currentPos in currentMap.keys():
			possibleNewPos = (currentPos[0] + currentDirection[0], currentPos[1] + currentDirection[1])
			if not(possibleNewPos in currentMap):
				break
			if currentMap[possibleNewPos] == '#':
				currentDirection = turnRight(currentDirection)		
			elif currentMap[possibleNewPos] == 'X' and currentDirection in mapDirections[possibleNewPos]:
				isLoop = True
				break
			else:
				currentPos = possibleNewPos
				currentMap[currentPos] = 'X'
				mapDirections[currentPos].append(currentDirection)
		
		if isLoop:
			loops = loops + 1	
	
	return loops

def do():
	strInput = readInputFile(6)

	print(do1(strInput))
	print(do2(strInput))

	print('done')


do()