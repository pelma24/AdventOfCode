from HelperFunctions import inputsplit

def do1(puzzleInput):

    groupCount = 0

    for group in puzzleInput:
        answers = set()
        persons = group.split('\n')
        for person in persons:
            answer = set(person)
            answers = answers.union(answer)
        groupCount += len(answers)

    return groupCount

def do2(puzzleInput):
    
    groupCount = 0

    for group in puzzleInput:
        persons = group.split('\n')
        sameAnswers = set(persons[0])
        for otherPerson in persons[1:]:
            answer = set(otherPerson)
            sameAnswers = sameAnswers.intersection(answer)        

        groupCount += len(sameAnswers)

    return groupCount

def do():
    with open ('Input/day6.txt') as f:
        strInput = f.read()

    splitInput = inputsplit(strInput, '\n\n')

    print(do1(splitInput))
    print(do2(splitInput))
    
do()