import math

input =""".###.#...#.#.##.#.####..
.#....#####...#.######..
#.#.###.###.#.....#.####
##.###..##..####.#.####.
###########.#######.##.#
##########.#########.##.
.#.##.########.##...###.
###.#.##.#####.#.###.###
##.#####.##..###.#.##.#.
.#.#.#####.####.#..#####
.###.#####.#..#..##.#.##
########.##.#...########
.####..##..#.###.###.#.#
....######.##.#.######.#
###.####.######.#....###
############.#.#.##.####
##...##..####.####.#..##
.###.#########.###..#.##
#.##.#.#...##...#####..#
##.#..###############.##
##.###.#####.##.######..
##.#####.#.#.##..#######
...#######.######...####
#....#.#.#.####.#.#.#.##
"""


def do():
    grid = input.split()
    asteroids = getAsteroids(grid)
    counts = {}
    detectedAsteroids = {}

    for x,y in asteroids:
        count, seenAsteroids = detectAsteroids(asteroids, (x,y))
        counts[(x,y)] = count
        detectedAsteroids[(x,y)] = seenAsteroids
    return counts, detectedAsteroids

def do2(center, asteroids):
    angles = {}
    upperPoint = (center[0], 0)

    for asteroid in asteroids:
        angle = getAngle(upperPoint, center, asteroid)
        angles[asteroid] = angle
    
    return angles

def getAsteroids(grid):
    asteroids = []
    for y in range(len(grid)):
        line = grid[y]
        for x in range(len(line)):
            point = line[x]
            if point != '#':
                continue
            asteroids.append((x,y))
    return asteroids

def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang

def detectAsteroids(asteroids, center):
    count = 0
    seenAsteroids = []
    for x,y in asteroids:
            if (x,y) == center:
                continue
            if canBeSeen(center, asteroids, (x,y)):
                count += 1
                seenAsteroids.append((x,y))
    return count, seenAsteroids

def canBeSeen(center, asteroids, endPoint):
    canBeSeen = True
    for x,y in asteroids:
        if (x,y) == center or (x,y) == endPoint:
            continue
        if isBetween(center, endPoint, (x,y)):
            canBeSeen = False
            break
    return canBeSeen

def isBetween(center, endPoint, point):
    crossProduct = (point[1] - center[1]) * (endPoint[0] - center[0]) - (point[0] - center[0]) * (endPoint[1] - center[1])
    if crossProduct != 0:
        return False
    dotProduct = (point[0] - center[0]) * (endPoint[0] - center[0]) + (point[1] - center[1])*(endPoint[1] - center[1])
    if dotProduct < 0:
        return False
    squaredLength = (endPoint[0] - center[0])*(endPoint[0] - center[0]) + (endPoint[1] - center[1])*(endPoint[1] - center[1])
    if dotProduct > squaredLength:
        return False
    return True

#part1
counts, asteroids = do()

maxKey = max(counts, key=counts.get)
maxValue = counts[maxKey]

print(maxValue)

#part2
angles = do2(maxKey, asteroids[maxKey])
sortedAngles = list((sorted(angles.items(), key=lambda item: item[1])))
print (sortedAngles[199][0][0] * 100 + sortedAngles[199][0][1])





