from HelperFunctions import inputsplit
import re
from HelperFunctions import convertToInt
from copy import deepcopy

def do1(puzzleInput):
    rules = getRules(puzzleInput[0])
    messages = puzzleInput[1].split('\n')

    result = checkMessages(messages, rules, 0)

    return result

def do2(puzzleInput):
    rules = getRules(puzzleInput[0])
    messages = puzzleInput[1].split('\n')

    result = checkMessages2(messages, rules, 0)

    return result

def getRules(puzzleInput):
    rules = {}
    missing = {}
    splitInput = puzzleInput.split('\n')
    newInput = deepcopy(splitInput)
    for rule in splitInput:
        match = re.match('([0-9]+): "(.+)"', rule)
        if match:
            rules[int(match.groups()[0])] = [match.groups()[1]]
            newInput.remove(rule)
        else:
            match = re.match('([0-9]+): (.+)', rule)
            missing[int(match.groups()[0])] = match.groups()[1]
        
    ls = deepcopy(missing)
    for key in ls.keys():
        getRule(key, rules, missing)

    return rules

def getRule(rule, rules, missing):
    if rule in rules.keys():
        return rules[rule]
    
    match = re.fullmatch('(([ ]?[0-9]+)+)', missing[rule])
    if match:
        subrules = convertToInt(match.groups()[0].split(' '))
        result = getResult(subrules, rules, missing)
        rules[rule] = result
    else:
        match = re.fullmatch('(([ ]?[0-9]+)+) \| (([ ]?[0-9]+)+)', missing[rule])
        if match:
            alternatives = []
            alternatives.append(match.groups()[0])
            alternatives.append(match.groups()[2])
            completeResult = []
            for alternative in alternatives:
                subrules = convertToInt(alternative.split(' '))
                result = getResult(subrules, rules, missing)
                completeResult += result
            rules[rule] = completeResult
    
    del missing[rule]
    return rules[rule]
    
def getResult(subrules, rules, missing):
    result = []
    for subrule in subrules:
        alternatives = getRule(subrule, rules, missing)
        if not result:
            result = deepcopy(alternatives)
        else:
            tmp = []
            for partResult in result:
                for alternative in alternatives:
                    tmp.append(partResult + alternative)
            result = tmp
    return result

def checkMessages(messages, rules, ruleNumber):
    count = 0
    for message in messages:
        if message in rules[ruleNumber]:
            count += 1

    return count

def checkMessages2(messages, rules, ruleNumber):
    blobSize = len(rules[42][0])
    
    count = 0
    for message in messages:
        if message in rules[ruleNumber]:
            count += 1
        else:
            count42 = 0
            count31 = 0
            successful = True
            for position in range(0, len(message) - blobSize + 1, blobSize):
                messageSlice = message[position:(position + blobSize)]
                if messageSlice in rules[42]:
                    count42 += 1
                    if count31:
                        successful = False
                        break
                elif messageSlice in rules[31]:
                    count31 += 1
            if successful and count31 and count42 - count31 > 0:
                count += 1

    return count


def do():
    with open ('Input/day19.txt') as f:
        strInput = f.read()

    splitInput = inputsplit(strInput, '\n\n')
    
    print(do1(splitInput))
    print(do2(splitInput))
    
do()