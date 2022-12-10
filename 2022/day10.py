from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt

image = []

def do1(splitInput):
	signalStrengths = []
	cycle = 0
	x = 1
	for line in splitInput:
		cycle += 1
		if cycle == 20 or (cycle-20) % 40 == 0:
			signalStrengths.append(x * cycle)
		match line.split(' '):
			case ['addx', value]:
				cycle += 1
				if cycle == 20 or (cycle-20) % 40 == 0:
					signalStrengths.append(x * cycle)
				x = x + int(value)
	
	return sum(signalStrengths)

def do2(splitInput):
	spritePos = 1
	cycle = 0
	for line in splitInput:
		cycle += 1
		draw(spritePos, cycle)
		match line.split(' '):
			case ['addx', value]:
				cycle += 1
				draw(spritePos, cycle)
				spritePos += int(value)
	
	for line in image:
		print(line)
	return 'done'

def draw(spritePos, cycle):
	line = int((cycle - 1) / 40)
	if len(image) < line + 1:
		image.append(['.' for x in range(40)])
	position = (cycle - 1) % 40
	if position in [spritePos-1,spritePos,spritePos+1]:
		image[line][position] = '#'

def do():
	strInput = readInputFile(10)

	splitInput = strInput.split('\n')

	print(do1(splitInput))
	print(do2(splitInput))

	print('done')


do()