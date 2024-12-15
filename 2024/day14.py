from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt
import re

xCount = {}
robotPosition = {}
robotVelocity = {}

def extractRobotInfo(strInput):
	splitInput = strInput.split('\n')
	
	for count,line in enumerate(splitInput):
		match = re.search('p=(\d+,\d+) v=(-?\d+,-?\d+)', line)
		pos = convertToInt(match.groups()[0].split(','))
		velocity = convertToInt(match.groups()[1].split(','))

		robotPosition[count] = (pos[0], pos[1])
		robotVelocity[count] = (velocity[0], velocity[1])

	return

def move(robot):
	width = 101
	height = 103

	x,y = robotPosition[robot]
	velX,velY = robotVelocity[robot]

	newPos = ((x + velX) % width, (y + velY) % height)

	robotPosition[robot] = newPos

def calculateSafetyFactor():
	width = 101
	height = 103

	first = 0
	second = 0
	third = 0
	fourth = 0
	for robot in robotPosition.values():
		x,y = robot
		match robot:
			case (x,y) if x in range(0, width//2) and y in range(0, height//2):
				first += 1
			case (x,y) if x in range(width//2 + 1, width) and y in range(0, height//2):
				second += 1
			case (x,y) if x in range(0, width//2) and y in range(height//2 + 1, height):
				third += 1
			case (x,y) if x in range(width//2 + 1, width) and y in range(height//2 + 1, height):
				fourth += 1
	
	return first * second * third * fourth

def printRobots(count):
	map = [['.' for i in range(101)] for j in range(103)]

	numberOfX = 0
	for robot in robotPosition.values():
		x,y = robot
		if map[y][x] != 'x':
			numberOfX += 1
			map[y][x] = 'x'
		
	xCount[count] = numberOfX
	
def do1():               

	for _ in range(100):
		for robot in robotPosition.keys():
			move(robot)
	
	safetyFactor = calculateSafetyFactor()
	
	return safetyFactor

def do2():
	for count in range(101, 15000):
		for robot in robotPosition.keys():
			move(robot)
		printRobots(count)
	
	maxRobotsVisible = max([x for x in xCount.values()])
	return [x for x in xCount.keys() if xCount[x] == maxRobotsVisible][0]

def do():
	strInput = readInputFile(14)

	extractRobotInfo(strInput)

	print(do1())
	print(do2())

	print('done')


do()