from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt

def createMap(strInput):
	map = {}

	for y,line in enumerate(strInput.split('\n')):
		for x,value in enumerate(line):
			map[(x,y)] = value

	return map

def findRegion(pos, map):
	value = map[pos]
	region = []
	workingList = set()
	workingList.add(pos)
	alreadyVisited = []

	while len(workingList) != 0:
		currentItem = workingList.pop()
		x,y = currentItem
		region.append(currentItem)
		alreadyVisited.append(currentItem)

		for xdiff,ydiff in [(-1,0), (1,0), (0,-1), (0,1)]:
			possibleNeighbor = (x+xdiff,y+ydiff)
			if possibleNeighbor not in alreadyVisited and map.get(possibleNeighbor, 0) == value:
				workingList.add(possibleNeighbor)

	return region

def calculatePerimeter(plot, map):
	x,y = plot
	value = map[plot]
	perimeter = 0
	for xdiff,ydiff in [(-1,0), (1,0), (0,-1), (0,1)]:
		possibleNeighbor = (x+xdiff,y+ydiff)
		if map.get(possibleNeighbor, 0) != value:
			perimeter += 1

	return perimeter

def do1(map):

	regions = {}
	count = 0

	for x,y in map.keys():
		if not any((x,y) in regions[a] for a in regions.keys()):
			regions[count] = findRegion((x,y), map)
			count += 1
	
	result = 0

	for region in regions.keys():
		area = len(regions[region])
		perimeter = 0
		for plot in regions[region]:
			perimeter += calculatePerimeter(plot, map)
		
		result += area * perimeter
	
	return result

def do2(splitInput):
	return 'done'

def do():
	strInput = readInputFile(12)
	#strInput = readExampleInput(12)

	map = createMap(strInput)

	print(do1(map))
	print(do2(strInput))

	print('done')


do()