from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt

TPositions = set()
tailPositions = set()

def do1(splitInput):
	HPos = (0,0)
	TPos = (0,0)
	TPositions.add(TPos)
	for line in splitInput:
		command,steps = line.split(' ')
		for _ in range(int(steps)):
			match command:
				case 'R':
					HPos = (HPos[0] + 1, HPos[1])
				case 'L':
					HPos = (HPos[0] - 1, HPos[1])
				case 'D':
					HPos = (HPos[0], HPos[1] - 1)
				case 'U':
					HPos = (HPos[0], HPos[1] + 1)
			TPos = updatePos(HPos, TPos)
			TPositions.add(TPos)
	
	
	return len(TPositions)

def do2(splitInput):
	positions = [(0,0) for x in range(10)]
	tailPositions.add(positions[8])
	for line in splitInput:
		command,steps = line.split(' ')
		for _ in range(int(steps)):
			headPos = positions[0]
			match command:
				case 'R':
					positions[0] = (headPos[0] + 1, headPos[1])
				case 'L':
					positions[0] = (headPos[0] - 1, headPos[1])
				case 'D':
					positions[0] = (headPos[0], headPos[1] - 1)
				case 'U':
					positions[0] = (headPos[0], headPos[1] + 1)
			for index,knot in enumerate(positions[1:]):
				positions[index + 1] = updatePos(positions[index], knot)
				tailPositions.add(positions[len(positions) - 1])
	
	return len(tailPositions)



def updatePos(HPos, TPos):
	TPositions.add(TPos)
	#same row or colum
	if TPos[0] == HPos[0]:
		match HPos[1] - TPos[1]:
			case 2:
				TPos = (TPos[0], TPos[1] + 1)
			case -2:
				TPos = (TPos[0], TPos[1] - 1)
	elif TPos[1] == HPos[1]:
		match HPos[0] - TPos[0]:
			case 2:
				TPos = (TPos[0] + 1, TPos[1])
			case -2:
				TPos = (TPos[0] - 1, TPos[1])
	#diagonally
	elif abs(HPos[0] - TPos[0]) + abs(HPos[1] - TPos[1]) == 2:
		return TPos
	else:
		# H is right from T:
		if HPos[0] > TPos[0]:
			if HPos[1] > TPos[1]:
				TPos = (TPos[0] + 1, TPos[1] + 1)
			else:
				TPos = (TPos[0] + 1, TPos[1] - 1)
		else:
			if HPos[1] > TPos[1]:
				TPos = (TPos[0] - 1, TPos[1] + 1)
			else:
				TPos = (TPos[0] - 1, TPos[1] - 1)
	return TPos
	


def do():
	strInput = readInputFile(9)

	splitInput = strInput.split('\n')

	print(do1(splitInput))
	print(do2(splitInput))

	print('done')


do()