from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt
import re

def do1(splitInput):
	pairs,sensors,beacons = extractSensorsAndBeacons(splitInput)

	impossiblePoints = set()
	y = 2000000

	for sensor,beacon in pairs.items():
		sensorX,sensorY = sensor
		distance = manhattanDistance(sensor,beacon)
		impossible = [(x,y) for x in range(sensorX-distance, sensorX+distance+1) if manhattanDistance(sensor,(x,y)) <= distance]
		impossiblePoints = impossiblePoints.union(set(impossible))

	sumImpossible = len([x for x in impossiblePoints if x[1] == y])
	sumBeacons = len([x for x in beacons if x[1] == y])
	sumSensors = len([x for x in sensors if x[1] == y])

	return sumImpossible - sumBeacons - sumSensors

def do2(splitInput):
	pairs,sensors,beacons = extractSensorsAndBeacons(splitInput)
	distances = {}

	for sensor,beacon in pairs.items():
		distances[sensor] = manhattanDistance(sensor,beacon)

	for sensor in sensors:
		sensorX,sensorY = sensor
		possiblePoints = []
		distance = distances[sensor]
		x = distance + 1
		y = 0
		while -distance - 1 <= x <= distance + 1:
			possiblePoints.append((sensorX + x, sensorY + y))
			x -= 1
			if x < 0:
				y -= 1
			else:
				y += 1
		for point in possiblePoints:
			pointX,pointY = point
			if not 0 <= pointX <= 4000000 or not 0 <= pointY <= 4000000:
				continue
			possible = True
			for otherSensor in sensors:
				if otherSensor == sensor:
					continue
				if manhattanDistance(point,otherSensor) <= distances[otherSensor]:
					possible = False
					break
			if possible:
				return point[0] * 4000000 + point[1]



def manhattanDistance(a,b):
	ax,ay = a
	bx,by = b
	return abs(ax-bx) + abs(ay-by)

def extractSensorsAndBeacons(splitInput):
	pairs = {}
	
	sensors = set()
	beacons = set()
	
	for line in splitInput:
		match = re.match('Sensor at x=(?P<xSensor>[-]?\d+), y=(?P<ySensor>[-]?\d+): closest beacon is at x=(?P<xBeacon>[-]?\d+), y=(?P<yBeacon>[-]?\d+)', line)
		sensorPos = (int(match.group('xSensor')), int(match.group('ySensor')))
		beaconPos = (int(match.group('xBeacon')), int(match.group('yBeacon')))

		pairs[sensorPos] = beaconPos
		sensors.add(sensorPos)
		beacons.add(beaconPos)
	
	return pairs,sensors,beacons

def do():
	strInput = readInputFile(15)
	
	splitInput = strInput.split('\n')

	print(do1(splitInput))
	print(do2(splitInput))

	print('done')


do()