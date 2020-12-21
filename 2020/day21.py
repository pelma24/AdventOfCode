from HelperFunctions import inputsplit
import re
from copy import deepcopy

def do1(puzzleInput):
    completeListOfIngredients, possibleAllergens = getIngredients(puzzleInput)

    badIngredients = extractBadIngredients(possibleAllergens)

    goodIngredients = countGoodIngredients(completeListOfIngredients, badIngredients)

    return goodIngredients

def do2(puzzleInput):
    _, possibleAllergens = getIngredients(puzzleInput)

    badIngredients = extractBadIngredients(possibleAllergens)

    canonical = getCanonicalDangerousList(badIngredients)

    return canonical

def getCanonicalDangerousList(badIngredients):
    sortedAllergens = sorted(list(badIngredients.keys()))

    result = ''
    for allergen in sortedAllergens:
        result += badIngredients[allergen]
        if allergen != sortedAllergens[-1]:
            result += ','
    
    return result

def getIngredients(puzzleInput):
    allergensInIngredients = {}
    completeListOfIngredients = []
    for line in puzzleInput:
        match = re.match('(.+) \(contains (.+)\)', line)
        if match:
            allIngredients = match.groups()[0].split(' ')
            completeListOfIngredients += allIngredients
            ingredients = set(allIngredients)
            allergens = match.groups()[1].replace(' ', '').split(',')
            
            for allergen in allergens:
                if allergen not in allergensInIngredients.keys():
                    allergensInIngredients[allergen] = ingredients
                else:
                    allergensInIngredients[allergen] = allergensInIngredients[allergen] & ingredients

    return completeListOfIngredients, allergensInIngredients

def countGoodIngredients(ingredients, badIngredients):
    for value in badIngredients.values():
        ingredients = [x for x in ingredients if x != value]

    return len(ingredients)

def extractBadIngredients(allergens):
    solution = {}
    while (len(solution.keys()) != len(allergens.keys())):
        for allergen,ingredients in allergens.items():
            if len(ingredients) == 1:
                solution[allergen] = ingredients.pop()
                for value in allergens.values():
                    value.discard(solution[allergen])
    return solution

def do():
    with open ('Input/day21.txt') as f:
        strInput = f.read()

    splitInput = inputsplit(strInput, '\n')
    
    print(do1(splitInput))
    print(do2(splitInput))
    
do()