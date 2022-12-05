from copy import deepcopy
from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt
import re

inputArrangement = [['N','T','B','S','Q','H','G','R'], ['J','Z','P','D','F','S','H'], ['V','H','Z'], ['H','G','F','J','Z','M'], ['R','S','M','L','D','C','Z','T'], ['J','Z','H','V','W','T','M'], ['Z','L','P','F','T'], ['S','W','V','Q'], ['C','N','D','T','M','L','H','W']]


def do1(splitInput):
	arrangement = deepcopy(inputArrangement)
	for line in splitInput:
		match = re.match('move (?P<number>\d+) from (?P<start>\d) to (?P<end>\d)', line)
		start = int(match.group('start')) - 1
		number = int(match.group('number'))
		end = int(match.group('end')) - 1
	
		for _ in range(number):
			arrangement[end].insert(0, arrangement[start].pop(0))
		
	result = ''
	for part in arrangement:
		result = result + part[0]

	return result

def do2(splitInput):
	arrangement = deepcopy(inputArrangement)	
	for line in splitInput:
		match = re.match('move (?P<number>\d+) from (?P<start>\d) to (?P<end>\d)', line)
		start = int(match.group('start')) - 1
		number = int(match.group('number'))
		end = int(match.group('end')) - 1

		movedParts = arrangement[start][0:number]
		arrangement[start] = arrangement[start][number:]
		arrangement[end] = movedParts + arrangement[end] 
	
	result = ''
	for part in arrangement:
		result = result + part[0]

	return result

def do():
	strInput = readInputFile(5)

	splitInput = strInput.split('\n')
	
	print(do1(splitInput))
	print(do2(splitInput))

	print('done')


do()