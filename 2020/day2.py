from HelperFunctions import inputsplit
import re

def do1(puzzleInput):
    numValidPasswords = 0
    
    for line in puzzleInput:
        match = re.match('([0-9]+)-([0-9]+) ([A-Za-z]): ([A-Za-z]+)', line)

        minCount, maxCount, letter, password = [int(x) if x.isnumeric() else x for x in match.groups()]

        numberOfOccurences = password.count(letter)

        if  minCount <= numberOfOccurences <= maxCount:
            numValidPasswords += 1

    return numValidPasswords

def do2(puzzleInput):
    numValidPasswords = 0
    
    for line in puzzleInput:
        match = re.match('([0-9]+)-([0-9]+) ([A-Za-z]): ([A-Za-z]+)', line)

        pos1, pos2, letter, password = [int(x) - 1 if x.isnumeric() else x for x in match.groups()]

        if (password[pos1] == letter and not password[pos2] == letter) or (password[pos2] == letter and not password[pos1] == letter):
            numValidPasswords += 1

    return numValidPasswords


def do():
    with open ('Input/day2.txt') as f:
        strInput = f.read()

    splitInput = inputsplit(strInput, '\n')

    print(do1(splitInput))
    print(do2(splitInput))
    
do()