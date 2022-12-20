from collections import defaultdict
from copy import deepcopy
from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt

def do1(intInput):
	diff = 100000
	workingList = deepcopy(intInput)
	length = len(intInput)
	for number in intInput:
		currentIndex = workingList.index(number)
		if number == 0:
			workingList[currentIndex] = diff
			continue
		newIndex = (currentIndex + number) % (length - 1)
		workingList.pop(currentIndex)
		workingList.insert(newIndex, number + diff)
	workingList = [x-diff for x in workingList]

	zeroIndex = workingList.index(0)
	
	return workingList[(zeroIndex + 1000) % length] + workingList[(zeroIndex + 2000) % length] + workingList[(zeroIndex + 3000) % length]

def do2(intInput):
	key = 811589153
	intInput = [(seq, x * key) for seq,x in enumerate(intInput)]
	length = len(intInput)
	workingList = deepcopy(intInput)
	for _ in range(10):
		for seq,number in intInput:
			currentIndex = workingList.index((seq,number))
			if number == 0:
				zeroSeq = seq
				continue
			newIndex = (currentIndex + number) % (length - 1)
			workingList.pop(currentIndex)
			workingList.insert(newIndex, (seq,number))

	zeroIndex = workingList.index((zeroSeq,0))
	
	return workingList[(zeroIndex + 1000) % length][1] + workingList[(zeroIndex + 2000) % length][1] + workingList[(zeroIndex + 3000) % length][1]

def do():
	strInput = readInputFile(20)
	#strInput = readExampleInput(20)

	intInput = convertToInt(strInput.split('\n'))

	print(do1(intInput))
	print(do2(intInput))

	print('done')


do()