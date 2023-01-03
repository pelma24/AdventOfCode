from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt

add = {'=':'-', '-':'0','0':'1','1':'2','2':'3'}
divide = {3:'=', 4:'-'}

def do1(splitInput):
	sumOfNumbers = 0

	for number in splitInput:
		sumOfNumbers += convertToDecimal(number)

	return convertToSnafu(sumOfNumbers)

def do2(splitInput):
	return 'nothing to do'

def convertToDecimal(number):
	decimal = 0
	number = number[::-1]
	for i in range(0,len(number)):
		match number[i]:
			case '=':
				decimal -= 2*pow(5,i)
			case '-':
				decimal -= pow(5,i)
			case num:
				decimal += pow(5,i) * int(num)
	return decimal

def convertToSnafu(number):
	i = 0
	while True:
		if number < pow(5,i):
			i = i-1
			break
		i += 1

	result = ''
	remaining = number
	while remaining:
		divided = int(remaining / (pow(5,i)))
		if divided > 2:
			if result:
				result = result[0:-1] + add[result[-1]] + divide[divided]
				result = updateResult(result)
			else:
				result = '1' + divide[divided]
		else:
			result = result + str(divided)
		remaining = remaining % (pow(5,i)) 
		i -= 1
	
	for _ in range(i,-1,-1):
		result += '0'

	return result

def updateResult(result):
	if '3' in result:
		position = result.index('3')
		if position == 0:
			return '1=' + result[1:]
		else:
			result = result[0:position-1] + add[result[position-1]] + '=' + result[position+1:]
			result = updateResult(result)
	return result 


def do():
	strInput = readInputFile(25)

	splitInput = strInput.split('\n')

	print(do1(splitInput))
	print(do2(splitInput))

	print('done')


do()