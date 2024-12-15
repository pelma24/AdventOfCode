from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt
import copy


def printMap(map):
	maxWidth = max([x for (x,y) in map.keys()])
	maxHeight = max([y for (x,y) in map.keys()])

	printmap = [['.' for x in range(maxWidth + 1)] for y in range(maxHeight + 1)]

	for key,value in map.items():
		x,y = key
		printmap[y][x] = value

	for line in printmap:
		print("".join(line))
		
def createMap1(mapInput):
	map = {}

	for y,line in enumerate(mapInput.split('\n')):
		for x,value in enumerate(line):
			map[(x,y)] = value

	return map

def createMap2(mapInput):
	mapInput = mapInput.replace('#', '##')
	mapInput = mapInput.replace('.', '..')
	mapInput = mapInput.replace('@', '@.')
	mapInput = mapInput.replace('O', '[]')

	return createMap1(mapInput)

def createMoves(moveInput):
	moves = []
	for line in moveInput.split('\n'):
		for value in line:
			moves.append(value)
	
	return moves

def push(boxPos, direction, map):
	xbox,ybox = boxPos
	match direction:
		case '^':
			pushPos = (xbox,ybox - 1)
		case 'v':
			pushPos = (xbox,ybox + 1)
		case '<':
			pushPos = (xbox - 1,ybox)
		case '>':
			pushPos = (xbox + 1,ybox)
	
	match map[pushPos]:
		case '#':
			return False
		case '.':
			map[pushPos] = 'O'
			map[boxPos] = '.'
			return True
		case 'O':
			if push(pushPos, direction, map):
				map[pushPos] = 'O'
				map[boxPos] = '.'
				return True
			else:
				return False

def pushBigBox(boxPositions, direction, map):
	boxPos1,boxPos2 = boxPositions
	x1,y1 = boxPos1
	x2,y2 = boxPos2

	match direction:
		case '^':
			newPos = [(x1,y1-1),(x2,y2-1)]
		case 'v':
			newPos = [(x1,y1+1), (x2,y2+1)]
		case '<':
			newPos = [(x1-1,y1)]
		case '>':
			newPos = [(x2+1,y2)]

	movingPossible = True
	for pos in newPos:
		match map[pos]:
			case '.':
				continue
			case '#':
				movingPossible = False
			case '[':
				a,b = pos
				if movingPossible:
					movingPossible = pushBigBox([(a,b),(a+1,b)], direction, map)
			case ']':
				a,b = pos
				if movingPossible:
					movingPossible = pushBigBox([(a-1,b),(a,b)], direction, map)

	if movingPossible:
		match direction:
			case '^':
				map[(x1,y1-1)] = '['
				map[(x2,y2-1)] = ']'
				map[(x1,y1)] = '.'
				map[(x2,y2)] = '.'
			case 'v':
				map[(x1,y1+1)] = '['
				map[(x2,y2+1)] = ']'
				map[(x1,y1)] = '.'
				map[(x2,y2)] = '.'
			case '<':
				map[(x1-1,y1)] = '['
				map[(x2-1,y2)] = ']'
				map[(x2,y2)] = '.'
			case '>':
				map[(x1+1,y1)] = '['
				map[(x2+1,y2)] = ']'
				map[(x1,y1)] = '.'

		return True
	else:
		return False
	

def do1(map, moves):
	currentPos = [x for x in map.keys() if map[x] == '@'][0]

	for move in moves:
		x,y = currentPos
		match move:
			case '^':
				possibleNewPos = (x, y-1)
			case 'v':
				possibleNewPos = (x, y+1)
			case '<':
				possibleNewPos = (x-1, y)
			case '>':
				possibleNewPos = (x+1, y)
		match map[possibleNewPos]:
			case '#':
				continue
			case '.':
				map[currentPos] = '.'
				currentPos = possibleNewPos
				map[currentPos] = '@'
			case 'O':
				if push(possibleNewPos, move, map):
					map[currentPos] = '.'
					currentPos = possibleNewPos
					map[currentPos] = '@'

	boxPositions = [100 * y + x for (x,y) in map.keys() if map[(x,y)] == 'O']

	return sum(boxPositions)

def do2(map, moves):
	currentPos = [x for x in map.keys() if map[x] == '@'][0]
	
	for move in moves:
		x,y = currentPos
		match move:
			case '^':
				possibleNewPos = (x, y-1)
			case 'v':
				possibleNewPos = (x, y+1)
			case '<':
				possibleNewPos = (x-1, y)
			case '>':
				possibleNewPos = (x+1, y)
		match map[possibleNewPos]:
			case '#':
				continue
			case '.':
				map[currentPos] = '.'
				currentPos = possibleNewPos
				map[currentPos] = '@'
			case '[':
				newMap = copy.deepcopy(map)
				boxPos1X,boxPos1Y = possibleNewPos
				if pushBigBox([possibleNewPos,(boxPos1X+1,boxPos1Y)], move, newMap):
					map = newMap
					map[currentPos] = '.'
					currentPos = possibleNewPos
					map[currentPos] = '@'
			case ']':
				newMap = copy.deepcopy(map)
				boxPos1X,boxPos1Y = possibleNewPos
				if pushBigBox([(boxPos1X-1,boxPos1Y),possibleNewPos], move, newMap):
					map = newMap
					map[currentPos] = '.'
					currentPos = possibleNewPos
					map[currentPos] = '@'

	boxPositions = [100 * y + x for (x,y) in map.keys() if map[(x,y)] == '[']

	return sum(boxPositions)

def do():
	strInput = readInputFile(15)

	mapInput,moveInput = strInput.split('\n\n')
	map1 = createMap1(mapInput)
	map2 = createMap2(mapInput)
	moves = createMoves(moveInput)

	print(do1(map1, moves))
	print(do2(map2, moves))

	print('done')


do()