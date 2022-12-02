from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt

points = {'X':1, 'Y':2, 'Z':3}

choices = ['Y', 'A', 'Z', 'B', 'X', 'C', 'Y']
sameChoice = {'A':'X', 'B':'Y', 'C':'Z'}

def do1(splitInput):
	score = 0
	for line in splitInput:
		opponent,me = line.split(' ')

		if [opponent,me] in choices:
			winScore = 0
		elif [me,opponent] in choices:
			winScore = 6
		else:
			winScore = 3
		roundScore = points[me] + winScore
		score += roundScore

	return score

def do2(splitInput):
	score = 0
	for line in splitInput:
		opponent,result = line.split(' ')
		opponentIndex = choices.index(opponent)
		match result:
			case 'X':
				me = choices[opponentIndex + 1]
				winScore = 0
			case 'Y':
				me = sameChoice[opponent]
				winScore = 3
			case 'Z':
				me = choices[opponentIndex - 1]
				winScore = 6
		roundScore = points[me] + winScore
		score += roundScore

	return score

def do():
	strInput = readInputFile(2)
	
	splitInput = strInput.split('\n')
	
	print(do1(splitInput))
	print(do2(splitInput))

	print('done')


do()