from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt
import re
from copy import deepcopy

def do1(dots, foldInstructions):
	points,instructions = getPointsAndInstructions(dots, foldInstructions)

	firstInstruction = instructions[0]

	points = fold(points, [firstInstruction])				

	return len(points)

def do2(dots, foldInstructions):
	points,instructions = getPointsAndInstructions(dots, foldInstructions)

	points = fold(points, instructions)		

	showPoints(points)

	return len(points)

def fold(points, instructions):
	for instruction in instructions:
		newPoints = set()
		match instruction:
			case ('x', value):
				for x,y in points:
					if x > value:
						newPoints.add((value - (x - value), y))
					else:
						newPoints.add((x,y))
			case ('y', value):
				for x,y in points:
					if y > value:
						newPoints.add((x, value - (y - value)))
					else:
						newPoints.add((x,y))
		points = deepcopy(newPoints)
	
	return points

def showPoints(points):
	maxX = max([x for x,y in points])
	maxY = max([y for x,y in points])

	grid = [['.' for i in range(maxX + 1)] for j in range(maxY + 1)]
	
	for x,y in points:
		grid[y][x] = '#'

	for line in grid:
		print(line)

def getPointsAndInstructions(dots, foldInstructions):
	points = set()
	instructions = []

	for dot in dots:
		x,y = convertToInt(dot.split(','))
		points.add((x,y))

	#foldInstructions
	for line in foldInstructions:
		match = re.fullmatch('fold along ([x,y])=([0-9]+)', line)
		if match:
			coordinate = match.groups()[0]
			value = int(match.groups()[1])
			instructions.append((coordinate,value))
	
	return points,instructions

def do():
	strInput = readInputFile(13)

	dots,foldInstructions = strInput.split('\n\n')
	dots = dots.split('\n')
	foldInstructions = foldInstructions.split('\n')

	print(do1(dots, foldInstructions))
	print(do2(dots, foldInstructions))

	print('done')


do()