from HelperFunctions import inputsplit
import re

def do1(puzzleInput):
    sum = 0
    for line in puzzleInput:
        sum += calculate(line, sumUp)

    return sum

def do2(puzzleInput):
    sum = 0
    for line in puzzleInput:
        sum += calculate(line, sumWithLineBeforeDot)

    return sum

def calculate(line, sumFunction):
    matches = re.findall('\([0-9 \+\*]+\)', line)
    while matches:
        match = matches[0]
        result = sumFunction(match[1:-1])
        line = line.replace(match, str(result), 1)
        matches = re.findall('\([0-9 \+\*]+\)', line)
    return sumFunction(line)

def sumWithLineBeforeDot(line):
    matches = re.findall('[\( ]?([0-9]+ \+ [0-9]+)[ \)]?', line)
    while matches:
        match = matches[0]
        result = sumUp(match)
        line = line.replace(match, str(result), 1)
        matches = re.findall('[0-9]+ \+ [0-9]+', line)
    return sumUp(line)

def sumUp(line):
    result = 0
    operation = add
    for symbol in line.split(' '):
        if symbol.isnumeric():
            symbol = int(symbol)
            result = operation(result, symbol)
        elif symbol == '+':
            operation = add
        elif symbol == '*':
            operation = multiply
    return result

def multiply(result, symbol):
    return result * symbol

def add(result, symbol):
    return result + symbol

def do():
    with open ('Input/day18.txt') as f:
        strInput = f.read()

    splitInput = inputsplit(strInput, '\n')

    print(do1(splitInput))
    print(do2(splitInput))
    
do()