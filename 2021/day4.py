from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput

def do1(splitInput):
	numbers = convertToInt(splitInput[0].split(','))

	boards = splitInput[1:]
	intBoards = []
	for board in boards:
		splitBoard = board.split('\n')
		intSplitBoard = []
		for line in splitBoard:
			intSplitBoard.append(convertToInt(line.split(' ')))
		intBoards.append(intSplitBoard)

	return play(numbers, intBoards)		
	

def do2(splitInput):
	return 'done'

def convertToInt(input):
	numbers = []
	for stringNumber in input:
		if stringNumber == '' :
			continue
		else:
			numbers.append(int(stringNumber))
	return numbers

def play(numbers, boards):
	for number in numbers:
		for board in boards:
			playNumberOnBoard(board, number)
			winner = winningBoard(boards)
		if  winner != -1:
			return number * winningScore(boards[winner])

def playNumberOnBoard(board, number):
	for line in board:
		if number in line:
			index = line.index(number)
			line[index] = 'X'			

def winningBoard(boards):
	winning = -1
	for number,board in enumerate(boards):
		if ['X', 'X', 'X', 'X', 'X'] in board:
			winning = number
		else:
			for i in range(len(board[0])):
				completeLine = True
				for j in range(len(board)):
					if board[j][i] != 'X':
						completeLine = False
						break
				if completeLine:
					winning = number
					break
	return winning

def winningScore(board):
	winningSum = 0
	for line in board:
		winningSum += sum([x for x in line if x != 'X'])

	return winningSum

def do():
	strInput = readInputFile(4)
	#strInput = readExampleInput(4)

	splitInput = strInput.split('\n\n')

	print(do1(splitInput))
	print(do2(splitInput))

	print('done')


do()