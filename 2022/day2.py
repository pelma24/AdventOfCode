from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt

points = {'X':1, 'Y':2, 'Z':3}

scoreX = {'A':3, 'B':0, 'C':6}
scoreY = {'A':6, 'B':3, 'C':0}
scoreZ = {'A':0, 'B':6, 'C':3}

choiceA = {'X':'Z', 'Y':'X', 'Z':'Y'}
choiceB = {'X':'X', 'Y':'Y', 'Z':'Z'}
choiceC = {'X':'Y', 'Y':'Z', 'Z':'X'}


winScores = {'X':scoreX, 'Y':scoreY, 'Z':scoreZ}
myChoice = {'A':choiceA, 'B':choiceB, 'C':choiceC}


def do1(splitInput):
	score = 0
	for line in splitInput:
		opponent,me = line.split(' ')
		roundScore = points[me] + winScores[me][opponent]
		score += roundScore
	
	return score

def do2(splitInput):
	score = 0
	for line in splitInput:
		opponent,result = line.split(' ')
		me = myChoice[opponent][result]
		roundScore = points[me] + winScores[me][opponent]
		score += roundScore
	
	return score

def do():
	strInput = readInputFile(2)
	#strInput = readExampleInput(2)
	
	splitInput = strInput.split('\n')
	
	print(do1(splitInput))
	print(do2(splitInput))

	print('done')


do()