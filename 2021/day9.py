from types import CodeType
from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt

def do1(splitInput):
	map, _ = generateMap(splitInput)
	lowPoints = []
	
	for lineNumber,line in enumerate(map):
		for position,height in enumerate(line):
			if height == 9:
				continue
			if line[position - 1] <= height:
				continue
			if line[position + 1] <= height:
				continue
			if map[lineNumber - 1][position] <= height:
				continue
			if map[lineNumber + 1][position] <= height:
				continue
			lowPoints.append(height)
	
	riskLevels = [x + 1 for x in lowPoints]
	
	return sum(riskLevels)

def do2(splitInput):
	map,bassins = generateMap(splitInput)
	
	bassinNumber = 0
	for lineNumber,line in enumerate(map):
		for position,height in enumerate(line):
			if height == 9:
				continue
			if bassins[lineNumber][position] != -1:
				continue
			search(lineNumber, position, map, bassins, bassinNumber)
			bassinNumber += 1

	count = {}
	for i in range(bassinNumber):
		sumI = 0
		for line in bassins:
			sumI += len([x for x in line if x == i])
		count[i] = sumI
	
	maxBassins = [x for x in sorted(count.values(), reverse=True)][0:3]

	return maxBassins[0] * maxBassins[1] * maxBassins[2]

def generateMap(splitInput):
	map = []
	bassins = []
	map.append([9] + [9 for x in splitInput[0]] + [9])
	bassins.append([-1] + [-1 for x in splitInput[0]] + [-1])
	for line in splitInput:
		bassinLine = [-1] + [-1 for x in line] + [-1]
		intLine = [9] + convertToInt(line) + [9]
		map.append(intLine)
		bassins.append(bassinLine)
	map.append([9] + [9 for x in splitInput[0]] + [9])
	bassins.append([-1] + [-1 for x in splitInput[0]] + [-1])

	return (map,bassins)

def search(line, position, map, bassins, bassinNumber):
	currentHeight = map[line][position]
	while currentHeight != 9:
		if bassins[line][position] != -1 and bassins[line][position] != bassinNumber:
			print('Something is wrong')
			return		
		if bassins[line][position] == bassinNumber:
			return
		bassins[line][position] = bassinNumber
		search(line - 1, position, map, bassins, bassinNumber)
		search(line + 1, position, map, bassins, bassinNumber)
		search(line, position - 1, map, bassins, bassinNumber)
		search(line, position + 1, map, bassins, bassinNumber)

def do():
	strInput = readInputFile(9)

	splitInput = strInput.split('\n')

	print(do1(splitInput))
	print(do2(splitInput))

	print('done')


do()