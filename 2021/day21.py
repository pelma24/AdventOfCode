from functools import cache
from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt
from collections import Counter, deque

die = deque([i for i in range(1,101)])

def do1(player1,player2):
	firstDeque = deque([i for i in range(1,11)])
	secondDeque = deque([i for i in range(1,11)])

	firstDeque.rotate(-(player1-1))
	secondDeque.rotate(-(player2-1))

	score1,score2,diceRolls = play1(firstDeque, secondDeque)
	losingScore = min([score1, score2])

	return diceRolls * losingScore

def do2(player1,player2):

	wins1, wins2 = play2(player1, player2, 0, 0)

	print(f'Player1: {wins1}, Player2: {wins2}\n')
	return max(wins1 / 27, wins2)

def getOptions():
	options1 = []
	for i in range(1,4):
		for j in range(1,4):
			for k in range(1,4):
				options1.append(i+j+k)

	options = [(x,y) for x in options1 for y in options1]

	counts = Counter()
	for option in options:
		counts[option] += 1
	
	return counts

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

			newfirst = (first - 1 + option[0]) % 10 + 1
			newscore1 = score1 + newfirst

			newsecond = (second - 1 + option[1]) % 10 + 1
			newscore2 = score2 + newsecond
			
			result1, result2 = play2(newfirst,newsecond,newscore1,newscore2)
			result = (result[0] + number * result1, result[1] + number * result2)
		return result


def play1(first, second):
	score1 = 0
	score2 = 0
	diceRolls = 0

	while score1 < 1000 and score2 < 1000:
		diceNumbers =  []
		for _ in range(3):
			diceNumbers.append(die[0])
			die.rotate(-1)
		diceRolls += 3

		first.rotate(-sum(diceNumbers))
		score1 += first[0]
		if score1 >= 1000:
			return score1,score2,diceRolls

		diceNumbers =  []
		for _ in range(3):
			diceNumbers.append(die[0])
			die.rotate(-1)
		diceRolls += 3

		second.rotate(-sum(diceNumbers))
		score2 += second[0]
	
	return score1,score2,diceRolls




def do():
	strInput = readInputFile(21)

	player1,player2 = convertToInt(strInput.split('\n'))

	print(do1(player1,player2))
	print(do2(player1,player2))

	print('done')


do()