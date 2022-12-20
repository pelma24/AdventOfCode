from collections import defaultdict
from copy import deepcopy
from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt

def do1(intInput):
	intInput = [(seq,x) for seq,x in enumerate(intInput)]
	workingList = mix(intInput, 1)
	length = len(intInput)

	zeroSeq = [y for (y,x) in intInput if x == 0][0]	
	zeroIndex = workingList.index((zeroSeq,0))
	
	return workingList[(zeroIndex + 1000) % length][1] + workingList[(zeroIndex + 2000) % length][1] + workingList[(zeroIndex + 3000) % length][1]

def do2(intInput):
	key = 811589153
	intInput = [(seq, x * key) for seq,x in enumerate(intInput)]
	length = len(intInput)
	workingList = mix(intInput, 10)

	zeroSeq = [y for (y,x) in intInput if x == 0][0]	
	zeroIndex = workingList.index((zeroSeq,0))
	
	return workingList[(zeroIndex + 1000) % length][1] + workingList[(zeroIndex + 2000) % length][1] + workingList[(zeroIndex + 3000) % length][1]

def mix(intInput, times):
	workingList = deepcopy(intInput)
	length = len(intInput)
	for _ in range(times):
		for seq,number in intInput:
			currentIndex = workingList.index((seq,number))
			if number == 0:
				continue
			newIndex = (currentIndex + number) % (length - 1)
			workingList.pop(currentIndex)
			workingList.insert(newIndex, (seq,number))
	
	return workingList

def do():
	strInput = readInputFile(20)

	intInput = convertToInt(strInput.split('\n'))

	print(do1(intInput))
	print(do2(intInput))

	print('done')


do()