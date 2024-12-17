from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt

def getProgram(programInput):

	_,program = programInput.split(' ')
	program = convertToInt(program.split(','))

	return program

def getComboOperand(operand,a,b,c):
	match operand:
			case 4:
				return a
			case 5:
				return b
			case 6:
				return c
			case _:
				return operand

def do1(program,a,b,c):
	position = 0
	output = []
	while position < len(program):
		instruction = program[position]
		operand = program[position+1]
		match instruction:
			case 0:
				operand = getComboOperand(operand,a,b,c)
				a = a // (pow(2,operand))
			case 1:
				b = b ^ operand
			case 2:
				operand = getComboOperand(operand,a,b,c)
				b = operand % 8
			case 3:
				if a:
					position = operand
					continue
			case 4:
				b = b ^ c
			case 5:
				operand = getComboOperand(operand,a,b,c)
				output.append(operand % 8)
			case 6:
				operand = getComboOperand(operand,a,b,c)
				b = a // (pow(2,operand))
			case 7:
				operand = getComboOperand(operand,a,b,c)
				c = a // (pow(2,operand))

		position += 2

	return output

def do2(program):
	a = 0
	outputLength = len(program)
	output = do1(program,a,0,0)

	while len(output) < outputLength:
		a = a * 8
		for offset in range(0,8):
			newA = a + offset
			output = do1(program,newA,0,0)
			diffLength = outputLength - len(output)
			if program[diffLength:] == output:
				a = newA
				break	
	return a

def do():
	strInput = readInputFile(17)
	
	_,programInput = strInput.split('\n\n')
	program = getProgram(programInput)

	a = 50230824
	b = 0
	c = 0

	print(do1(program,a,b,c))
	print(do2(program))

	print('done')


do()