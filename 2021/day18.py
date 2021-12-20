from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt
import re
from copy import deepcopy

def do1(splitInput):
	addition = splitInput[0]
	for line in splitInput[1:]:
		addition = '[' + addition + ',' + line + ']'

		addition = reduce(addition)

	magnitude = calculateMagnitude(addition)
	
	return magnitude

def do2(splitInput):
	magnitudes = []
	
	for i in splitInput:
		for j in splitInput:
			if i == j:
				continue
			addition = '[' + i + ',' + j + ']'
			addition = reduce(addition)
			magnitude = calculateMagnitude(addition)
			magnitudes.append(magnitude)	
	
	return max(magnitudes)

def reduce(addition):
	nestingLevel = 0
	lastPosition = -1
	newInput = deepcopy(addition)
	repeat = True
	while repeat:
		nestingLevel = 0
		lastPosition = -1
		addition = deepcopy(newInput)
		repeat = False
		for position,next in enumerate(addition):
			match next:
				case '[':
					nestingLevel += 1
					if nestingLevel > 4:
						left,right = findInner(addition[position:])
						length = len(str(left) + str(right) + ',') + 2
						nextNumberPos = findNextNumber(addition[position+length:])
						newInput = addition[0:position] + '0' + addition[position + length:]
						newInput = addToNextNumber(nextNumberPos, right, position, newInput)
						newInput = addToLastNumber(lastPosition, left, position, newInput)
						repeat = True
						break						
				case ']':
					nestingLevel -= 1
				case a if a.isnumeric():
					if not addition[position-1].isnumeric():	
						lastPosition = position
		# again for big numbers
		if not repeat:
			for position,next in enumerate(addition):
				match next:
					case a if a.isnumeric():
						if addition[position+1].isnumeric():
							number = int(addition[position:position + 2])
							splitLeft = number // 2
							splitRight = (number + 1) // 2
							newInput = addition[0:position] + '[' + str(splitLeft) + ',' + str(splitRight) + ']' + addition[position + 2:]
							repeat = True
							break

	return newInput

def addToNextNumber(nextNumberPos, right, position, newInput):
	if nextNumberPos == -1:
		return newInput
	number = ''
	nextNumberStart = position + nextNumberPos + 1
	currentPos = nextNumberStart
	while newInput[currentPos].isnumeric():
		number += newInput[currentPos]
		currentPos += 1
	
	length = len(number)
	number = int(number)

	
	newInput = newInput[0: nextNumberStart] + str(number + right) + newInput[nextNumberStart + length:]  

	return newInput

def addToLastNumber(lastNumberPos, left, position, newInput):
	if lastNumberPos == -1:
		return newInput
	number = ''
	currentPos = lastNumberPos
	while newInput[currentPos].isnumeric():
		number += newInput[currentPos]
		currentPos += 1
	
	length = len(number)
	number = int(number)

	newInput = newInput[0:lastNumberPos] + str(number + left) + newInput[lastNumberPos + length:]

	return newInput

def findInner(addition):
	left = ''
	right = ''
	isLeft = True
	lastOpened = 0
	for next in addition[1:]:
		match next:
			case '[':
				if isLeft:
					left += next
				else:
					right += next
				lastOpened += 1
			case ']':
				if lastOpened == 0:
					if left.isnumeric():
						left = int(left)
					if right.isnumeric():
						right = int(right)
					return left,right
				if isLeft:
					left += next
				else:
					right += next
				lastOpened -= 1
			case ',':
				if lastOpened == 0:
					isLeft = False
					continue
				else:
					if isLeft:
						left += next
					else:
						right += next
			case _:
				if isLeft:
					left += next
				else:
					right += next

def findNextNumber(input):
	for position,value in enumerate(input):
		if value.isnumeric():
			return position
	return -1

def calculateMagnitude(addition):
	if str(addition).isnumeric():
		return addition
	left,right = findInner(addition)
	
	return 3* calculateMagnitude(left) + 2* calculateMagnitude(right)

def do():
	strInput = readInputFile(18)

	splitInput = strInput.split('\n')

	print(do1(splitInput))
	print(do2(splitInput))

	print('done')


do()