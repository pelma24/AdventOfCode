from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt
import re
from collections import defaultdict
from copy import deepcopy

def do1(start, rules):
	ruleSet = getRules(rules)
	
	resultStr = insert(start, ruleSet, 10)

	occurences = {}
	for value in ruleSet.values():
		if value in occurences:
			continue
		occurences[value] = resultStr.count(value)

	mostCommon = max([x for x in occurences.values()])
	leastCommon = min([x for x in occurences.values()])
	
	return mostCommon - leastCommon

def do2(start, rules):
	ruleSet = getRules(rules)
	
	occurences = insert2(start, ruleSet, 40)
	
	mostCommon = max([x for x in occurences.values()])
	leastCommon = min([x for x in occurences.values()])

	return mostCommon - leastCommon

def getRules(rules):
	ruleSet = {}

	for rule in rules:
		match = re.fullmatch('([A-Z]+) -> ([A-Z])', rule)
		if match:
			ruleSet[(match.groups()[0][0], match.groups()[0][1])] = match.groups()[1]

	return ruleSet

def insert(start, ruleSet, steps):
	for i in range(steps):
		resultStr = ''
		pairs = [(x,y) for x,y in zip(start, start[1:])]

		for first,second in pairs:
			resultStr += first + ruleSet[(first,second)]
		resultStr += second
		start = resultStr

	return resultStr

def insert2(start, ruleSet, steps):
	occurences = defaultdict(lambda: 0)
	pairOccurences = defaultdict(lambda: 0)

	for x in start:
		occurences[x] += 1

	pairs = [(x,y) for x,y in zip(start, start[1:])]
	for (x,y) in pairs:
		pairOccurences[(x,y)] += 1

	newPairOccurences = deepcopy(pairOccurences)
	for _ in range(steps):
		pairOccurences = deepcopy(newPairOccurences)
		for (x,y) in pairOccurences.keys():
			if pairOccurences[(x,y)] == 0:
				continue
			quantity = pairOccurences[(x,y)]
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