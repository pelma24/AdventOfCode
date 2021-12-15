from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt
from collections import defaultdict
from copy import deepcopy

def do1(splitInput):
	
	costs = getSums(splitInput)

	return costs[(len(splitInput[0]) - 1, len(splitInput) - 1)]

def do2(splitInput):
	newMap = generateBiggerMap(splitInput)

	costs = getSums(newMap)

	return costs[(len(newMap[0]) - 1, len(newMap) - 1)]

def generateBiggerMap(splitInput):
	newLines = []
	for line in splitInput:
		line = convertToInt(line)
		newPart = deepcopy(line)
		for i in range(4):
			newPart = [x + 1 if x < 9 else 1 for x in newPart]
			line += newPart
		newLines.append(line)

	newMap = deepcopy(newLines)
	for i in range(1, 5):
		for line in newLines:
			newMap.append([x + i if x + i < 10 else (x + i) - 9 for x in line])

	return newMap			

def getSums(splitInput):
	costs = defaultdict(lambda: 1000000000)
	costs[(0,0)] = 0	
	changed = True

	while(changed):
		changed = False
		for lineNumber,line in enumerate(splitInput):
			for position,risk in enumerate(line):
				if lineNumber == 0 and position == 0:
					continue
				left = (lineNumber, position - 1)
				right = (lineNumber, position + 1)
				up = (lineNumber - 1, position)
				down = (lineNumber + 1, position)

				minNeighborCost = 1000000000
				for neighbor in [left, right, up, down]:
					minNeighborCost = min(minNeighborCost, costs[neighbor])

				newCosts = int(risk) + minNeighborCost
				if newCosts < costs[(lineNumber, position)]:
					changed = True
					costs[(lineNumber, position)] = newCosts
	return costs

def do():
	strInput = readInputFile(15)

	splitInput = strInput.split('\n')

	print(do1(splitInput))
	print(do2(splitInput))

	print('done')


do()