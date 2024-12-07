from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt
import re
import itertools

def calculateResults(result, parts, combinations):

	for combination in combinations:
			i = 0
			calculatedResult = parts[0]
			while i < len(combination):
				match (combination[i]):
					case '+':
						calculatedResult = calculatedResult + parts[i + 1]
					case '*':
						calculatedResult = (calculatedResult) * parts[i + 1]
					case '|':
						calculatedResult = int(str(calculatedResult) + str(parts[i + 1]))
				i = i + 1
			if calculatedResult == result:
				return result				

	return 0

def do1And2(splitInput):
	possibleCalculations1 = 0
	possibleCalculations2 = 0
	
	for line in splitInput:
		match = re.search('(\d+): (.+)', line)
		result = int(match.groups()[0]) 
		parts = convertToInt(match.groups()[1].split(' '))

		combinations1 = itertools.product('+*', repeat=len(parts) - 1)
		combinations2 = itertools.product('+*|', repeat=len(parts) - 1)
		
		possibleCalculations1 = possibleCalculations1 + calculateResults(result, parts, combinations1)
		possibleCalculations2 = possibleCalculations2 + calculateResults(result, parts, combinations2)

	return possibleCalculations1, possibleCalculations2

def do():
	strInput = readInputFile(7)

	splitInput = strInput.split('\n')

	print(do1And2(splitInput))
	
	print('done')


do()