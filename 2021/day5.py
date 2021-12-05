from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt
import re
from collections import defaultdict

def do1(splitInput):
	points = defaultdict(lambda: 0)

	parsedLines = parseLines(splitInput)
	
	for line in parsedLines:
		x1,x2,y1,y2 = line
		addPoints(x1, x2, y1, y2, points, False)

	multiples = findMultiples(points)
	return len(multiples)

def do2(splitInput):
	points = defaultdict(lambda: 0)

	parsedLines = parseLines(splitInput)
	
	for line in parsedLines:
		x1,x2,y1,y2 = line
		addPoints(x1, x2, y1, y2, points, True)

	multiples = findMultiples(points)
	return len(multiples)

def parseLines(splitInput):
	parsedLines = []
	for line in splitInput:
		match = re.fullmatch('(?P<x1>[0-9]+),(?P<y1>[0-9]+) -> (?P<x2>[0-9]+),(?P<y2>[0-9]+)', line)
		if match:
			x1 = int(match.group('x1'))
			x2 = int(match.group('x2'))
			y1 = int(match.group('y1'))
			y2 = int(match.group('y2'))

			parsedLines.append((x1,x2,y1,y2))
	
	return parsedLines

def addPoints(x1,x2,y1,y2, points, diagonalsAllowed):
	x = sorted([x1,x2])
	y = sorted([y1,y2])
	
	if x1 == x2:
		for i in range(y[0], y[1] + 1):
			points[(x1, i)] += 1
	elif y1 == y2:
		for i in range(x[0], x[1] + 1):
			points[(i, y1)] += 1
	else:
		if not diagonalsAllowed:
			return
		else:
			factorX = 1
			factorY = 1
			if x1 > x2:
				factorX = -1
			if y1 > y2:
				factorY = -1

			for i in range(x[1] - x[0] + 1):
				points[(x1 + factorX * i, y1 + factorY * i)] += 1

def findMultiples(points):
	multiples = [x for x in points.keys() if points[x] > 1]

	return multiples

def do():
	strInput = readInputFile(5)

	splitInput = strInput.split('\n')

	print(do1(splitInput))
	print(do2(splitInput))

	print('done')


do()