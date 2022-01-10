from functools import cache

inputDict = {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10}

def do1():

	global inputDict
	k = [1, 10, 2, 5, 6, 0, 16, 12, 15, 7, 6, 5, 6, 15]
	special = {3: 10, 7: 11, 8: 7, 10: 13, 11: 0, 12: 11, 13: 0, }

	for position in range(1,14):
		newDict = inputDict.copy()
		for oldW, z in inputDict.items():
			if position in special.keys():
				w = (z % 26) - special[position]
				if w < 1 or w > 9:
					del newDict[oldW]
					continue
				znew = z // 26
				newDict[oldW * 10 + w] = znew	
			else:
				for w in range(1,10):
					znew = 26 * z + w + k[position]
					newDict[oldW * 10 + w] = znew
			del newDict[oldW]
		inputDict = newDict.copy()

	possibleValues = [x for x in inputDict.keys() if inputDict[x] == 0]

	return max(possibleValues)			

def do2():
	global inputDict
	
	possibleValues = [x for x in inputDict.keys() if inputDict[x] == 0]

	return min(possibleValues)

def do():
	
	print(do1())
	print(do2())

	print('done')


do()