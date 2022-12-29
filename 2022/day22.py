from enum import IntEnum
from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt

class Direction(IntEnum):
	NORTH = 3
	EAST = 0
	SOUTH = 1
	WEST = 2

turnRight = {Direction.NORTH:Direction.EAST, Direction.EAST:Direction.SOUTH, Direction.SOUTH:Direction.WEST, Direction.WEST:Direction.NORTH}
turnLeft = {Direction.NORTH:Direction.WEST, Direction.EAST:Direction.NORTH, Direction.SOUTH:Direction.EAST, Direction.WEST:Direction.SOUTH}

east = {1: lambda x,y: (2,x,0,Direction.EAST), 2: lambda x,y: (5,49-x,49,Direction.WEST), 3: lambda x,y: (2,49,x,Direction.NORTH),4: lambda x,y: (5,x,0,Direction.EAST), 5: lambda x,y: (2,49-x,49,Direction.WEST), 6: lambda x,y: (5,49,x,Direction.NORTH)}
south = {1: lambda x,y: (3,0,y,Direction.SOUTH), 2: lambda x,y: (3,y,49,Direction.WEST), 3: lambda x,y: (5,0,y,Direction.SOUTH),4: lambda x,y: (6,0,y,Direction.SOUTH), 5: lambda x,y: (6,y,49,Direction.WEST), 6: lambda x,y: (2,0,y,Direction.SOUTH)}
north = {1:lambda x,y: (6,y,0,Direction.EAST), 2: lambda x,y: (6,49,y,Direction.NORTH), 3: lambda x,y: (1,49,y,Direction.NORTH), 4: lambda x,y: (3,y,0,Direction.EAST), 5: lambda x,y: (3,49,y,Direction.NORTH),6: lambda x,y: (4,49,y,Direction.NORTH)}
west = {1:lambda x,y: (4,49-x,0,Direction.EAST), 2: lambda x,y: (1,x,49,Direction.WEST), 3: lambda x,y: (4,0,x,Direction.SOUTH), 4: lambda x,y: (1,49-x,0,Direction.EAST), 5: lambda x,y: (4,x,49,Direction.WEST), 6: lambda x,y: (1,0,x,Direction.SOUTH)}

def do1(splitInput):
	mapInput,steps = splitInput

	map = createMap(mapInput)

	startY = min([y for (x,y) in map.keys() if x == 0])
	position = (0,startY)
	direction = Direction.EAST
	length = ''
	for char in steps:
		if char == 'R' or char == 'L':
			position = move(int(length),position,direction,map)
			length = ''
			direction = turn(char, direction)
		else:
			length += char
	position = move(int(length),position,direction,map)

	return 1000 * (position[0] + 1) + 4 * (position[1] + 1) + int(direction)
def do2(splitInput):
	mapInput,steps = splitInput
	
	map,cube = createCube(mapInput)
	position = (1,0,0)
	direction = Direction.EAST
	length = ''
	for char in steps:
		if char == 'R' or char == 'L':
			side,posX,posY,direction = moveCube(int(length),position,direction,map,cube)
			position = (side,posX,posY)
			length = ''
			direction = turn(char, direction)
		else:
			length += char
	side,posX,posY,direction = moveCube(int(length),position,direction,map,cube)

	mapPosX,mapPosY = cube[side][(posX,posY)]
	return 1000 * (mapPosX + 1) + 4 * (mapPosY + 1) + int(direction) 

def createMap(mapInput):
	map = {}
	for lineNumber,line in enumerate(mapInput.split('\n')):
		for position,tile in enumerate(line):
			if not tile == ' ':
				map[(lineNumber,position)] = tile
	return map

def createCube(mapInput):
	map = createMap(mapInput)
	cube = {1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}}

	x = 0
	for j in range(0,50):
		y = 0
		for i in range(50, 100):
			cube[1][x,y] = (j,i)
			y += 1
		y = 0	
		for i in range(100, 150):
			cube[2][x,y] = (j,i)
			y += 1
		x += 1
	x = 0
	for j in range(50,100):
		y = 0
		for i in range(50, 100):
			cube[3][x,y] = (j,i)
			y += 1
		x += 1
	x = 0
	for j in range(100,150):
		y = 0
		for i in range(0,50):
			cube[4][x,y] = (j,i)
			y += 1
		y = 0
		for i in range(50,100):
			cube[5][x,y] = (j,i)
			y += 1
		x += 1
	x = 0
	for j in range(150,200):
		y = 0
		for i in range(0,50):
			cube[6][x,y] = (j,i)
			y += 1
		x += 1

	return map,cube	

