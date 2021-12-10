from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt
from collections import defaultdict

correspondingCharacters = {')':'(', ']':'[', '}':'{', '>':'<'}
correspondingCharacters_reverse = {'(':')', '[':']', '{':'}', '<':'>'}
points = {')': 3, ']': 57, '}': 1197, '>': 25137, None: 0}
points2 = {')': 1, ']': 2, '}': 3, '>': 4, None: 0}

def do1(splitInput):
	score = 0

	for line in splitInput:
		illegalCharacter,_ = findIllegalCharacter(line)
		score += points[illegalCharacter]
	
	return score

def do2(splitInput):
	scores = []

	for line in splitInput:
		illegalCharacter,remainingCloses = findIllegalCharacter(line)
		if not illegalCharacter:
			lineScore = 0
			while remainingCloses:
				lineScore = lineScore * 5
				lineScore += points2[correspondingCharacters_reverse[remainingCloses.pop()]]
			scores.append(lineScore)
	
	scores.sort()
	return scores[len(scores) // 2]

def findIllegalCharacter(line):
	lastOpened = []
	for character in line:
		match character:
			case '(' | '[' | '{' | '<':
				lastOpened.append(character)
			case ']' | ')' | '}' | '>' :
				correspondingCharacter = correspondingCharacters[character]
				if lastOpened[-1] != correspondingCharacter:
					return character,lastOpened
				else:
					lastOpened.pop()
	return None,lastOpened

def do():
	strInput = readInputFile(10)

	splitInput = strInput.split('\n')
	
	print(do1(splitInput))
	print(do2(splitInput))

	print('done')


do()