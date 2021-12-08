from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt
from collections import defaultdict

numberMapping = {1: ['c', 'f'], 2: ['a', 'c', 'd', 'e', 'g'], 3: ['a', 'c', 'd', 'f', 'g'], 4: ['b', 'c', 'd', 'f'], 5: ['a', 'b', 'd', 'f', 'g'], 6: ['a', 'b', 'd', 'e', 'f', 'g'], 7: ['a', 'c', 'f'], 8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'], 9: ['a', 'b', 'c', 'd', 'f', 'g'], 0: ['a', 'b', 'c', 'e', 'f', 'g']}
allPossibleDigitsPerNumber = {2: ['c', 'f'], 3: ['a', 'c', 'f'], 4: ['b', 'c', 'd', 'f'], 7: ['a', 'b', 'c', 'd', 'e', 'f', 'g'], 5: ['a', 'b', 'c', 'd', 'e', 'f', 'g'], 6: ['a', 'b', 'c', 'd', 'e', 'f', 'g']}

def do1(splitInput):
	uniqueDigits = 0

	for line in splitInput:
		input,output = line.split('|')

		outputDigits = output.split(' ')

		for digit in outputDigits:
			if len(digit) in [2, 3, 4, 7]:
				uniqueDigits += 1
	
	return uniqueDigits

def do2(splitInput):
	sumOutputValues = 0

	for line in splitInput:
		input,output = line.split('|')

		inputValues = input.split(' ')
		outputValues = output.split(' ')

		mapping = getMapping(inputValues)
		outputValue = calculateOutputValues(outputValues, mapping)

		sumOutputValues += outputValue
	
	return sumOutputValues

def getMapping(inputValues):
	mapping = {'a': set(('a', 'b', 'c', 'd', 'e', 'f', 'g')), 'b': set(('a', 'b', 'c', 'd', 'e', 'f', 'g')), 'c': set(('a', 'b', 'c', 'd', 'e', 'f', 'g')), 'd': set(('a', 'b', 'c', 'd', 'e', 'f', 'g')), 'e': set(('a', 'b', 'c', 'd', 'e', 'f', 'g')), 'f': set(('a', 'b', 'c', 'd', 'e', 'f', 'g')), 'g': set(('a', 'b', 'c', 'd', 'e', 'f', 'g'))}

	inputPerLength = defaultdict(lambda: [])

	for inputValue in inputValues[0:-1]:
		length = len(inputValue)
		inputPerLength[length].append([x for x in inputValue])
		possibleValues = set(allPossibleDigitsPerNumber[length])
		for digit in inputValue:
			mapping[digit].intersection_update(possibleValues)

	# c & f (1)
	one1,one2 = [x for x in mapping.keys() if mapping[x] == {'c', 'f'}]
	sumOfOne = countOccurence(one1, inputValues)	
	
	if sumOfOne == 8:
		mapping[one1] = {'c'}
		removeFromMapping(one1, 'c', mapping)
		removeFromMapping(one2, 'f', mapping)
	else:
		mapping[one1] = {'f'}
		removeFromMapping(one1, 'f', mapping)
		removeFromMapping(one2, 'c', mapping)

	# a (7)
	seven = [x for x in mapping.keys() if mapping[x] == {'a'}][0]
	removeFromMapping(seven, 'a', mapping)

	# b & d (4)
	four1,four2 = [x for x in mapping.keys() if mapping[x] == {'b', 'd'}]
	sumOfFour = countOccurence(four1, inputValues)
	if sumOfFour == 6:
		mapping[four1] = {'b'}
		removeFromMapping(four1, 'b', mapping)
		removeFromMapping(four2, 'd', mapping)
	else:
		mapping[four1] = {'d'}
		removeFromMapping(four1, 'd', mapping)
		removeFromMapping(four2, 'b', mapping)

	# e & g
	other1,other2 = [x for x in mapping.keys() if mapping[x] == {'e', 'g'}]
	sumOfOthers = countOccurence(other1, inputValues)
	if sumOfOthers == 4:
		mapping[other1] = {'e'}
		removeFromMapping(other1, 'e', mapping)
	else:
		mapping[other1] = {'g'}
		removeFromMapping(other1, 'g', mapping)
	
	return mapping

def countOccurence(digit, inputValues):
	sumOfDigit = 0
	for input in inputValues:
		if digit in input:
			sumOfDigit += 1
	return sumOfDigit

def removeFromMapping(rightKey, digit, mapping):
	for key in mapping.keys():
			if key != rightKey:
				if digit in mapping[key]:
					mapping[key].remove(digit)

def calculateOutputValues(outputValues, mapping):
	result = ''
	for outputValue in outputValues:
		if outputValue == '':
			continue
		
		resultStr = []
		for digit in outputValue:
			resultStr.append(list(mapping[digit])[0])
		sortedResult = sorted(resultStr)

		resultDigit = str([x for x in numberMapping.keys() if sorted(numberMapping[x]) == sortedResult][0])
		result += resultDigit	
	
	return int(result)

def do():
	strInput = readInputFile(8)
	splitInput = strInput.split('\n')

	print(do1(splitInput))
	print(do2(splitInput))

	print('done')


do()