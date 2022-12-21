from collections import namedtuple
from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt

NumberMonkey = namedtuple('NumberMonkey', ['name', 'number'])
OperationMonkey = namedtuple('OperationMonkey', ['name', 'operation', 'first', 'second'])

def add(first,second):
	return first + second
def substract(first,second):
	return first - second
def multiply(first,second):
	return first * second
def divide(first,second):
	return first / second

operations = {'+': add, '-': substract, '*': multiply, '/': divide}

def do1(splitInput):
	monkeys = extractMonkeyInformation(splitInput)
		
	return getNumber('root', monkeys)

def do2(splitInput):
	monkeys = extractMonkeyInformation(splitInput)

	i1,i2 = [0, 1000000000000]

	monkeys['humn'] = NumberMonkey('humn', i1)
	first1 = getNumber(monkeys['root'].first, monkeys)

	monkeys['humn'] = NumberMonkey('humn', i2)
	first2 = getNumber(monkeys['root'].first, monkeys)

	second = getNumber(monkeys['root'].second, monkeys)

	firstDiff = first1-first2
	secondDiff = abs(second - first2)

	missingDiff = secondDiff / firstDiff
	return int(missingDiff * i2 + i2 + 1)

def extractMonkeyInformation(splitInput):
	monkeys = {}
	for line in splitInput:
		match line.split(' '):
			case [monkey, number]:
				monkey = monkey[0:-1]
				number = int(number)
				monkeys[monkey] = NumberMonkey(monkey, number)
			case [monkey, first, operation, second]:
				monkey = monkey[0:-1]
				monkeys[monkey] = OperationMonkey(monkey,operations[operation],first,second)
	return monkeys	

def getNumber(monkeyName, monkeys):
	monkey = monkeys[monkeyName]
	if type(monkey) is NumberMonkey:
		return monkey.number
	
	return monkey.operation(getNumber(monkey.first, monkeys), getNumber(monkey.second, monkeys))

def do():
	strInput = readInputFile(21)

	splitInput = strInput.split('\n')

	print(do1(splitInput))
	print(do2(splitInput))

	print('done')


do()