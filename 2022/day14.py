from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt

def do1(splitInput):
	map = buildWalls(splitInput)
	sand = set()

	rested,restingPos = letTheSandFall(map, sand)
	while rested:
		sand.add(restingPos)
		rested,restingPos = letTheSandFall(map, sand)

	return len(sand)

def do2(splitInput):
	map = buildWalls(splitInput)
	sand = set()

	highestY = max([x[1] for x in map])
	# add floor
	for x in range(-1000, 1000+1):
		map.add((x, highestY + 2))

	rested,restingPos = letTheSandFall(map, sand)
	while rested:
		sand.add(restingPos)
		if restingPos == (500,0):
			break
		rested,restingPos = letTheSandFall(map, sand)

	return len(sand)

def buildWalls(splitInput):
	map = set()
	for line in splitInput:
		parts = line.split(' -> ')
		for i in range(1, len(parts)):
			startX,startY = [int(x) for x in parts[i].split(',')]
			endX,endY = [int(x) for x in parts[i-1].split(',')]

			if startY == endY:
				x = sorted([startX, endX])
				for j in range(x[0], x[1] + 1):
					map.add((j, startY))
			else:
				y = sorted([startY, endY])
				for j in range(y[0], y[1] + 1):
					map.add((startX, j))
		
	return map

def letTheSandFall(map, sand):
	boundaryLeft = min([x[0] for x in map])
	boundaryRight = max([x[0] for x in map])
	
	sandStart = (500,0)
	position = sandStart
	while True:
		newPosition = (position[0], position[1] + 1)
		if newPosition in map or newPosition in sand:
			# diagonally left
			if (newPosition[0] - 1, newPosition[1]) in map or (newPosition[0] - 1, newPosition[1]) in sand:
				# diagonally right
				if (newPosition[0] + 1, newPosition[1]) in map or (newPosition[0] + 1, newPosition[1]) in sand:
					return True,position
				else:
					position = (position[0] + 1, position[1] + 1)
					if position[0] > boundaryRight:
						return False,(0,0)
					continue
			else:
				position = (position[0] - 1, position[1] + 1)
				if position[0] < boundaryLeft:
						return False,(0,0)
				continue
		else:
			position = newPosition

def do():
	strInput = readInputFile(14)

	splitInput = strInput.split('\n')
	
	print(do1(splitInput))
	print(do2(splitInput))

	print('done')


do()