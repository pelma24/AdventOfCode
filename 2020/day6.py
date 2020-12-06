from HelperFunctions import inputsplit

def do1(puzzleInput):

    groupCount = 0

    for group in puzzleInput:
        answers = []
        persons = group.split('\n')
        for person in persons:
            for answer in person:
                answers.append(answer)
        groupCount += len(set(answers))

    return groupCount

def do2(puzzleInput):
    
    groupCount = 0

    for group in puzzleInput:
        persons = group.split('\n')
        sameAnswers = getAnswers(persons[0])
        for otherPerson in persons[1:]:
            answer = getAnswers(otherPerson)
            sameAnswers = sameAnswers.intersection(answer)        

        groupCount += len(sameAnswers)

    return groupCount

def getAnswers(person):
    answers = []
    for answer in person:
        answers.append(answer)
    
    return set(answers)

def do():
    with open ('Input/day6.txt') as f:
        strInput = f.read()

    splitInput = inputsplit(strInput, '\n\n')

    print(do1(splitInput))
    print(do2(splitInput))
    
do()