from collections import defaultdict
from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt


def do1(strInput):
	distances = defaultdict(lambda: 1000)
	unvisited = []
	visited = []
	
	startingPos,endPos,heightMap = createHeightMap(strInput.split('\n'))

	distances[startingPos] = 0
	unvisited.append((startingPos))

	findShortestPath(heightMap, visited, unvisited, distances)
	
	return distances[endPos]

def do2(strInput):
	_,endPos,heightMap = createHeightMap(strInput.split('\n'))
	
	startingPositions = []
	for lineNumber,line in enumerate(heightMap):
		for index,position in enumerate(line):
			if position == ord('a'):
				startingPositions.append((lineNumber,index))

	distancesToDestination = []

	for startingPosition in startingPositions:
		unvisited = []
		visited = []
		distances = defaultdict(lambda: 1000)
		distances[startingPosition] = 0
		unvisited.append(startingPosition)
		findShortestPath(heightMap, visited, unvisited, distances)
		distancesToDestination.append(distances[endPos])

	return min(distancesToDestination)

def createHeightMap(map):
	for lineNumber,line in enumerate(map):
		for index,position in enumerate(line):
			if position == 'S':
				startingPos = (lineNumber,index)
			elif position == 'E':
				endPos = (lineNumber, index)
	
	heightMap = [[ord(x) for x in y] for y in map]
	heightMap[startingPos[0]][startingPos[1]] = ord('a')
	heightMap[endPos[0]][endPos[1]] = ord('z')

	return (startingPos, endPos, heightMap)

def findShortestPath(heightMap, visited, unvisited, distances):
	while unvisited:
		currentPos = None
		currentDistance = 0
		for position in unvisited:
			if currentPos == None:
				currentPos = position
				currentDistance = distances[position]
			elif distances[position] < distances[currentPos]:
				currentPos = position
				currentDistance = distances[position]
		
		neighbors = getPossibleNeighbors(currentPos, heightMap)
		for neighbor in neighbors:
			if neighbor not in visited and neighbor not in unvisited:
				unvisited.append(neighbor)
			if distances[neighbor] > currentDistance + 1:
				distances[neighbor] = currentDistance + 1
		
		visited.append(currentPos)
		unvisited.remove(currentPos)

def getPossibleNeighbors(position, map):
	possibleNeighbors = []
	line,index = position
	currentHeight = map[line][index]
	if line - 1 >= 0 and map[line-1][index] <= currentHeight + 1:
		possibleNeighbors.append((line-1,index))
	if line + 1 < len(map) and map[line+1][index] <= currentHeight + 1:
		possibleNeighbors.append((line+1,index))
	if index + 1 < len(map[0]) and map[line][index+1] <= currentHeight + 1:
		possibleNeighbors.append((line,index+1))
	if index - 1 >= 0 and map[line][index-1] <= currentHeight + 1:
		possibleNeighbors.append((line,index-1))
	
	return possibleNeighbors

def do():
	strInput = readInputFile(12)

	print(do1(strInput))
	print(do2(strInput))

	print('done')


do()