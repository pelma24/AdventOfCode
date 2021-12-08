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
		outputValue = int(calculateOutputValues(outputValues, mapping))

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
	# a (7)
	a = list(set(inputPerLength[3][0]).symmetric_difference(set(inputPerLength[2][0])))[0]
	mapping[a] = {'a'}
	removeFromMapping(a, 'a', mapping)

	# c & f (1)
	one = [x for x in mapping.keys() if mapping[x] == {'c', 'f'}]
	sumOfOne = 0
	for input in inputValues:
		if one[0] in input:
			sumOfOne += 1
	if sumOfOne == 8:
		mapping[one[0]] = {'c'}
		removeFromMapping(one[0], 'c', mapping)
		removeFromMapping(one[1], 'f', mapping)
	else:
		mapping[one[0]] = {'f'}
		removeFromMapping(one[0], 'f', mapping)
		removeFromMapping(one[1], 'c', mapping)

	# b & d (4)
	four = [x for x in mapping.keys() if mapping[x] == {'b', 'd'}]
	sumOfFour = 0
	for input in inputValues:
		if four[0] in input:
			sumOfFour += 1
	if sumOfFour == 6:
		mapping[four[0]] = {'b'}
		removeFromMapping(four[0], 'b', mapping)
		removeFromMapping(four[1], 'd', mapping)
	else:
		mapping[four[0]] = {'d'}
		removeFromMapping(four[0], 'd', mapping)
		removeFromMapping(four[1], 'b', mapping)

	# e & g
	others = [x for x in mapping.keys() if mapping[x] == {'e', 'g'}]
	sumOfOthers = 0
	for input in inputValues:
		if others[0] in input:
			sumOfOthers += 1
	if sumOfOthers == 4:
		mapping[others[0]] = {'e'}
		removeFromMapping(others[0], 'e', mapping)
	else:
		mapping[others[0]] = {'g'}
		removeFromMapping(others[0], 'g', mapping)
	
	return mapping

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
	
	return result

def do():
	strInput = readInputFile(8)

	splitInput = strInput.split('\n')

	print(do1(splitInput))
	print(do2(splitInput))

	print('done')


do()