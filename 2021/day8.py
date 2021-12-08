from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt

def do1(splitInput):
	uniqueDigits = 0

	for line in splitInput:
		input,output = line.split('|')

		outputDigits = output.split(' ')

		for digit in outputDigits:
			if len(digit) in [2, 3, 4, 7]:
				uniqueDigits += 1
	
	return uniqueDigits

def do2(splitInput):
	
	return 'done'

def do():
	strInput = readInputFile(8)
	strInput = readExampleInput(8)

	splitInput = strInput.split('\n')

	print(do1(splitInput))
	print(do2(splitInput))

	print('done')


do()