from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt

def do1(xRange, yRange):
	xMin,xMax = convertToInt(xRange.split(','))
	yMin,yMax = convertToInt(yRange.split(','))

	maxY = -100000

	for xVel in range(1, xMax + 1):
		for yVel in range(0, 200):
			currentMaxY = fly((0,0), (xVel,yVel), (xMin,xMax), (yMin, yMax))
			maxY = max(maxY, currentMaxY)
	
	return maxY

def do2(xRange, yRange):
	xMin,xMax = convertToInt(xRange.split(','))
	yMin,yMax = convertToInt(yRange.split(','))

	landingVels = []

	for xVel in range(1, xMax + 1):
		for yVel in range(-100, 200):
			currentMaxY = fly((0,0), (xVel,yVel), (xMin,xMax), (yMin, yMax))
			if currentMaxY != -1000000:
				landingVels.append((xVel,yVel))

	return len(landingVels)

def step(xPos, yPos, xVel, yVel):

	xPos = xPos + xVel
	yPos = yPos + yVel
	if xVel > 0:
		xVel -= 1
	elif xVel < 0:
		xVel += 1
	yVel -= 1

	return (xPos, yPos, xVel, yVel)

def fly(position, velocity, targetX, targetY):
	maxY = -1000000
	x,y = position
	xVel,yVel = velocity
	yMin,_ = targetY

	while True:	
		x,y,xVel,yVel = step(x, y, xVel, yVel)
		maxY = max(maxY, y)
		if isInTargetArea((x, y), targetX, targetY):
			return maxY
		if xVel == 0:
			if y < yMin:
				return -1000000		

def isInTargetArea(position, targetX, targetY):
	x,y = position
	xMin,xMax = targetX
	yMin, yMax = targetY

	if xMin <= x <= xMax and yMin <= y <= yMax:
		return True
	
	return False

def do():
	strInput = readInputFile(17)

	xRange,yRange = strInput.split('\n')

	print(do1(xRange,yRange))
	print(do2(xRange,yRange))

	print('done')


do()