from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt

def createMap(mapInput, size, countOfBytes):
	map = {}
	for count,value in enumerate(mapInput):
		if count == countOfBytes:
			break
		x,y = value
		map[(x,y)] = '#'

	for x in range(size + 1):
		for y in range(size + 1):
			if (x,y) not in map.keys():
				map[(x,y)] = '.'

	return map

def getNeighbors(position,map):
	x,y = position
	neighbors = []

	for xdiff,ydiff in [(-1,0), (1,0), (0,-1), (0,1)]:
		possibleNeighbor = (x+xdiff,y+ydiff)
		if possibleNeighbor in map.keys() and map[possibleNeighbor] == '.':
			neighbors.append(possibleNeighbor)

	return neighbors

def do1(map, end):
	start = (0,0)
	visited = {start:None}
	
	pathFound = False

	queue = [start]
	while queue:
		currentPos = queue.pop(0)
		if currentPos == end:
			pathFound = True
			path = []
			while currentPos:
				path.append(currentPos)
				currentPos = visited[currentPos]
		else:
			neighbors = getNeighbors(currentPos,map)
			for neighbor in neighbors:
				if neighbor not in visited.keys():
					visited[neighbor] = currentPos
					queue.append(neighbor)
	if pathFound:
		return len(path) - 1
	else:
		return False

def do2(map, end, count, mapInput):
	
	for i in range(count, len(mapInput)):
		newX,newY = mapInput[i]
		map[(newX,newY)] = '#'
		
		if do1(map, end):
			continue
		else:
			return (newX,newY)

	return 'done'

def do():
	strInput = readInputFile(18)
	
	size = 70
	count = 1024

	mapInput = []
	for line in strInput.split('\n'):
		x,y = line.split(',')
		mapInput.append((int(x),int(y)))
	
	map = createMap(mapInput, size, count)

	print(do1(map, (size,size)))
	print(do2(map, (size,size), count, mapInput))

	print('done')


do()