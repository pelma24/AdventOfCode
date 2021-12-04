from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput

def do1(splitInput):
	numbers = convertToInt(splitInput[0].split(','))

	boards = splitInput[1:]
	intBoards = prepareBoards(boards)

	return play1(numbers, intBoards)		
	

def do2(splitInput):
	numbers = convertToInt(splitInput[0].split(','))

	boards = splitInput[1:]
	intBoards = prepareBoards(boards)
	
	return play2(numbers, intBoards)

def prepareBoards(boards):
	intBoards = []
	for board in boards:
		splitBoard = board.split('\n')
		intSplitBoard = []
		for line in splitBoard:
			intSplitBoard.append(convertToInt(line.split(' ')))
		intBoards.append(intSplitBoard)
	return intBoards

def convertToInt(input):
	numbers = []
	for stringNumber in input:
		if stringNumber == '' :
			continue
		else:
			numbers.append(int(stringNumber))
	return numbers

def play1(numbers, boards):
	for number in numbers:
		for board in boards:
			playNumberOnBoard(board, number)
		winners = winningBoards(boards)
		if  len(winners) != 0:
			return number * winningScore(boards[winners[0]])

def play2(numbers, boards):
	for number in numbers:
		for board in boards:
			playNumberOnBoard(board, number)
		if len(boards) == 1:
			return number * winningScore(boards[winners[-1]])
		winners = winningBoards(boards)
		if winners:
			for winner in sorted(winners, reverse=True):
				boards.pop(winner)
		
		

def playNumberOnBoard(board, number):
	for line in board:
		if number in line:
			index = line.index(number)
			line[index] = 'X'			

def winningBoards(boards):
	winning = []
	for number,board in enumerate(boards):
		if ['X', 'X', 'X', 'X', 'X'] in board:
			winning.append(number)
		else:
			for i in range(len(board[0])):
				completeLine = True
				for j in range(len(board)):
					if board[j][i] != 'X':
						completeLine = False
						break
				if completeLine:
					winning.append(number)
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