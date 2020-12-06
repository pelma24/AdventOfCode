from HelperFunctions import inputsplit

def do1(puzzleInput):

    return getGroupCount(puzzleInput, union)

def do2(puzzleInput):
    
    return getGroupCount(puzzleInput, intersection)

def getGroupCount(puzzleInput, mergeFunction):
    groupCount = 0

    for group in puzzleInput:
        persons = group.split('\n')
        sameAnswers = set(persons[0])
        for otherPerson in persons[1:]:
            answer = set(otherPerson)
            sameAnswers = mergeFunction(sameAnswers, answer)        

        groupCount += len(sameAnswers)

    return groupCount    

def intersection(set1, set2):
    return set1.intersection(set2)

def union(set1, set2):
    return set1.union(set2)

def do():
    with open ('Input/day6.txt') as f:
        strInput = f.read()

    splitInput = inputsplit(strInput, '\n\n')

    print(do1(splitInput))
    print(do2(splitInput))
    
do()