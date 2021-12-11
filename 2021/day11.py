from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt

def do1(splitInput):
	octopuses = prepareInput(splitInput)
	steps = 100
	sumOfFlashes = 0
	for _ in range(steps):
		octopuses,flashes = flashOctopuses(octopuses)
		sumOfFlashes += flashes

	return sumOfFlashes

def do2(splitInput):
	octopuses = prepareInput(splitInput)
	steps = 0
	flashes = 0
	while flashes < len(splitInput) * len(splitInput[0]):
		steps += 1
		octopuses,flashes = flashOctopuses(octopuses)

	return steps

def flashOctopuses(octopuses):
	#increase energy level
	energyOctopuses = []
	for x in range(len(octopuses)):
		energyOctopuses.append([y + 1 if y != -1 else -1 for y in octopuses[x] ])
	
	flashes = 0
	newFlashes = 1
	flashed = []
	while newFlashes != 0:
		newFlashes = 0
		for lineNumber,line in enumerate(energyOctopuses):
			for position,octopus in enumerate(line):
				if octopus == -1:
					continue
				elif octopus > 9:
					flash(lineNumber, position, energyOctopuses, flashed)
					newFlashes += 1
		flashes += newFlashes

	return energyOctopuses,flashes

def flash(line, position, octopuses, flashed):
	if octopuses[line][position] < 10:
		print('Why are we here?')
		return
	
	octopuses[line][position] = 0
	flashed.append((line, position))

	if octopuses[line-1][position-1] != -1 and (line-1,position-1) not in flashed:
		octopuses[line-1][position-1] += 1
	if octopuses[line-1][position] != -1 and (line-1,position) not in flashed:
		octopuses[line-1][position] += 1
	if octopuses[line-1][position+1] != -1 and (line-1,position+1) not in flashed:
		octopuses[line-1][position+1] += 1
	
	if octopuses[line][position-1] != -1 and (line,position-1) not in flashed:
		octopuses[line][position-1] += 1
	if octopuses[line][position+1] != -1 and (line,position+1) not in flashed:
		octopuses[line][position+1] += 1
	
	if octopuses[line+1][position-1] != -1 and (line+1,position-1) not in flashed:
		octopuses[line+1][position-1] += 1
	if octopuses[line+1][position] != -1 and (line+1,position) not in flashed:
		octopuses[line+1][position] += 1
	if octopuses[line+1][position+1] != -1 and (line+1,position+1) not in flashed:
		octopuses[line+1][position+1] += 1


def prepareInput(splitInput):
	octopuses = []

	octopuses.append([-1] + [-1 for _ in range(len(splitInput[0]))] + [-1])

	for line in splitInput:
		octoLine = [-1] + convertToInt(line) + [-1]
		octopuses.append(octoLine)

	octopuses.append([-1 for _ in range(len(octopuses[0]))])
	
	return octopuses

def do():
	strInput = readInputFile(11)

	splitInput = strInput.split('\n')

	print(do1(splitInput))
	print(do2(splitInput))

	print('done')


do()