from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt
from collections import defaultdict

order = defaultdict(list)
firstOrder = defaultdict(list)

def createOrder(orderInstructions):
	orderInstructions = orderInstructions.split('\n')
	for line in orderInstructions:
		first,second = line.split('|')
		order[int(second)].append(int(first))
		firstOrder[int(first)].append(int(second))

	return

def isCorrectOrder(update):
	index = 0
	for page in update:
		for restriction in order[page]:
			if not restriction in update:
				continue
			if not(update.index(restriction) < index):
				return False
		index = index + 1
	
	return True

def do1(updates):
	updates = updates.split('\n')

	incorrectUpdates = []

	result = 0

	for update in updates:
		update = convertToInt(update.split(','))
		if isCorrectOrder(update):
			result += update[int(len(update) / 2)]
		else:
			incorrectUpdates.append(update)

	return result,incorrectUpdates

def do2(incorrectUpdates):

	result = 0

	for incorrectUpdate in incorrectUpdates:
		correctedUpdate = incorrectUpdate.copy()
		
		i = 0
		while (i < len(correctedUpdate)):
			newIndex = i
			page = correctedUpdate[i]
			for restriction in firstOrder[page]:
				if not restriction in correctedUpdate:
					continue
				otherIndex = correctedUpdate.index(restriction)
				if not(otherIndex > i):
					newIndex = otherIndex - 1
			
			if newIndex != i:
				correctedUpdate.pop(i)
				if newIndex == -1:
					correctedUpdate = [page] + correctedUpdate				
				else:
					correctedUpdate.insert(newIndex, page)
				i = 0
			else:
				i = i + 1

		result += correctedUpdate[int(len(correctedUpdate) / 2)]

	return result

def do():
	strInput = readInputFile(5)

	orderInstructions,updates = strInput.split('\n\n')

	createOrder(orderInstructions)

	result1,incorrectUpdates = do1(updates)
	print(result1)
	print(do2(incorrectUpdates))

	print('done')


do()