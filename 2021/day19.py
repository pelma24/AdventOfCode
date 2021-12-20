from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt
import re
from collections import Counter, defaultdict

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

def do2(splitInput):
	scannerPoints = parseInput(splitInput)
	
	while len(alreadyInScanner0) < len(scannerPoints.keys()) - 1:
		scannerOrientations = findScannerOrientation(scannerPoints)

		addPointsToScanner(scannerOrientations, scannerPoints)

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
	
	match rotation:
		case 'x,y,z':
			return (x,y,z)
		case '-x,-y,-z':
			return (-x,-y,-z)
		case 'y,-x,z':
			return (y,-x,z)
		case '-y,x,-z':
			return (-y,+x,-z)
		case '-x,-y,z':
			return (-x,-y,z)
		case 'x,y,-z':
			return (x,y,-z)
		case '-y,x,z':
			return (-y,x,z)
		case 'y,-x,-z':
			return (y,-x,-z)
		case 'z,y,-x':
			return (z,y,-x)
		case '-z,-y,x':
			return (-z,-y,x)
		case 'y,-z,-x':
			return (y,-z,-x)
		case '-y,z,x':
			return (-y,z,x)
		case '-z,-y,-x':
			return (-z,-y,-x)
		case 'z,y,x':
			return (z,y,x)
		case '-y,z,-x':
			return (-y,z,-x)
		case 'y,-z,x':
			return (y,-z,x)
		case 'z,-x,-y':
			return (z,-x,-y)
		case '-z,x,y':
			return (-z,x,y)
		case '-x,-z,-y':
			return (-x,-z,-y)
		case 'x,z,y':
			return (x,z,y)
		case '-z,x,-y':
			return (-z,x,-y)
		case 'z,-x,y':
			return (z,-x,y)
		case 'x,z,-y':
			return (x,z,-y)
		case '-x,-z,y':
			return (-x,-z,y)
		case 'z,-y,x':
			return (z,-y,x)
		case '-z,y,-x':
			return (-z,y,-x)
		case '-y,-z,x':
			return (-y,-z,x)
		case 'y,z,-x':
			return (y,z,-x)
		case '-z,y,x':
			return (-z,y,x)
		case 'z,-y,-x':
			return (z,-y,-x)
		case 'y,z,x':
			return (y,z,x)
		case '-y,-z,-x':
			return (-y,-z,-x)
		case 'z,x,y':
			return (z,x,y)
		case '-z,-x,-y':
			return (-z,-x,-y)
		case 'x,-z,y':
			return (x,-z,y)
		case '-x,z,-y':
			return (-x,z,-y)
		case '-z,-x,y':
			return (-z,-x,y)
		case 'z,x,-y':
			return (z,x,-y)
		case '-x,z,y':
			return (-x,z,y)
		case 'x,-z,-y':
			return (x,-z,-y)
		case '-x,y,-z':
			return (-x,y,-z)
		case 'x,-y,z':
			return (x,-y,z)
		case 'y,x,-z':
			return (y,x,-z)
		case '-y,-x,z':
			return (-y,-x,z)
		case 'x,-y,-z':
			return (x,-y,-z)
		case '-x,y,z':
			return (-x,y,z)
		case '-y,-x,-z':
			return (-y,-x,-z)
		case 'y,x,z':
			return (y,x,z)

def addPointsToScanner(scannerOrientations, scannerPoints):
	for scannerNr,position,rotation in scannerOrientations[0]:
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
	scannerOrientation = defaultdict(lambda: [])
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
				scannerOrientation[0].append((secondScanner, result[0], rotation))

	return scannerOrientation

def getRotations(point):
	rotations = set()
	x,y,z = point
	rotations.add((x,y,z))
	rotations.add((y,-x,z))
	rotations.add((-x,-y,z))
	rotations.add((-y,x,z))
	rotations.add((z,y,-x))	
	rotations.add((y,-z,-x))
	rotations.add((-z,-y,-x))
	rotations.add((-y,z,-x))
	rotations.add((z,-x,-y))
	rotations.add((-x,-z,-y))
	rotations.add((-z,x,-y))
	rotations.add((x,z,-y))
	rotations.add((z,-y,x))
	rotations.add((-y,-z,x))
	rotations.add((-z,y,x))
	rotations.add((y,z,x))
	rotations.add((z,x,y))
	rotations.add((x,-z,y))
	rotations.add((-z,-x,y))
	rotations.add((-x,z,y))
	rotations.add((-x,y,-z))
	rotations.add((y,x,-z))
	rotations.add((x,-y,-z))
	rotations.add((-y,-x,-z))

	oldPoints = rotations.copy()
	for point in oldPoints:
		x,y,z = point
		newPoint = (-x,-y,-z)
		rotations.add(newPoint)
	return rotations

def rotateX(point):
	x,y,z = point
	return (x,-z,y)

def rotateY(point):
	x,y,z = point
	return (z,y,-x)

def rotateZ(point):
	x,y,z = point
	return (-y,x,z)

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

def getNeighborDistances(points):
	neighborDistances = {}

	for point1 in points:
		neighborDistances[point1] = []
		for point2 in points:
			if point1 == point2:
				continue
			x1,y1,z1 = point1
			x2,y2,z2 = point2
			distance = abs(x1-x2) + abs(y1-y2) + abs(z1-z2)
			neighborDistances[point1].append(distance)
	
	return neighborDistances

def do():
	strInput = readInputFile(19)
	#strInput = readExampleInput(19)

	splitInput = strInput.split('\n\n')

	#print(do1(splitInput))
	print(do2(splitInput))

	print('done')


do()