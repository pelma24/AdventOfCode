from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt
from collections import defaultdict

def createMap(mapInput):
	map = {}

	for y,line in enumerate(mapInput):
		for x,value in enumerate(line):
			map[(x,y)] = value
			if value == 'E':
				end = (x,y)
			elif value == 'S':
				start = (x,y)

	return map,start,end

def getNeighbors(position,map):
	x,y = position
	neighbors = []

	for xdiff,ydiff in [(-1,0), (1,0), (0,-1), (0,1)]:
		possibleNeighbor = (x+xdiff,y+ydiff)
		if possibleNeighbor in map.keys() and map[possibleNeighbor] != '#':
			neighbors.append(possibleNeighbor)

	return neighbors

def do1(map, start, end):
	visited = {start:None}
	queue = [start]
	while queue:
		currentPos = queue.pop(0)
		if currentPos == end:
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
	
	cheats = defaultdict(list)
	length = len(path)

	for position,(x,y) in enumerate(path):
		followingSteps = path[position + 1:]
		for otherPosition,(xother,yother) in enumerate(followingSteps):
			cheat = False
			if (x - xother) == 2 and y == yother and (x-1,y) not in path :
				cheat = True
			elif (y - yother) == 2 and x == xother and (x,y-1) not in path:
				cheat = True
			elif (xother-x) == 2 and y == yother and (xother-1,y) not in path:
				cheat = True
			elif (yother - y) == 2 and x == xother and (x,yother-1) not in path:
				cheat = True
			if cheat:
				newLength = len(path[0:position]) + len(path[position + otherPosition:])
				cheats[(x,y)].append(length - newLength - 1)
	
	count = 0
	for cheatPos in cheats.keys():
		for timeSaved in cheats[cheatPos]:
			if timeSaved > 99:
				count += 1
	return count

def do2(splitInput):
	return 'done'

def do():
	strInput = readInputFile(20)

	map,start,end = createMap(strInput.split('\n'))

	print(do1(map,start,end))
	print(do2(strInput))

	print('done')


do()