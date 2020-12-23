from collections import deque

def do1(puzzleInput):
    queue = deque([int(x) for x in puzzleInput])

    play(queue, 100)

    return cupOrder(queue)

def do2(puzzleInput):
    queue = deque([int(x) for x in puzzleInput] + list(range(10, 1000000+1)))
    
    play2(queue, 10000000)

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

    for _ in range(1, turns + 1):
        currentElement = queue.popleft()
        removed = [queue.popleft(), queue.popleft(), queue.popleft()]

        newElement = currentElement - 1

        if newElement < minValue:
            newElement = maxValue

        while newElement in removed:
            newElement -= 1
            if newElement < minValue:
                newElement = maxValue
        newIndex = queue.index(newElement)

        queue.rotate(- (newIndex + 1))
        queue.extendleft(removed[::-1])
        queue.rotate(newIndex + 1)

        queue.append(currentElement)

def play2(queue, turns):
    maxValue = max(queue)
    minValue = min(queue)

    comesAfter = {}

    for _ in range(1, turns + 1):
        currentElement = getNextElement(queue, comesAfter)
        removed = [getNextElement(queue, comesAfter), getNextElement(queue, comesAfter), getNextElement(queue, comesAfter)]

        newElement = currentElement - 1

        if newElement < minValue:
            newElement = maxValue

        while newElement in removed:
            newElement -= 1
            if newElement < minValue:
                newElement = maxValue
        
        comesAfter[newElement] = removed

        queue.append(currentElement)

def getNextElement(queue, comesAfter):
    nextElement = queue.popleft()

    if nextElement in comesAfter.keys():
        queue.extendleft(comesAfter[nextElement][::-1])
        del comesAfter[nextElement]

    return nextElement

def do():
    with open ('Input/day23.txt') as f:
        strInput = f.read()

    print(do1(strInput))
    print(do2(strInput))
    
do()