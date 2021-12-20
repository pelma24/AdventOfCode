from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt
import re
from collections import Counter

rotations = ['x,y,z', '-x,-y,-z', 'y,-x,z', '-y,x,-z', '-x,-y,z', 'x,y,-z', '-y,x,z', 'y,-x,-z', 'z,y,-x', '-z,-y,x', 'y,-z,-x',
'-y,z,x', '-z,-y,-x', 'z,y,x', '-y,z,-x', 'y,-z,x', 'z,-x,-y', '-z,x,y', '-x,-z,-y', 'x,z,y',
'-z,x,-y', 'z,-x,y', 'x,z,-y', '-x,-z,y', 'z,-y,x', '-z,y,-x', '-y,-z,x', 'y,z,-x', '-z,y,x', 'z,-y,-x',
'y,z,x', '-y,-z,-x', 'z,x,y', '-z,-x,-y', 'x,-z,y', '-x,z,-y', '-z,-x,y', 'z,x,-y',
'-x,z,y', 'x,-z,-y', '-x,y,-z', 'x,-y,z', 'y,x,-z', '-y,-x,z', 'x,-y,-z', '-x,y,z', '-y,-x,-z', 'y,x,z']

alreadyInScanner0 = []
scannerPositions = [(0,0,0)]

def do1(splitInput):
	scannerPoints = parseInput(splitInput)
	
	while len(alreadyInScanner0) < len(scannerPoints.keys()) - 1:
		scannerOrientations = findScannerOrientation(scannerPoints)

		addPointsToScanner(scannerOrientations, scannerPoints)
	
	return len(scannerPoints[0])

def do2():
	
	return getLargestScannerDistance()

def getLargestScannerDistance():
	distances = []
	for x1,y1,z1 in scannerPositions:
		for x2,y2,z2 in scannerPositions:
			distance = abs(x1-x2) + abs(y1-y2) + abs(z1-z2)
			distances.append(distance)
	return max(distances)

def getRotatedPoint(point, rotation):
	x,y,z = point
	
	match = re.match('([-]?[xyz]),([-]?[xyz]),([-]?[xyz])', rotation)

	newPoint = []
	for part in match.groups():
		negative = 1
		if len(part) > 1:
			negative = -1
			part = part[1]
		match part:
			case 'x':
				newPoint.append(negative * x)
			case 'y':
				newPoint.append(negative * y)
			case 'z':
				newPoint.append(negative * z)
	return (newPoint[0], newPoint[1], newPoint[2])

def addPointsToScanner(scannerOrientations, scannerPoints):
	for scannerNr,position,rotation in scannerOrientations:
		if scannerNr in alreadyInScanner0:
			continue
		xPos,yPos,zPos = position
		scannerPositions.append(position)

		firstScanner = set(scannerPoints[0])
		secondScanner = scannerPoints[scannerNr]

		for point in secondScanner:
			x,y,z = getRotatedPoint(point, rotation)
			newPoint = (xPos - x, yPos - y, zPos - z)
			firstScanner.add(newPoint)
		
		scannerPoints[0] = list(firstScanner)
		alreadyInScanner0.append(scannerNr)

def findScannerOrientation(scannerPoints):
	scannerOrientation = []
	scanner1 = scannerPoints[0]
	for secondScanner,scanner2 in scannerPoints.items():
		if secondScanner == 0 or secondScanner in alreadyInScanner0:
			continue
		for rotation in rotations:
			newPoints = Counter()
			for point1 in scanner1:
				x1,y1,z1 = point1
				for point2 in scanner2:
					x2,y2,z2 = getRotatedPoint(point2, rotation)

					newPoint = (x1 + x2, y1 + y2, z1 + z2)
					newPoints[newPoint] += 1
			
			result = [x for x in newPoints.keys() if newPoints[x] > 10]
			if result:
				scannerOrientation.append((secondScanner, result[0], rotation))

	return scannerOrientation

def parseInput(splitInput):
	scannerPoints = {}
	for scanner in splitInput:
		scanner = scanner.split('\n')
		match = re.match('--- scanner ([0-9]+) ---', scanner[0])
		scannerNumber = int(match.groups()[0])
		scannerPoints[scannerNumber] = []
		for line in scanner[1:]:
			x,y,z = line.split(',')
			x = int(x)
			y = int(y)
			z = int(z)
			scannerPoints[scannerNumber].append((x,y,z))

	return scannerPoints

def do():
	strInput = readInputFile(19)

	splitInput = strInput.split('\n\n')

	print(do1(splitInput))
	print(do2())

	print('done')


do()