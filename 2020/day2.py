from HelperFunctions import inputsplit
import re

def do1(puzzleInput):
    numValidPasswords = 0
    
    for line in puzzleInput:
        match = re.match('([0-9]+)-([0-9]+) ([A-Za-z]): ([A-Za-z]+)', line)

        minCount, maxCount, letter, password = match.groups()

        numberOfOccurences = password.count(letter)

        if numberOfOccurences >= int(minCount) and numberOfOccurences <= int(maxCount):
            numValidPasswords += 1

    return numValidPasswords

def do2(puzzleInput):
    numValidPasswords = 0
    
    for line in puzzleInput:
        match = re.match('([0-9]+)-([0-9]+) ([A-Za-z]): ([A-Za-z]+)', line)

        pos1, pos2, letter, password = match.groups()

        if (password[int(pos1) - 1] == letter and not password[int(pos2) - 1] == letter) or (password[int(pos2) - 1] == letter and not password[int(pos1) - 1] == letter):
            numValidPasswords += 1

    return numValidPasswords


def do():
    with open ('Input/day2.txt') as f:
        strInput = f.read()

    splitInput = inputsplit(strInput, '\n')

    print(do1(splitInput))
    print(do2(splitInput))
    
do()