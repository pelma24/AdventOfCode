from functools import cache
from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt
from collections import defaultdict
from copy import deepcopy

inputDict = {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10}

def do1(splitInput):

	global inputDict
	k1 = [1, 1, 1, 26, 1, 1, 1, 26, 26, 1, 26, 26, 26, 26]
	k2 = [26 for i in range(14)]
	k3 = [1, 10, 2, 5, 6, 0, 16, 12, 15, 7, 6, 5, 6, 15]

	for position in range(1,14):
		newDict = inputDict.copy()
		for oldW, z in inputDict.items():
			if position == 3:
				w = (z % 26) - 10
				if w < 1 or w > 9:
					del newDict[oldW]
					continue
				znew = z // 26
				newDict[oldW * 10 + w] = znew
			elif position == 7:
				w = (z % 26) - 11
				if w < 1 or w > 9:
					del newDict[oldW]
					continue
				znew = z // 26
				newDict[oldW * 10 + w] = znew
			elif position == 8:
				w = (z % 26) - 7
				if w < 1 or w > 9:
					del newDict[oldW]
					continue
				znew = z // 26
				newDict[oldW * 10 + w] = znew
			elif position == 10:
				w = (z % 26) - 13
				if w < 1 or w > 9:
					del newDict[oldW]
					continue
				znew = z // 26
				newDict[oldW * 10 + w] = znew	
			elif position == 11:
				w = (z % 26)
				if w < 1 or w > 9:
					del newDict[oldW]
					continue
				znew = z // 26
				newDict[oldW * 10 + w] = znew	
			elif position == 12:
				w = (z % 26) - 11
				if w < 1 or w > 9:
					del newDict[oldW]
					continue
				znew = z // 26
				newDict[oldW * 10 + w] = znew	
			elif position == 13:
				w = (z % 26)
				if w < 1 or w > 9:
					del newDict[oldW]
					continue
				znew = z // 26
				newDict[oldW * 10 + w] = znew	
			else:
				for w in range(1,10):
					znew = calculateZ(z, w, k1[position], k2[position], k3[position])
					newDict[oldW * 10 + w] = znew
			del newDict[oldW]
		inputDict = newDict.copy()

	possibleValues = [x for x in inputDict.keys() if inputDict[x] == 0]

	return max(possibleValues)			

@cache
def calculateZ(z, w, k1, k2, k3):
	z = (z // k1) * k2 + w + k3
	return z

def do2(splitInput):
	global inputDict
	
	possibleValues = [x for x in inputDict.keys() if inputDict[x] == 0]

	return min(possibleValues)

def do():
	strInput = readInputFile(24)

	splitInput = strInput.split('\n')

	print(do1(splitInput))
	print(do2(splitInput))

	print('done')


do()