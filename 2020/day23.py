from collections import deque

def do1(puzzleInput):
    queue = deque([int(x) for x in puzzleInput])

    play(queue, 100)

    return cupOrder(queue)

def do2(puzzleInput):
    queue = [int(x) for x in puzzleInput] + list(range(10, 1000000+1))
    
    linkedList = play2(queue, 10000000)

    return findStars(linkedList)

def cupOrder(queue):
    result = ''

    first = queue.index(1)
    queue.rotate(-(first + 1))

    for _ in range(len(queue) - 1):
        result += str(queue.popleft())

    return result

def findStars(linkedList):
    first = linkedList[1]
    second = linkedList[first]

    return first * second

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
    
    linkedList = {}

    for index,item in enumerate(queue[0:-1]):
        linkedList[item] = queue[index + 1]
    linkedList[queue[-1]] = queue[0]

    currentIndex = queue[-1]

    for _ in range(1, turns + 1):
        currentElement = linkedList[currentIndex]
        removed = [linkedList[currentElement], linkedList[linkedList[currentElement]], linkedList[linkedList[linkedList[currentElement]]]]
        nextafternextafternext = removed[-1]
        newElement = currentElement - 1

        if newElement < minValue:
            newElement = maxValue
        while newElement in removed:
            newElement -= 1
            if newElement < minValue:
                newElement = maxValue

        tmp1 = linkedList[newElement]
        tmp2 = linkedList[nextafternextafternext]
        linkedList[newElement] = linkedList[currentElement]
        linkedList[nextafternextafternext] = tmp1
        linkedList[currentElement] = tmp2

        currentIndex = currentElement
        
    return linkedList

def do():
    with open ('Input/day23.txt') as f:
        strInput = f.read()

    print(do1(strInput))
    print(do2(strInput))
    
do()