rawInput = """R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83"""


def do1(splitInput):
    first,second = splitInput

    locations = {}
    
    processWires(first, locations, 1)
    processWires(second, locations, 2)

    sameLocations = [x for x in locations[1] if x in locations[2]]
    distancesSameLocations = [abs(x[0]) + abs(x[1]) for x in sameLocations]

    return min(distancesSameLocations)

def processWires(wire, locations, value):
    locations[value] = []
    currentPosition = (0,0)
    for movement in wire.split(','):
        direction = movement[0]
        distance = int(movement[1:])

        if direction == 'R':
            deltaMovement = (1,0)
        elif direction == 'U':
            deltaMovement = (0,1)
        elif direction == 'L':
            deltaMovement = (-1,0)
        elif direction == 'D':
            deltaMovement = (0,-1)
        
        for _ in range(distance):
            currentPosition = (currentPosition[0] + deltaMovement[0], currentPosition[1] + deltaMovement[1])
            locations[value].append(currentPosition)

def do():

    splitInput = rawInput.split()

    print(do1(splitInput))

do()


