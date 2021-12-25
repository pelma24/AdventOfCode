from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt
from copy import deepcopy

def do1(splitInput):
	map = []
	for line in splitInput:
		newLine = [x for x in line]
		map.append(newLine)	
	
	newMap = deepcopy(map)
	moving = True
	steps = 0
	
	while moving:
		moving = False
		steps += 1
		for lineNumber,line in enumerate(map):
			for position,value in enumerate(line):
				match value:
					case '.':
						continue
					case 'v':
						continue
					case '>':
						neighborPos = position + 1
						if neighborPos == len(line):
							neighborPos = 0
						if line[neighborPos] == '.':
							newMap[lineNumber][neighborPos] = '>'
							newMap[lineNumber][position] = '.'
							moving = True
		map = deepcopy(newMap)
		# again for south-facing
		for lineNumber,line in enumerate(map):
			for position,value in enumerate(line):
				match value:
					case '.':
						continue
					case 'v':
						neighborLine = lineNumber + 1
						if neighborLine == len(map):
							neighborLine = 0
						if map[neighborLine][position] == '.':
							newMap[neighborLine][position] = 'v'
							newMap[lineNumber][position] = '.'
							moving = True
					case '>':
						continue

		map = deepcopy(newMap)
	
	return steps

def do2(splitInput):
	return 'Nothing to do'

def do():
	strInput = readInputFile(25)

	splitInput = strInput.split('\n')

	print(do1(splitInput))
	print(do2(splitInput))

	print('done')


do()