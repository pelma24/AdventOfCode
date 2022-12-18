from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt

def do1(splitInput):
	cubes = extractCubes(splitInput)
	openSides = 0
	for x,y,z in cubes:
		sides = 6
		for oX,oY,oZ in cubes:
			if oX == x and oY == y and abs(oZ - z) == 1:
				sides -= 1
			elif oX == x and oZ == z and abs(oY - y) == 1:
				sides -= 1
			elif oY == y and oZ == z and abs(oX - x) == 1:
				sides -= 1
		openSides += sides		

	return openSides

def do2(splitInput):
	cubes = extractCubes(splitInput)
	maxX = max(x for x,y,z in cubes) + 1
	maxY = max(y for x,y,z in cubes) + 1
	maxZ = max(z for x,y,z in cubes) + 1

	sides = 0
	newAir = set()
	newAir.add((maxX,maxY,maxZ))
	visitedAir = set()

	while len(newAir) > 0:
		cube = newAir.pop()
		cubeNeighbors,airNeighbors = getNeighbors(cube,cubes,maxX,maxY,maxZ,visitedAir)
		sides += len(cubeNeighbors)
		newAir = newAir.union(airNeighbors)
		visitedAir.add(cube)
	return sides

def extractCubes(splitInput):
	cubes = set()
	for line in splitInput:
		cube = [int(x) for x in line.split(',')]
		cubes.add((cube[0], cube[1], cube[2]))
	return cubes

def getNeighbors(cube, cubes, maxX, maxY, maxZ, visitedAir):
	cubeNeighbors = set()
	airNeighbors = set()
	cubeX,cubeY,cubeZ = cube
	if cubeX - 1 >= -1:
		if (cubeX - 1, cubeY, cubeZ) in cubes:
			cubeNeighbors.add((cubeX - 1, cubeY, cubeZ))
		elif (cubeX - 1, cubeY, cubeZ) not in visitedAir:
			airNeighbors.add((cubeX - 1, cubeY, cubeZ))
	if cubeX + 1 <= maxX:
		if (cubeX + 1, cubeY, cubeZ) in cubes:
			cubeNeighbors.add((cubeX + 1, cubeY, cubeZ))
		elif (cubeX + 1, cubeY, cubeZ) not in visitedAir:
			airNeighbors.add((cubeX + 1, cubeY, cubeZ))
	if cubeY - 1 >= -1:
		if (cubeX, cubeY - 1, cubeZ) in cubes:
			cubeNeighbors.add((cubeX, cubeY - 1, cubeZ))
		elif (cubeX, cubeY - 1, cubeZ) not in visitedAir:
			airNeighbors.add((cubeX, cubeY - 1, cubeZ))
	if cubeY + 1 <= maxY:
		if (cubeX, cubeY + 1, cubeZ) in cubes:
			cubeNeighbors.add((cubeX, cubeY + 1, cubeZ))
		elif (cubeX, cubeY + 1, cubeZ) not in visitedAir:
			airNeighbors.add((cubeX, cubeY + 1, cubeZ))
	if cubeZ - 1 >= -1:
		if (cubeX, cubeY, cubeZ - 1) in cubes:
			cubeNeighbors.add((cubeX, cubeY, cubeZ - 1))
		elif (cubeX, cubeY, cubeZ - 1) not in visitedAir:
			airNeighbors.add((cubeX, cubeY, cubeZ - 1))
	if cubeZ + 1 <= maxZ:
		if (cubeX, cubeY, cubeZ + 1) in cubes:
			cubeNeighbors.add((cubeX, cubeY, cubeZ + 1))
		elif (cubeX, cubeY, cubeZ + 1) not in visitedAir:
			airNeighbors.add((cubeX, cubeY, cubeZ + 1))
	
	return cubeNeighbors,airNeighbors


def do():
	strInput = readInputFile(18)

	splitInput = strInput.split('\n')

	print(do1(splitInput))
	print(do2(splitInput))

	print('done')


do()