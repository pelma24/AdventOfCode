from HelperFunctions import inputsplit

def do1(puzzleInput):
    
    return countTrees(puzzleInput, 1, 3)

def do2(puzzleInput):
    
    trees1 = countTrees(puzzleInput, 1, 1)
    trees2 = countTrees(puzzleInput, 1, 3)
    trees3 = countTrees(puzzleInput, 1, 5)
    trees4 = countTrees(puzzleInput, 1, 7)
    trees5 = countTrees(puzzleInput, 2, 1)

    return trees1 * trees2 * trees3 * trees4 * trees5

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

    print(do1(splitInput))
    print(do2(splitInput))
    
do()