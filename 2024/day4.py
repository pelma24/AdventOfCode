from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt

directions = {'UP':(0,-1), 'DOWN':(0,1), 'LEFT':(-1,0), 'RIGHT':(1,0), 'UPLEFT':(-1,-1), 'UPRIGHT':(1,-1), 'DOWNLEFT':(-1,1), 'DOWNRIGHT':(1,1)}
word = ['X','M','A','S']

def prepareBoard(board):

	newBoard = []

	newBoard.append(['.' for x in range(len(board[0])+2)])

	for line in board:
		newLine = ['.'] + [x for x in line] + ['.']
		newBoard.append(newLine)

	newBoard.append(['.' for x in range(len(board[0])+2)])

	return newBoard

def findWordInDirection(posX,posY,direction,board):
	
	currentPos = (posX,posY)
	for wordPos in range(1,5):
		if wordPos == 4:
			return True
		
		currentPos = (currentPos[0] + direction[0], currentPos[1] + direction[1])
		if not(board[currentPos[1]][currentPos[0]] == word[wordPos]):
			return False

	return False

def findWords(posX,posY,board):

	words = 0

	for direction in directions.keys():
		words = words + findWordInDirection(posX,posY,directions[direction],board)

	return words

def do1(board):

	words = 0

	for posY,line in enumerate(board):
		for posX,value in enumerate(line):
			if value == 'X':
				words = words + findWords(posX,posY,board)

	return words

def do2(splitInput):
	return 'done'

def do():
	strInput = readInputFile(4)
	#strInput = readExampleInput(4)

	board = prepareBoard(strInput.split('\n'))

	print(do1(board))
	print(do2(board))

	print('done')


do()