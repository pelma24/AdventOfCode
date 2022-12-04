from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt

def do1(splitInput):
	fullyContained = 0
	for pair in splitInput:
		elves = pair.split(',')
		assignment = set()
		for elf in elves:
			elfStart,elfStop = [int(x) for x in elf.split('-')]
			elfAssignment = set([x for x in range(elfStart, elfStop + 1)])
			if not assignment:
				assignment = elfAssignment
				continue
			intersection = elfAssignment.intersection(assignment)
			if len(intersection) == len(assignment) or len(intersection) == len(elfAssignment):
				fullyContained += 1
	return fullyContained

def do2(splitInput):
	overlaps = 0
	for pair in splitInput:
		elves = pair.split(',')
		assignment = set()
		for elf in elves:
			elfStart,elfStop = [int(x) for x in elf.split('-')]
			elfAssignment = set([x for x in range(elfStart, elfStop + 1)])
			if not assignment:
				assignment = elfAssignment
				continue
			if elfAssignment.intersection(assignment):
				overlaps += 1
	return overlaps

def do():
	strInput = readInputFile(4)

	splitInput = strInput.split('\n')

	print(do1(splitInput))
	print(do2(splitInput))

	print('done')


do()