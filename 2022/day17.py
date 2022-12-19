from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt

rocks = {0:[(0,0),(1,0),(2,0),(3,0)], 1:[(1,0),(0,1),(1,1),(2,1),(1,2)], 2:[(0,0),(1,0),(2,0),(2,1),(2,2)], 3:[(0,0),(0,1),(0,2),(0,3)], 4:[(0,0),(0,1),(1,0),(1,1)]}

def do1(movement):
	rockPositions = set([(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0)])
	position = 0
	floor = 0
	fallenRocks = 0
	while fallenRocks <	2022:
		rock = rocks[fallenRocks % 5]
		leftCorner = (2,floor + 4)
		falling = True
		while falling:
			leftCorner = getPushed(movement[position], rockPositions, leftCorner, rock)
			position = (position + 1) % len(movement) 
			falling,leftCorner = fallDown(leftCorner, rockPositions, rock)
		fallenRocks += 1
		leftCornerX,leftCornerY = leftCorner
		for rockPartX,rockPartY in rock:
			rockPositions.add((leftCornerX + rockPartX, leftCornerY + rockPartY))
			floor = max(floor, leftCornerY + rockPartY)
	return max([y for (x,y) in rockPositions])

def getPushed(movement, rockPositions, leftCorner, rock):
	leftCornerX,leftCornerY = leftCorner
	match movement:
		case '<':
			leftCornerX -= 1
			for rockPartX,rockPartY in rock:
				if (leftCornerX + rockPartX,leftCornerY + rockPartY) in rockPositions or leftCornerX + rockPartX < 0:
					return leftCorner
			return (leftCornerX,leftCornerY)
		case '>':
			leftCornerX += 1
			for rockPartX,rockPartY in rock:
				if (leftCornerX + rockPartX,leftCornerY + rockPartY) in rockPositions or leftCornerX + rockPartX > 6:
					return leftCorner
			return (leftCornerX,leftCornerY)

def fallDown(leftCorner, rockPositions, rock):
	leftCornerX,leftCornerY = leftCorner
	leftCornerY -= 1
	for rockPartX,rockPartY in rock:
		if (leftCornerX + rockPartX,leftCornerY + rockPartY) in rockPositions:
			return False,leftCorner
	return True,(leftCornerX,leftCornerY)

def do2(movement):
	#cycle starts at position = 9 with 1720 fallen rocks and floor height = 2691, floor difference from cycle to cycle is +2728 with 1725 new rocks
	#missing rocks to reach 1000000000000 are 1605 which have a height of 2524 

	return 2691 + (int((1000000000000-1720) / 1725)) * 2728 + 2524

def do():
	strInput = readInputFile(17)

	print(do1(strInput))
	print(do2(strInput))

	print('done')


do()