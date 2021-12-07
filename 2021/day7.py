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

def do2(crabs):
	steps = [i for i in range(1,10000)]
	fuelNeeded = [sum(steps[0:i]) for i in range(1,10000)]
	minFuelSum = 10000000000

	for i in range(10000):
		fuelSum = 0
		for crab in crabs:
			stepsNeeded = abs(i - crab)
			fuel = fuelNeeded[stepsNeeded - 1]
			fuelSum += fuel
		if fuelSum < minFuelSum:
			minFuelSum = fuelSum
	
	return minFuelSum
	
def do():
	strInput = readInputFile(7)

	splitInput = strInput.split(',')
	intInput = convertToInt(splitInput)

	print(do1(intInput))
	print(do2(intInput))

	print('done')


do()