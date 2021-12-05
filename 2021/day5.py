from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt
import re
from collections import defaultdict

def do1(splitInput):
	points = defaultdict(lambda: 0)

	for line in splitInput:
		match = re.fullmatch('(?P<x1>[0-9]+),(?P<y1>[0-9]+) -> (?P<x2>[0-9]+),(?P<y2>[0-9]+)', line)
		if match:
			x1 = int(match.group('x1'))
			x2 = int(match.group('x2'))
			y1 = int(match.group('y1'))
			y2 = int(match.group('y2'))

			addPoints(x1,x2,y1,y2, points, 1)
		else:
			print('Oops')
	multiples = findMultiples(points)
	return len(multiples)

def do2(splitInput):
	points = defaultdict(lambda: 0)

	for line in splitInput:
		match = re.fullmatch('(?P<x1>[0-9]+),(?P<y1>[0-9]+) -> (?P<x2>[0-9]+),(?P<y2>[0-9]+)', line)
		if match:
			x1 = int(match.group('x1'))
			x2 = int(match.group('x2'))
			y1 = int(match.group('y1'))
			y2 = int(match.group('y2'))

			addPoints(x1,x2,y1,y2, points, 2)
		else:
			print('Oops')
	multiples = findMultiples(points)
	return len(multiples)

def addPoints(x1,x2,y1,y2, points, part):
	x = sorted([x1,x2])
	y = sorted([y1,y2])
	
	if x1 == x2:
		for i in range(y[0], y[1] + 1):
			points[(x1, i)] += 1
	elif y1 == y2:
		for i in range(x[0], x[1] + 1):
			points[(i, y1)] += 1
	else:
		if part == 1:
			return
		else:
			if x1 < x2:
				if y1 < y2:
					for i in range(x2 - x1 + 1):
						points[(x1 + i, y1 + i)] += 1
				else:
					for i in range(x2 - x1 + 1):
						points[(x1 + i, y1 - i)] += 1
			else:
				if y1 < y2:
					for i in range(x1 - x2 + 1):
						points[(x1 - i, y1 + i)] += 1
				else:
					for i in range(x1 - x2 + 1):
						points[(x1 - i, y1 - i)] += 1
				
		

def findMultiples(points):
	multiples = [x for x in points.keys() if points[x] > 1]

	return multiples

def do():
	strInput = readInputFile(5)
	#strInput = readExampleInput(5)

	splitInput = strInput.split('\n')

	print(do1(splitInput))
	print(do2(splitInput))

	print('done')


do()