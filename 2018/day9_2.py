from collections import deque

def do(players, marbles):

    player = 1
    
    marble_list = deque([0])
    scores = {}

    for marble in range(1, marbles + 1):
        if (marble % 23 == 0):
            points = marble

            marble_list.rotate(7)
            points += marble_list.popleft()

            if player not in scores:
                scores[player] = 0
            
            scores[player] += points

        else:
            marble_list.rotate(-2)
            marble_list.insert(0, marble)
        
        player = (player + 1) % players
    
    return max(scores.values())
    

print(do(477, 7085100))