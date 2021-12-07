from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt

def do1(crabs):
	fuelSum = 0
	minFuelSum = 10000000

	for i in range(10000):
		fuelSum = 0
		for crab in crabs:
			fuel = abs(i - crab)
			fuelSum += fuel
		if fuelSum < minFuelSum:
			minFuelSum = fuelSum
	
	return minFuelSum

def do2(splitInput):
	return 'done'

def do():
	strInput = readInputFile(7)
	#strInput = readExampleInput(7)

	splitInput = strInput.split(',')
	intInput = convertToInt(splitInput)

	print(do1(intInput))
	print(do2(intInput))

	print('done')


do()