from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt

def do1(splitInput):
	fullyContained = 0
	for pair in splitInput:
		elf1Assignment,elf2Assignment = getElvesAssignments(pair)
		intersection = elf1Assignment.intersection(elf2Assignment)
		if len(intersection) == len(elf1Assignment) or len(intersection) == len(elf2Assignment):
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
	elf1,elf2 = pair.split(',')
	elf1Start,elf1Stop = [int(x) for x in elf1.split('-')]
	elf2Start,elf2Stop = [int(x) for x in elf2.split('-')]
	elf1Assignment = set([x for x in range(elf1Start, elf1Stop + 1)])
	elf2Assignment = set([x for x in range(elf2Start, elf2Stop + 1)])

	return (elf1Assignment,elf2Assignment)


def do():
	strInput = readInputFile(4)

	splitInput = strInput.split('\n')

	print(do1(splitInput))
	print(do2(splitInput))

	print('done')


do()