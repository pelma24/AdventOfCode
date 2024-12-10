from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt


def createMap(splitInput):
	map = []
	map.append([-1 for _ in range(len(splitInput) + 2)])
	for line in splitInput:
		map.append([-1] + convertToInt(line) + [-1])
	map.append([-1 for _ in range(len(splitInput) + 2)])
	
	trailheads = []
	for y,line in enumerate(map):
		for x,value in enumerate(line):
			if value == 0:
				trailheads.append((x,y))


	return map,trailheads

def getPossibleNeighbors(value, pos, map):
	x,y = pos
	possibleNeighbors = []
	for xdiff,ydiff in [(-1,0), (1,0), (0,-1), (0,1)]:
		if map[y+ydiff][x+xdiff] == value + 1:
			possibleNeighbors.append((x+xdiff, y+ydiff))

	return possibleNeighbors	

def differentPeaks(value, pos, map):
	
	if value == 9:
		result = set()
		result.add(pos)
		return result

	possibleNeighbors = getPossibleNeighbors(value, pos, map)
	
	ends = set()
	for neighbor in possibleNeighbors:
		ends = ends.union(differentPeaks(value + 1, neighbor, map))

	return ends

def differentPaths(value, pos, map, path):
	if value == 9:
		return [path]
	
	possibleNeighbors = getPossibleNeighbors(value, pos, map)

	paths = []
	for neighbor in possibleNeighbors:
		newPath = path.copy()
		newPath.append(neighbor)
		differentPathsFromNeighbor = differentPaths(value + 1, neighbor, map, newPath)
		for differentPath in differentPathsFromNeighbor:
			paths.append(differentPath)

	return paths

def do1(map, trailheads):
	
	score = 0
	for trailhead in trailheads:
		score = score + len(differentPeaks(0, trailhead, map))

	return score

def do2(map, trailheads):
	
	score = 0
	for trailhead in trailheads:
		score = score + len(differentPaths(0, trailhead, map, [trailhead]))

	return score

def do():
	strInput = readInputFile(10)

	splitInput = strInput.split('\n')

	map, trailheads = createMap(splitInput)

	print(do1(map, trailheads))
	print(do2(map, trailheads))

	print('done')


do()