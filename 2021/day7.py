from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt

def do1(crabs):
	fuelSum = 0
	minFuelSum = 10000000

	for i in range(min(crabs), max(crabs) + 1):
		fuelSum = 0
		for crab in crabs:
			fuel = abs(i - crab)
			fuelSum += fuel
		minFuelSum = min(minFuelSum, fuelSum)
	
	return minFuelSum

def do2(crabs):
	maxCrabs = max(crabs) + 1
	crabRange = range(min(crabs), maxCrabs)
	steps = [i for i in range(1, maxCrabs)]
	fuelNeeded = [sum(steps[0:i]) for i in range(1, maxCrabs)]
	minFuelSum = 10000000000

	for i in crabRange:
		fuelSum = 0
		for crab in crabs:
			stepsNeeded = abs(i - crab)
			fuel = fuelNeeded[stepsNeeded - 1]
			fuelSum += fuel
		minFuelSum = min(minFuelSum, fuelSum)
	
	return minFuelSum
	
def do():
	strInput = readInputFile(7)

	splitInput = strInput.split(',')
	intInput = convertToInt(splitInput)

	print(do1(intInput))
	print(do2(intInput))

	print('done')


do()