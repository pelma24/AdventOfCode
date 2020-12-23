from collections import deque

def do1(puzzleInput):
    queue = deque([int(x) for x in puzzleInput])

    play(queue, 100)

    return cupOrder(queue)

def do2(puzzleInput):
    queue = deque([int(x) for x in puzzleInput])
    length = len(queue)

    for i in range(length + 1, 1000001):
        queue.append(i)

    play(queue, 10000000)

    return findStars(queue)

def cupOrder(queue):
    result = ''

    first = queue.index(1)
    queue.rotate(-(first + 1))

    for _ in range(len(queue) - 1):
        result += str(queue.popleft())

    return result

def findStars(queue):
    first = queue.index(1)
    queue.rotate(-(first + 1))

    a = queue.popleft()
    b = queue.popleft()

    return a * b

def play(queue, turns):
    maxValue = max(queue)
    minValue = min(queue)

    for repetition in range(turns):

        queue.rotate(-1)
        removed = []
        for _ in range(3):            
            removed.append(queue.popleft())
        queue.rotate(1)

        newElement = queue[0] - 1

        if newElement < minValue:
            newElement = maxValue

        while newElement in removed:
            newElement -= 1
            if newElement < minValue:
                newElement = maxValue
        
        newIndex = queue.index(newElement)

        for value in removed:
            newIndex += 1
            queue.insert(newIndex, value)
        
        queue.rotate(-1)

def do():
    with open ('Input/day23.txt') as f:
        strInput = f.read()

    print(do1(strInput))
    print(do2(strInput))
    
do()