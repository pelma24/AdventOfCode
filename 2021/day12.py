from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt
from collections import defaultdict

def do1(splitInput):
	paths = preparePaths(splitInput)
	ways = findPossibleWays(paths, 'start', 'end', [])
	return len(ways)

def do2(splitInput):
	paths = preparePaths(splitInput)

	maxAmount = {}
	lowerKeys = [x for x in paths.keys() if x.islower()]
	for key in lowerKeys:
		maxAmount[key] = 1

	allWays = []
	for key in lowerKeys:
		if key == 'start' or key == 'end':
			continue
		maxAmount[key] = 2
		ways = findPossibleWays2(paths, 'start', 'end', [], maxAmount)
		for way in ways:
			if way not in allWays:
				allWays.append(way)
		maxAmount[key] = 1
	return len(allWays)

def preparePaths(splitInput):
	paths = defaultdict(lambda: set())
	
	for line in splitInput:
		first,second = line.split('-')
		firstSet = {first}
		secondSet = {second}
		paths[first] = paths[first].union(secondSet)
		paths[second]= paths[second].union(firstSet)
	
	return paths

def findPossibleWays(paths, start, end, path):
	path = path + [start]
	if start == end:
		return [path]

	newPaths = []
	for connected in paths[start]:
		if connected not in path or connected.isupper():
			possiblePaths = findPossibleWays(paths, connected, end, path)
			for possiblePath in possiblePaths:
				newPaths.append(possiblePath)
	return newPaths

def findPossibleWays2(paths, start, end, path, maxAmount):
	path = path + [start]
	if start == end:
		return [path]

	newPaths = []
	for connected in paths[start]:
		if connected not in path or connected.isupper() or path.count(connected) < maxAmount[connected]:
			possiblePaths = findPossibleWays2(paths, connected, end, path, maxAmount)
			for possiblePath in possiblePaths:
				newPaths.append(possiblePath)
	return newPaths

def do():
	strInput = readInputFile(12)

	splitInput = strInput.split('\n')

	print(do1(splitInput))
	print(do2(splitInput))

	print('done')


do()