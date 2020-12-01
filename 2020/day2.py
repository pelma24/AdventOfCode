def do1(puzzleInput):
    return 'done'

def do2(puzzleInput):
    return 'done'

def do():
    with open ('Input/day2.txt') as f:
        strInput = f.read()

    print(do1(strInput))
    print(do2(strInput))
    
do()