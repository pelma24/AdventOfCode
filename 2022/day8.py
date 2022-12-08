from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt

def do1(splitInput):
	visibleTrees = 0
	for linePos,line in enumerate(splitInput):
		for position,_ in enumerate(line):
			if onlySmallerTrees(linePos,position,splitInput):
				visibleTrees += 1
	return visibleTrees

def do2(splitInput):
	scenicScores = []

	for linePos,line in enumerate(splitInput):
		for position,_ in enumerate(line):
			scenicScores.append(calculateScenicScore(linePos,position,splitInput))

	return max(scenicScores)

def onlySmallerTrees(linePos, position, map):
	tree = map[linePos][position]
	
	#left
	otherTrees = [x for x in map[linePos][0:position] if x >= tree]
	if not otherTrees:
		return True

	#right
	otherTrees = [x for x in map[linePos][position + 1:] if x >= tree]
	if not otherTrees:
		return True

	#up
	otherTrees = [x[position] for x in map[0:linePos] if x[position] >= tree]
	if not otherTrees:
		return True

	#down
	otherTrees = [x[position] for x in map[linePos+1:] if x[position] >= tree]
	if not otherTrees:
		return True

def calculateScenicScore(linePos,position,map):
	tree = map[linePos][position]
	
	#right
	scoreRight = 0
	for i in range(position + 1, len(map[linePos])):
		scoreRight += 1
		if map[linePos][i] >= tree:
			break
	
	#left
	scoreLeft = 0
	for i in range(position - 1, -1, -1):
		scoreLeft += 1
		if map[linePos][i] >= tree:
			break
	
	#down
	scoreDown = 0
	for i in range(linePos + 1, len(map)):
		scoreDown += 1
		if map[i][position] >= tree:
			break
	
	#up
	scoreUp = 0
	for i in range(linePos - 1, -1, -1):
		scoreUp += 1
		if map[i][position] >= tree:
			break
	
	return scoreRight * scoreLeft * scoreDown * scoreUp

def do():
	strInput = readInputFile(8)

	splitInput = strInput.split('\n')

	print(do1(splitInput))
	print(do2(splitInput))

	print('done')


do()