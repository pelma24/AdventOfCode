from HelperFunctions import inputsplit

def do1(earliest, puzzleInput):
    bestBusID = 0
    leastWaitingTime = 100000000000

    for bus in puzzleInput:
        if bus == 'x':
            continue
        busDepartTime = 0
        busID = int(bus)
        while busDepartTime < earliest:
            busDepartTime += busID
        if (busDepartTime - earliest) < leastWaitingTime:
            leastWaitingTime = busDepartTime - earliest
            bestBusID = busID
    
    return bestBusID * leastWaitingTime

def do2(puzzleInput):

    maxBus = max([x for x in puzzleInput if x != 'x'])
    maxBusIndex = puzzleInput.index(maxBus)
    maxBus = int(maxBus)

    departTime = 100000000000481-maxBusIndex
    works = False
    while not works:
        works = True
        departTime += maxBus
        for i in range(len(puzzleInput)):
            bus = puzzleInput[i]
            if bus == 'x':
                continue
            busID = int(bus)
            if (departTime + i) % busID != 0:
                works = False
                break
    
    return departTime

def do():
    with open ('Input/day13.txt') as f:
        strInput = f.read()

    splitInput = inputsplit(strInput, ',')

    earliest = 1007125

    #print(do1(earliest, splitInput))
    print(do2(splitInput))
    
do()
