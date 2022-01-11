from functools import cache
from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt
from collections import Counter, deque

die = deque([i for i in range(1,101)])

def do1(player1,player2):
	
	score1,score2,diceRolls = play1(player1, player2)
	losingScore = min([score1, score2])

	return diceRolls * losingScore

def do2(player1,player2):

	wins = play2(player1, player2, 0, 0)

	return max(wins)

def getOptions():
	options = []
	for i in range(1,4):
		for j in range(1,4):
			for k in range(1,4):
				options.append(i+j+k)

	counts = Counter()
	for option in options:
		counts[option] += 1
	
	return counts

def play1(first, second):
	score1 = 0
	score2 = 0
	diceRolls = 0

	while score1 < 1000 and score2 < 1000:
		diceNumber = getDice()
		diceRolls += 3

		first = (first - 1 + diceNumber) % 10 + 1
		score1 += first
		if score1 >= 1000:
			return score1,score2,diceRolls

		diceNumber = getDice()
		diceRolls += 3

		second = (second - 1 + diceNumber) % 10 + 1
		score2 += second
		if score2 >= 1000:
			return score1,score2,diceRolls
	
	return score1,score2,diceRolls

@cache
def play2(first, second, score1, score2):
	if score1 >= 21:
		return (1,0)
	elif score2 >= 21:
		return (0,1)
	else:
		counts = getOptions()
		result = (0,0)
		for option,number in counts.items():

			newfirst = (first - 1 + option) % 10 + 1
			newscore1 = score1 + newfirst

			if newscore1 < 21:
				counts2 = getOptions()
				for option2,number2 in counts2.items():
					newsecond = (second - 1 + option2) % 10 + 1
					newscore2 = score2 + newsecond
			
					result1, result2 = play2(newfirst,newsecond,newscore1,newscore2)
					result = (result[0] + number * number2 * result1, result[1] + number * number2 * result2)
			else:
				result = (result[0] + number, result[1])
		return result

def getDice():
	diceNumbers =  []
	for _ in range(3):
		diceNumbers.append(die[0])
		die.rotate(-1)
	return sum(diceNumbers)

def do():
	strInput = readInputFile(21)

	player1,player2 = convertToInt(strInput.split('\n'))

	print(do1(player1,player2))
	print(do2(player1,player2))

	print('done')


do()