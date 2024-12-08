from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt
from collections import defaultdict
import itertools

def createMap(splitInput):
	map = {}
	antennas = defaultdict(list)

	for y,line in enumerate(splitInput):
		for x,value in enumerate(line):
			if value != '.':
				antennas[value].append((x,y))
			map[(x,y)] = value

	return map,antennas

def do1(map, antennas):
	antinodes = set()

	for antennaType in antennas.keys():
		combinations = itertools.combinations(antennas[antennaType], 2)

		for first,second in combinations:
			x1,y1 = first
			x2,y2 = second
			distance = ((x2-x1),(y2-y1))
			antinode1 = (x1 - distance[0], y1 - distance[1])
			antinode2 = (x2 + distance[0], y2 + distance[1])

			if antinode1 in map.keys():
				antinodes.add(antinode1)
			if antinode2 in map.keys():
				antinodes.add(antinode2)
	
	return len(antinodes)

def do2(map, antennas):
	antinodes = set()
	for antennaType in antennas.keys():
		combinations = itertools.combinations(antennas[antennaType], 2)

		for first,second in combinations:
			x1,y1 = first
			x2,y2 = second
			distance = ((x2-x1),(y2-y1))
			currentPosition = first
			while currentPosition in map:
				antinodes.add(currentPosition)
				currentPosition = (currentPosition[0] - distance[0], currentPosition[1] - distance[1])
			currentPosition = second
			while currentPosition in map:
				antinodes.add(currentPosition)
				currentPosition = (currentPosition[0] + distance[0], currentPosition[1] + distance[1])
	
	return len(antinodes)

def do():
	strInput = readInputFile(8)

	map,antennas = createMap(strInput.split('\n'))

	print(do1(map, antennas))
	print(do2(map, antennas))

	print('done')


do()