from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt
from copy import deepcopy
from collections import defaultdict

def do1(splitInput):

	fishes = growFishes(splitInput, 80)
	sumOfFishes = sum([x for x in fishes.values()])

	return sumOfFishes

def do2(splitInput):
	fishes = growFishes(splitInput, 256)
	sumOfFishes = sum([x for x in fishes.values()])

	return sumOfFishes

def growFishes(splitInput, days):
	fishes = defaultdict(lambda: 0)

	for fish in splitInput:
		fishes[fish] += 1
	
	for i in range(days):
		newFishes = defaultdict(lambda: 0)
		for key,value in fishes.items():
			if key == 0:
				newFishes[8] += value
				newFishes[6] += value
			else:
				newFishes[key - 1] += value
		fishes = deepcopy(newFishes)
	
	return fishes

def do():
	strInput = readInputFile(6)

	splitInput = strInput.split(',')
	intInput = convertToInt(splitInput)

	print(do1(intInput))
	print(do2(intInput))

	print('done')


do()