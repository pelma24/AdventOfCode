from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt

def do1(splitInput):
	fullyContained = 0
	for pair in splitInput:
		elf1Assignment,elf2Assignment = getElvesAssignments(pair)
		if elf1Assignment.issubset(elf2Assignment) or elf2Assignment.issubset(elf1Assignment):
			fullyContained += 1
	return fullyContained

def do2(splitInput):
	overlaps = 0
	for pair in splitInput:
		elf1Assignment,elf2Assignment = getElvesAssignments(pair)
		if elf1Assignment.intersection(elf2Assignment):
			overlaps += 1
	return overlaps

def getElvesAssignments(pair):
	assignments = []
	for elf in pair.split(','):
		elfStart,elfStop = [int(x) for x in elf.split('-')]
		elfAssignment = set([x for x in range(elfStart, elfStop + 1)])
		assignments.append(elfAssignment)
	return assignments

def do():
	strInput = readInputFile(4)

	splitInput = strInput.split('\n')

	print(do1(splitInput))
	print(do2(splitInput))

	print('done')


do()