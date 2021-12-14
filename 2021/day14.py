from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt
import re
from collections import Counter
from copy import deepcopy
from itertools import pairwise

def do1(start, rules):
	ruleSet = getRules(rules)
	
	occurences = insert(start, ruleSet, 10)

	mostCommon = max(occurences.values())
	leastCommon = min(occurences.values())
	
	return mostCommon - leastCommon

def do2(start, rules):
	ruleSet = getRules(rules)
	
	occurences = insert(start, ruleSet, 40)
	
	mostCommon = max(occurences.values())
	leastCommon = min(occurences.values())

	return mostCommon - leastCommon

def getRules(rules):
	ruleSet = {}

	for rule in rules:
		match = re.fullmatch('([A-Z]+) -> ([A-Z])', rule)
		if match:
			ruleSet[(match.groups()[0][0], match.groups()[0][1])] = match.groups()[1]

	return ruleSet

def insert(start, ruleSet, steps):
	occurences = Counter()
	pairOccurences = Counter()

	for x in start:
		occurences[x] += 1

	pairs = pairwise(start)
	for pair in pairs:
		pairOccurences[pair] += 1

	newPairOccurences = deepcopy(pairOccurences)
	for _ in range(steps):
		pairOccurences = deepcopy(newPairOccurences)
		for (x,y),quantity in pairOccurences.items():
			if quantity == 0:
				continue
			newElement = ruleSet[(x,y)]
			occurences[newElement] += quantity

			newPairOccurences[(x,newElement)] += quantity
			newPairOccurences[(newElement, y)] += quantity
			newPairOccurences[(x,y)] -= quantity

	return occurences

def do():
	strInput = readInputFile(14)

	start,rules = strInput.split('\n\n')
	rules = rules.split('\n')

	print(do1(start, rules))
	print(do2(start, rules))

	print('done')


do()