from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt

def do1(splitInput):
	horizontal = 0
	depth = 0

	for line in splitInput:
		direction,value = line.split(' ')
		value = int(value)

		match direction:
			case 'forward':
				horizontal += value
			case 'up':
				depth -= value
			case 'down':
				depth += value
	
	return horizontal * depth

def do2(splitInput):
	horizontal = 0
	depth = 0
	aim = 0
	
	for line in splitInput:
		direction,value = line.split(' ')
		value = int(value)

		match direction:
			case 'forward':
				horizontal += value
				depth += aim * value
			case 'up':
				aim -= value
			case 'down':
				aim += value
	
	return horizontal * depth

def do():
	strInput = readInputFile(2)

	splitInput = strInput.split('\n')

	print(do1(splitInput))
	print(do2(splitInput))

	print('done')


do()