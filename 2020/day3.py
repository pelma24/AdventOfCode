from HelperFunctions import inputsplit

def do1(puzzleInput):
    
    return countTrees(puzzleInput, 1, 3)

def do2(puzzleInput, slopes):
    
    trees = 1

    for slope in slopes:
        trees *= countTrees(puzzleInput, slope[0], slope[1])

    return trees

def countTrees(puzzleInput, slopeRow, slopeColumn):
    trees = 0

    rowEnd = len(puzzleInput) - 1
    columnLength = len(puzzleInput[0])

    row = 0
    column = 0

    while(row < rowEnd):
        row += slopeRow
        column = (column + slopeColumn) % columnLength
        if puzzleInput[row][column] == '#':
            trees += 1

    return trees


def do():
    with open ('Input/day3.txt') as f:
        strInput = f.read()

    splitInput = inputsplit(strInput, '\n')

    slopes = [(1,1), (1,3), (1,5), (1,7), (2,1)]

    print(do1(splitInput))
    print(do2(splitInput, slopes))
    
do()