def turn(direction, currentDirection):
	if direction == 'R':
		return turnRight[currentDirection]
	else:
		return turnLeft[currentDirection]

def move(steps,position,direction,map):
	currentPos = position
	match direction:
		case Direction.NORTH:
			for _ in range(steps):
				posX,posY = currentPos
				nextPos = (posX - 1, posY)
				if nextPos not in map.keys():
					nextPosX = max([x for (x,y) in map.keys() if y == posY])
					nextPos = (nextPosX,posY)
				if map[nextPos] == '#':
					return currentPos
				else:
					currentPos = nextPos
			return currentPos
		case Direction.EAST:
			for _ in range(steps):
				posX,posY = currentPos
				nextPos = (posX, posY + 1)
				if nextPos not in map.keys():
					nextPosY = min([y for (x,y) in map.keys() if x == posX])
					nextPos = (posX, nextPosY)
				if map[nextPos] == '#':
					return currentPos
				else:
					currentPos = nextPos
			return currentPos
		case Direction.SOUTH:
			for _ in range(steps):
				posX,posY = currentPos
				nextPos = (posX + 1, posY)
				if nextPos not in map.keys():
					nextPosX = min([x for (x,y) in map.keys() if y == posY])
					nextPos = (nextPosX,posY)
				if map[nextPos] == '#':
					return currentPos
				else:
					currentPos = nextPos
			return currentPos
		case Direction.WEST:
			for _ in range(steps):
				posX,posY = currentPos
				nextPos = (posX, posY - 1)
				if nextPos not in map.keys():
					nextPosY = max([y for (x,y) in map.keys() if x == posX])
					nextPos = (posX, nextPosY)
				if map[nextPos] == '#':
					return currentPos
				else:
					currentPos = nextPos
			return currentPos

def moveCube(steps,position,direction,map,cube):
	currentPos = position
	for _ in range(steps):
		match direction:
			case Direction.NORTH:
				side,posX,posY = currentPos
				newSide = side
				nextPosX,nextPosY = (posX - 1, posY)
				if nextPosX < 0:
					newSide,nextPosX,nextPosY,direction = north[side](posX,posY)
				if map[cube[newSide][(nextPosX,nextPosY)]] == '#':
					return side,posX,posY,Direction.NORTH
				else:
					currentPos = (newSide,nextPosX,nextPosY)
			case Direction.EAST:
				side,posX,posY = currentPos
				newSide = side
				nextPosX,nextPosY = (posX, posY + 1)
				if nextPosY > 49:
					newSide,nextPosX,nextPosY,direction = east[side](posX,posY)
				if map[cube[newSide][(nextPosX,nextPosY)]] == '#':
					return side,posX,posY,Direction.EAST
				else:
					currentPos = (newSide,nextPosX,nextPosY)
			case Direction.SOUTH:
				side,posX,posY = currentPos
				newSide = side
				nextPosX,nextPosY = (posX + 1, posY)
				if nextPosX > 49:
					newSide,nextPosX,nextPosY,direction = south[side](posX,posY)
				if map[cube[newSide][(nextPosX,nextPosY)]] == '#':
					return side,posX,posY,Direction.SOUTH
				else:
					currentPos = (newSide,nextPosX,nextPosY)
			case Direction.WEST:
				side,posX,posY = currentPos
				newSide = side
				nextPosX,nextPosY = (posX, posY - 1)
				if nextPosY < 0:
					newSide,nextPosX,nextPosY,direction = west[side](posX,posY)
				if map[cube[newSide][(nextPosX,nextPosY)]] == '#':
					return side,posX,posY,Direction.WEST
				else:
					currentPos = (newSide,nextPosX,nextPosY)
	side,x,y = currentPos
	return side,x,y,direction

def do():
	strInput = readInputFile(22)

	splitInput = strInput.split('\n\n')
	
	print(do1(splitInput))
	print(do2(splitInput))

	print('done')


do()