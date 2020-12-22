from HelperFunctions import inputsplit
from HelperFunctions import convertToInt

def do1(puzzleInput):
    player1 = convertToInt(puzzleInput[0].split('\n')[1:])
    player2 = convertToInt(puzzleInput[1].split('\n')[1:])

    winner = play(player1, player2)

    winningScore = getWinningScore(winner)

    return winningScore

def do2(puzzleInput):
    player1 = convertToInt(puzzleInput[0].split('\n')[1:])
    player2 = convertToInt(puzzleInput[1].split('\n')[1:])

    memory = []
    winner = playRecursive(player1, player2, memory)

    if winner == 1:
        return getWinningScore(player1)
    else:
        return getWinningScore(player2)

def play(player1, player2):
    while True:
        card1 = player1.pop(0)
        card2 = player2.pop(0)

        if card1 < card2:
            player2.append(card2)
            player2.append(card1)
        else:
            player1.append(card1)
            player1.append(card2)
        
        if len(player1) == 0:
            return player2
        if len(player2) == 0:
            return player1

def playRecursive(player1, player2, memory):
    while True:
        if (player1, player2) in memory:
            return 1
        else:
            memory.append((player1.copy(), player2.copy()))

        card1 = player1.pop(0)
        card2 = player2.pop(0)

        if len(player1) >= card1 and len(player2) >= card2:
            winner = playRecursive(player1[0:card1].copy(), player2[0:card2].copy(), [])   
        else:
            if card1 < card2:
                winner = 2
            else:
                winner = 1
        
        if winner == 1:
            player1.append(card1)
            player1.append(card2)
        else:
            player2.append(card2)
            player2.append(card1)     

        if len(player1) == 0:
            return 2
        if len(player2) == 0:
            return 1   

def getWinningScore(player):
    value = range(len(player), 0, -1)
    score = sum([a*b for a,b in zip(player, value)])
    
    return score

def do():
    with open ('Input/day22.txt') as f:
        strInput = f.read()

    splitInput = inputsplit(strInput, '\n\n')
    
    print(do1(splitInput))
    print(do2(splitInput))
    
do()