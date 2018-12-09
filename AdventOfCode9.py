input = "477 players; last marble is worth 70851 points"

players = 477
marble = 7085100

def do():

    result = {}
    l = [0, 1]
    position = 1
    player = 2
    for turn in range(2, marble):
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

        player += 1
        if player > 477:
            player = 1

    return result

result = do()
print(max(result.values()))