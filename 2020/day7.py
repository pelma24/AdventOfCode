from HelperFunctions import inputsplit
import re

bagCounts = {}

def do1(puzzleInput):
    
    bags = getBags(puzzleInput, False)

    bagsToHoldAShinyGoldBag = []

    for bag in bags.keys():
        if containsShinyBag(bags, bag):
            bagsToHoldAShinyGoldBag.append(bag)

    return len(bagsToHoldAShinyGoldBag)

def do2(puzzleInput):
    
    bags = getBags(puzzleInput, True)

    return bagCount('shiny gold', bags)

def getBags(puzzleInput, numberIsImportant):
    bags = {}
    
    for line in puzzleInput:
        match1 = re.search('(.+) bags contain', line)
        match2 = re.findall('([0-9]+) (\D+) bag[s]?[\.|, ]', line)

        bag = match1.groups()[0]
        bags[bag] = []
        for innerBag in match2:
            if numberIsImportant:
                for _ in range(int(innerBag[0])):
                    bags[bag].append(innerBag[1])
            else:
                bags[bag].append(innerBag[1])
    return bags

def bagCount(bag, bags):    
    if bag in bagCounts.keys():
        return bagCounts[bag]

    count = len(bags[bag])
    for innerbag in bags[bag]:
        count += bagCount(innerbag, bags)
    
    bagCounts[bag] = count

    return count

def containsShinyBag(bags, bag):

    if 'shiny gold' in bags[bag]:
        return True
    for innerBag in bags[bag]:
        if containsShinyBag(bags, innerBag):
            return True
    return False

def do():
    with open ('Input/day7.txt') as f:
        strInput = f.read()

    splitInput = inputsplit(strInput, '\n')

    print(do1(splitInput))
    print(do2(splitInput))
    
do()