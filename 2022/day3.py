from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt

def do1(splitInput):
	prioritySum = 0
	for rucksack in splitInput:
		firstCompartment = rucksack[0:int(len(rucksack)/2)]
		secondCompartment = rucksack[int(len(rucksack)/2):]

		sameType = [x for x in firstCompartment if x in secondCompartment][0]
		prioritySum += calculatePriorityValue(sameType)
	return prioritySum

def do2(splitInput):
	prioritySum = 0

	groups = [splitInput[i:i+3] for i in range(0, len(splitInput), 3)]
	for elf1,elf2,elf3 in groups:
		sameType = [x for x in elf1 if x in elf2 and x in elf3][0]
		prioritySum += calculatePriorityValue(sameType)
	return prioritySum

def calculatePriorityValue(item):
	if 'a' <= item <= 'z':
		return ord(item) - ord('a') + 1
	elif 'A' <= item <= 'Z':
		return ord(item) - ord('A') + 27

def do():
	strInput = readInputFile(3)

	splitInput = strInput.split('\n')

	print(do1(splitInput))
	print(do2(splitInput))

	print('done')


do()