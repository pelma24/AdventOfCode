from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt
from copy import deepcopy

def do1(splitInput):
	map = []
	for line in splitInput:
		newLine = [x for x in line]
		map.append(newLine)	
	
	mapLength = len(map)

	newMap = deepcopy(map)
	moving = True
	steps = 0
	southfacing = True
	while moving or not southfacing:
		southfacing = not southfacing
		moving = False
		if not southfacing:
			steps += 1
		for lineNumber,line in enumerate(map):
			lineLength = len(line)
			for position,value in enumerate(line):
				match value:
					case '.':
						continue
					case 'v':
						if southfacing:
							neighborLine = (lineNumber + 1) % mapLength
							if map[neighborLine][position] == '.':
								newMap[neighborLine][position] = 'v'
								newMap[lineNumber][position] = '.'
								moving = True
					case '>':
						if not southfacing:
							neighborPos = (position + 1) % lineLength
							if line[neighborPos] == '.':
								newMap[lineNumber][neighborPos] = '>'
								newMap[lineNumber][position] = '.'
								moving = True
		map = deepcopy(newMap)		
	
	return steps

def do2():
	return 'Nothing to do'

def do():
	strInput = readInputFile(25)

	splitInput = strInput.split('\n')

	print(do1(splitInput))
	print(do2())

	print('done')


do()