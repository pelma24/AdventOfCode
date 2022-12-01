from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt

def calculateElfCalories(splitInput):
	elfCalories = []
	
	for elf in splitInput:
		calories = convertToInt(elf.split('\n'))
		elfCalories.append(sum(calories))	
	
	return elfCalories

def do1(splitInput):
	elfCalories = calculateElfCalories(splitInput)
	return max(elfCalories)

def do2(splitInput):
	elfCalories = calculateElfCalories(splitInput)
	elfCalories.sort(reverse=True)
	
	return sum(elfCalories[0:3])

def do():
	strInput = readInputFile(1)

	splitInput = strInput.split('\n\n')
	
	print(do1(splitInput))
	print(do2(splitInput))

	print('done')


do()