from HelperFunctions import inputsplit
import re

def do1(puzzleInput):
        
    passportKeys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    passportData = extractPassportData(puzzleInput)

    numberOfValidPassports = 0
    for passport in passportData:
        if all (x in passport.keys() for x in passportKeys):
            numberOfValidPassports += 1

    return numberOfValidPassports

def do2(puzzleInput):
    
    passportData = extractPassportData(puzzleInput)

    passportKeys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    numberOfValidPassports = 0

    for passport in passportData:
        if all (x in passport.keys() for x in passportKeys):
            if (checkBirthYear(passport) and checkIssueYear(passport) and checkExpirationYear(passport) and checkHeight(passport) and checkHairColor(passport) and checkPassportID(passport) and checkEyeColor(passport)):
                numberOfValidPassports += 1

    return numberOfValidPassports

def checkBirthYear(passport):
    if passport['byr'].isnumeric and 1920 <= int(passport['byr']) <= 2002:
        return True  

    return False

def checkIssueYear(passport):
    if passport['iyr'].isnumeric and 2010 <= int(passport['iyr']) <= 2020:
        return True  

    return False

def checkExpirationYear(passport):
    if passport['eyr'].isnumeric and 2020 <= int(passport['eyr']) <= 2030:
        return True  

    return False

def checkHeight(passport):
    match = re.fullmatch('([0-9]+)(\D+)', passport['hgt'])
    if match and match.groups()[1] == 'cm' and 150 <= int(match.groups()[0]) <= 193:
        return True
    if match and match.groups()[1] == 'in' and 59 <= int(match.groups()[0]) <= 76:
        return True
    
    return False

def checkHairColor(passport):
    match = re.fullmatch('\#[0-9|a-f]{6}', passport['hcl'])
    if match:
        return True

    return False

def checkPassportID(passport):
    match = re.fullmatch('[0-9]{9}', passport['pid'])

    if match:
        return True
    
    return False

def checkEyeColor(passport):

    validEyeColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    if passport['ecl'] in validEyeColors:
        return True
    return False

def extractPassportData(puzzleInput):

    resultList = []

    for passportData in puzzleInput:
        passport = {}
        match = re.findall('([a-z]+):([\#a-zA-Z0-9]+)[\s]?', passportData)

        for entries in match:
            passport[entries[0]] = entries[1]

        resultList.append(passport)

    return resultList

def do():
    with open ('Input/day4.txt') as f:
        strInput = f.read()

    splitInput = inputsplit(strInput, '\n\n')

    print(do1(splitInput))
    print(do2(splitInput))
    
do()