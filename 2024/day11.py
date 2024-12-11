from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt
from collections import defaultdict

def do1And2(numbers):

	blinks = {}
	blinks[0] = {}
	for number in numbers:
		blinks[0][number] = 1
	
	for i in range(1,76):
		blinks[i] = defaultdict(int)
		for number,count in blinks[i-1].items():
			match number:
				case 0:
					blinks[i][1] += count
				case a if len(str(a)) % 2 == 0:
					halfLength = len(str(a))//2
					blinks[i][int(str(a)[:halfLength])] += count
					blinks[i][int(str(a)[halfLength:])] += count
				case _:
					blinks[i][number * 2024] += count
	
	result1 = sum([value for value in blinks[25].values()])
	result2 = sum([value for value in blinks[75].values()])

	return result1,result2

def do():
	strInput = readInputFile(11)

	numbers = convertToInt(strInput.split(' '))

	print(do1And2(numbers))

	print('done')


do()