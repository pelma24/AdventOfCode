from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt

def do1(splitInput):
	horizontal = 0
	depth = 0

	for line in splitInput:
		direction,value = line.split(' ')

		match direction:
			case 'forward':
				horizontal += int(value)
			case 'up':
				depth -= int(value)
			case 'down':
				depth += int(value)
	
	return horizontal * depth

def do2(splitInput):
	horizontal = 0
	depth = 0
	aim = 0
	
	for line in splitInput:
		direction,value = line.split(' ')

		match direction:
			case 'forward':
				horizontal += int(value)
				depth += aim * int(value)
			case 'up':
				aim -= int(value)
			case 'down':
				aim += int(value)
	
	return horizontal * depth

def do():
	strInput = readInputFile(2)

	splitInput = strInput.split('\n')

	print(do1(splitInput))
	print(do2(splitInput))

	print('done')


do()