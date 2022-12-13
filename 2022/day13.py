import ast
from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt

def do1(splitInput):
	rightOrderPairs = 0
	
	for index,pair in enumerate(splitInput):
		left,right = pair.split('\n')
		left = ast.literal_eval(left)
		right = ast.literal_eval(right)

		successful,result = compare(left,right)
		if successful and result:
			rightOrderPairs += index + 1		
	
	return rightOrderPairs

def do2(strInput):
	result = []
	
	strInput = strInput.replace('\n\n', '\n')
	splitInput = strInput.split('\n')
	splitInput.append('[[2]]')
	splitInput.append('[[6]]')

	first = ast.literal_eval(splitInput[0])
	result.append(first)

	for line in splitInput[1:]:
		inserted = False
		new = ast.literal_eval(line)
		for index,old in enumerate(result):
			successful,rightOrder = compare(old,new)
			if successful and not rightOrder:
				result.insert(index,new)
				inserted = True
				break
		if not inserted:
			result.append(new)		

	return (result.index([[2]]) + 1) * (result.index([[6]]) + 1) 

def compare(left,right):
	leftLength = len(left)
	rightLength = len(right)
	
	i = -1
	while True:
		i += 1
		if leftLength < i + 1 and rightLength >= i + 1:
			return True,True
		elif rightLength < i + 1 and leftLength >= i + 1:
			return True,False
		elif leftLength < i + 1 and rightLength < i + 1:
			return False,False
		leftPart = left[i]
		rightPart = right[i]

		if type(leftPart) == type(rightPart):
			if type(leftPart) is int:
					if leftPart < rightPart:
						return True,True
					elif rightPart < leftPart:
						return True,False
					else:
						continue
			elif type(leftPart) is list:
					successful,result = compare(leftPart,rightPart)
					if successful:
						return True,result
					else:
						continue
		if type(leftPart) is int:
			leftPart = [leftPart]
		else:
			rightPart = [rightPart]
		successful,result = compare(leftPart,rightPart)
		if successful:
			return True,result
		else:
			continue

def do():
	strInput = readInputFile(13)

	splitInput = strInput.split('\n\n')

	print(do1(splitInput))
	print(do2(strInput))

	print('done')


do()