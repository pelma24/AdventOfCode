from HelperFunctions import inputsplit
from HelperFunctions import convertToInt
from copy import deepcopy
import re

def do1(puzzleInput):
    valid = puzzleInput[0].split('\n')

    nearbyTickets = puzzleInput[2].split('\n')[1:]

    validFields = extractValidFields(valid)

    invalidValues = checkNearbyTickets(nearbyTickets, validFields)

    return sum(invalidValues)

def do2(puzzleInput):
    valid = puzzleInput[0].split('\n')

    myTicket = puzzleInput[1].split('\n')[1]

    nearbyTickets = puzzleInput[2].split('\n')[1:]

    validFields = extractValidFields(valid)

    validTickets = getValidTickets(nearbyTickets, validFields)
    
    assignedFields = getActualFields(validTickets, validFields)

    result = multiplyDepartureValues(assignedFields, myTicket)

    return result

def extractValidFields(valid):
    validFields = {}
    for line in valid:
        match = re.match('([a-z ]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)', line)
        name, x1, x2, y1, y2 = [int(x) if x.isnumeric() else x for x in match.groups()]

        validFields[name] = []
        for i in range(x1, x2 + 1):
            validFields[name].append(i)
        for i in range(y1, y2 + 1):
            validFields[name].append(i)

    return validFields

def checkNearbyTickets(tickets, validFields):
    invalidValues = []
    for ticket in tickets:
        strfields = ticket.split(',')
        fields = convertToInt(strfields)
        for field in fields:
            valid = False
            for value in validFields.values():
                if field in value:
                    valid = True
            if not valid:
                invalidValues.append(field)

    return invalidValues

def getValidTickets(tickets, validFields):
    validIntTickets = []
    for ticket in tickets:
        ticketValid = True
        strfields = ticket.split(',')
        fields = convertToInt(strfields)
        for field in fields:
            valid = False
            for value in validFields.values():
                if field in value:
                    valid = True
            if not valid:
                ticketValid = False
                break
        if ticketValid:
            validIntTickets.append(fields)
    
    return validIntTickets

def getActualFields(validTickets, validFields):
    possibleFields = {}
    for position in range(0, len(validTickets[0])):
        possibleFields[position] = []
        for key,value in validFields.items():
            possibleFields[position].append(key)
            
    for ticket in validTickets:
        for position,field in enumerate(ticket):
            for key in possibleFields[position]:
                if not (field in validFields[key]):
                    possibleFields[position].remove(key)

    solution = {}    
    while (len(solution.keys()) != len(validFields.keys())):
        for key,value in possibleFields.items():
            if len(value) == 1:
                solution[key] = value[0]
                for otherValues in possibleFields.values():
                    if solution[key] in otherValues:
                        otherValues.remove(solution[key])

    return solution

def multiplyDepartureValues(assignedFields, myTicket):
    myTicket = [int(x) for x in myTicket.split(',')]

    result = 1
    for key,value in assignedFields.items():
        if re.match('departure', value):
            result *= myTicket[key]
    
    return result

def do():
    with open ('Input/day16.txt') as f:
        strInput = f.read()

    splitInput = inputsplit(strInput, '\n\n')

    print(do1(splitInput))
    print(do2(splitInput))
    
do()