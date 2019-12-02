input = "477 players; last marble is worth 70851 points"

def do(players, marble):

    result = {}
    l = [0, 1]
    position = 1
    player = 2
    for turn in range(2, marble + 1):
        if (turn % 23) == 0:
            if player not in result:
                result[player] = 0
            removePosition = (position - 7 + len(l)) % len(l)
            score = turn + l[removePosition]
            l.remove(l[removePosition])
            result[player] += score

            position = removePosition % len(l)
        else:
            index = (position + 2) % len(l)
            l.insert(index, turn)
            position = index

        player = (player + 1) % players

    return max(result.values())

result = do(477, 70851)
print(result)