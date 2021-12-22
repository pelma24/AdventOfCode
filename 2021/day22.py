from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt
import re

def do1(splitInput):
	points = set()
	for line in splitInput:
		onorOff,xmin,xmax,ymin,ymax,zmin,zmax = getLine(line)

		if xmin < -50 or xmax > 50 or ymin < -50 or ymax > 50 or zmin < -50 or zmax > 50:
			continue

		for x in range(xmin, xmax + 1):
			for y in range(ymin, ymax + 1):
				for z in range(zmin, zmax + 1):
					match onorOff:
						case 'on':
							points.add((x,y,z))
						case 'off':
							if (x,y,z) in points:
								points.remove((x,y,z))
						case _:
							print('missing implementation')	
	return len(points)

def do2(splitInput):
	processed = []

	for line in splitInput:
		onorOff,xmin,xmax,ymin,ymax,zmin,zmax = getLine(line)
		cube = (xmin,xmax,ymin,ymax,zmin,zmax)

		newCubes = []
		
		for otherCube,activation in processed:
			intersectionCube = intersectCubes(cube, otherCube)
			if intersectionCube:
				if activation == 'on':
					newActivation = 'off'
				else:
					newActivation = 'on'
				newCubes.append((intersectionCube, newActivation))
			
		if onorOff == 'on':
			processed.append((cube, onorOff))	
		processed += newCubes

	on = 0

	for cube,activation in processed:
		volume = getCubeVolume(cube)
		if activation == 'on':
			on += volume
		else:
			on -= volume
	return on

def getCubeVolume(cube):
	if not cube:
		return 0
	xmin,xmax,ymin,ymax,zmin,zmax = cube

	return abs(xmax + 1 - xmin) * abs(ymax + 1 - ymin) * abs(zmax + 1 - zmin)

def intersectCubes(cube1, cube2):
	xmin1,xmax1,ymin1,ymax1,zmin1,zmax1 = cube1
	xmin2,xmax2,ymin2,ymax2,zmin2,zmax2 = cube2

	if xmin1 < xmin2:
		if xmin2 > xmax1:
			return []
	else:
		if xmin1 > xmax2:
			return []
	if ymin1 < ymin2:
		if ymin2 > ymax1:
			return []
	else:
		if ymin1 > ymax2:
			return []
	if zmin1 < zmin2:
		if zmin2 > zmax1:
			return []
	else:
		if zmin1 > zmax2:
			return []
	
	ixmin = max(xmin1, xmin2)
	iymin = max(ymin1, ymin2)
	izmin = max(zmin1, zmin2)

	ixmax = min(xmax1, xmax2)
	iymax = min(ymax1, ymax2)
	izmax = min(zmax1, zmax2)	

	return [ixmin,ixmax,iymin,iymax,izmin,izmax]

def getLine(line):
	match = re.findall('(on|off) x=(-?[0-9]+)\.\.(-?[0-9]+)',line)
	onOrOff,xmin,xmax = match[0]
	xmin,xmax = convertToInt((xmin,xmax))

	match = re.findall('y=(-?[0-9]+)\.\.(-?[0-9]+)',line)
	ymin,ymax = convertToInt(match[0])

	match = re.findall('z=(-?[0-9]+)\.\.(-?[0-9]+)',line)
	zmin,zmax = convertToInt(match[0])

	return onOrOff,xmin,xmax,ymin,ymax,zmin,zmax

def do():
	strInput = readInputFile(22)

	splitInput = strInput.split('\n')

	print(do1(splitInput))
	print(do2(splitInput))

	print('done')


do()