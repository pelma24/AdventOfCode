from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt

def do1(strInput):
	windowSize = 4
	result = [y + windowSize for y,x in enumerate([strInput[i:i+windowSize] for i in range(len(strInput) - windowSize + 1)]) if len(set(x)) == windowSize][0]
	return result

def do2(strInput):
	windowSize = 14
	result = [y + windowSize for y,x in enumerate([strInput[i:i+windowSize] for i in range(len(strInput) - windowSize + 1)]) if len(set(x)) == windowSize][0]
	return result

def do():
	strInput = readInputFile(6)

	print(do1(strInput))
	print(do2(strInput))

	print('done')


do()