from copy import deepcopy
from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt
import re

class Monkey:
	def __init__(self, items, operation, value, testMethod, throwIfTrue, throwIfFalse):
		self.items = items
		self.operation = operation
		self.value = value
		self.testMethod = testMethod
		self.throwIfTrue = throwIfTrue
		self.throwIfFalse = throwIfFalse
		self.inspectedItems = 0
	
	def addItem(self, item):
		self.items.append(item)

originalMonkeys = []

def multiply(value, old):
	return old * value
def add(value, old):
	return old + value
def multiplyWithItself(old,value):
	return old * old

def do1(splitInput):
	createMonkeys(splitInput)	
	
	monkeys = deepcopy(originalMonkeys)

	for _ in range(20):
		monkeyIndex = 0
		for _ in range(len(monkeys)):
			currentMonkey = monkeys[monkeyIndex]
			while currentMonkey.items:
				currentMonkey.inspectedItems += 1
				item = currentMonkey.items.pop(0)
				item = currentMonkey.operation(value=currentMonkey.value, old=item)
				item = int(item / 3)
				if item % currentMonkey.testMethod == 0:
					monkeys[currentMonkey.throwIfTrue].addItem(item)
				else:
					monkeys[currentMonkey.throwIfFalse].addItem(item)
			monkeyIndex += 1
	
	inspectedItems = [x.inspectedItems for x in monkeys]
	inspectedItems.sort(reverse=True)

	return inspectedItems[0] * inspectedItems[1]

def do2(splitInput):
	monkeys = deepcopy(originalMonkeys)
	
	divisor = 1
	for monkey in monkeys:
		divisor *= monkey.testMethod

	for _ in range(10000):
		monkeyIndex = 0
		for _ in range(len(monkeys)):
			currentMonkey = monkeys[monkeyIndex]
			while currentMonkey.items:
				currentMonkey.inspectedItems += 1
				item = currentMonkey.items.pop(0)
				item = currentMonkey.operation(value=currentMonkey.value, old=item)
				item = item - (int(item / divisor) * divisor)
				if item % currentMonkey.testMethod == 0:
					monkeys[currentMonkey.throwIfTrue].addItem(item)
				else:
					monkeys[currentMonkey.throwIfFalse].addItem(item)
			monkeyIndex += 1
	
	inspectedItems = [x.inspectedItems for x in monkeys]
	inspectedItems.sort(reverse=True)

	return inspectedItems[0] * inspectedItems[1]

def createMonkeys(splitInput):
	for monkey in splitInput:
		lines = monkey.split('\n')
		startingItems = [int(x[0:2]) for x in lines[1].split(' ')[4:]]
		match lines[2].split(' '):
			case [*stuff, '*', 'old']:
				operation = multiplyWithItself
				value = 0
			case [*stuff, '*', value]:
				operation = multiply
				value = int(value)
			case [*stuff, '+', value]:
				operation = add
				value = int(value)
		matchTest = re.match('  Test: divisible by (\d+)', lines[3])
		testMethod = int(matchTest.groups()[0])
		throwIfTrue = int(lines[4][-1])
		throwIfFalse = int(lines[5][-1])

		originalMonkeys.append(Monkey(startingItems, operation, value, testMethod, throwIfTrue, throwIfFalse))

def do():
	strInput = readInputFile(11)

	splitInput = strInput.split('\n\n')

	print(do1(splitInput))
	print(do2(splitInput))

	print('done')


do()