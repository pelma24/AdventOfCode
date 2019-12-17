import re

input = """<x=14, y=2, z=8>
<x=7, y=4, z=10>
<x=1, y=17, z=16>
<x=-4, y=-1, z=1>"""


def do():
    splitInput = input.split('\n')

    moons = getMoons(splitInput)

    simulate(moons, 1000)

    energy = calculateEnergy(moons)

    return energy

def do2():
    splitInput = input.split('\n')

    moons = getMoons(splitInput)

    steps = simulateEndless(moons)

    return steps

def getMoons(splitInput):
    moons = {}
    for i in range(len(splitInput)):
        moons[i] = {}
        moon = splitInput[i]
        match = re.match('<x=([-]?[0-9]+), y=([-]?[0-9]+), z=([-]?[0-9]+)>', moon)

        positionX, positionY, positionZ = [int(x) for x in match.groups()]

        moons[i]['posX'] = positionX
        moons[i]['posY'] = positionY
        moons[i]['posZ'] = positionZ
        moons[i]['velX'] = 0
        moons[i]['velY'] = 0
        moons[i]['velZ'] = 0

    return moons

def simulate(moons, time):
    for i in range(time):
        for observedMoon in moons.keys():
            for otherMoon in moons.keys():
                #x
                if moons[observedMoon]['posX'] < moons[otherMoon]['posX']:
                    moons[observedMoon]['velX'] += 1
                elif moons[observedMoon]['posX'] > moons[otherMoon]['posX']:
                    moons[observedMoon]['velX'] -= 1
                #y
                if moons[observedMoon]['posY'] < moons[otherMoon]['posY']:
                    moons[observedMoon]['velY'] += 1
                elif moons[observedMoon]['posY'] > moons[otherMoon]['posY']:
                    moons[observedMoon]['velY'] -= 1
                #z
                if moons[observedMoon]['posZ'] < moons[otherMoon]['posZ']:
                    moons[observedMoon]['velZ'] += 1
                elif moons[observedMoon]['posZ'] > moons[otherMoon]['posZ']:
                    moons[observedMoon]['velZ'] -= 1
        moveMoons(moons)
    return moons

def simulateEndless(moons):
    steps = 0
    while True:
        for observedMoon in moons.keys():
            for otherMoon in moons.keys():
                #x
                if moons[observedMoon]['posX'] < moons[otherMoon]['posX']:
                    moons[observedMoon]['velX'] += 1
                elif moons[observedMoon]['posX'] > moons[otherMoon]['posX']:
                    moons[observedMoon]['velX'] -= 1
                #y
                if moons[observedMoon]['posY'] < moons[otherMoon]['posY']:
                    moons[observedMoon]['velY'] += 1
                elif moons[observedMoon]['posY'] > moons[otherMoon]['posY']:
                    moons[observedMoon]['velY'] -= 1
                #z
                if moons[observedMoon]['posZ'] < moons[otherMoon]['posZ']:
                    moons[observedMoon]['velZ'] += 1
                elif moons[observedMoon]['posZ'] > moons[otherMoon]['posZ']:
                    moons[observedMoon]['velZ'] -= 1
        moveMoons(moons)
        steps += 1
        if moons[0]['posX'] == 14 and moons[1]['posX'] == 7 and moons[2]['posX'] == 1 and moons[3]['posX'] == -4 and moons[0]['posY'] == 2 and moons[1]['posY'] == 4 and moons[2]['posY'] == 17 and moons[3]['posY'] == -1:
            print(steps)
            break
    return steps

def moveMoons(moons):
    for moon in moons.keys():
        moons[moon]['posX'] += moons[moon]['velX']
        moons[moon]['posY'] += moons[moon]['velY']
        moons[moon]['posZ'] += moons[moon]['velZ']

def calculateEnergy(moons):
    totalEnergy = 0
    for moon in moons.keys():
        potentialEnergy = 0
        kineticEnergy = 0
        potentialEnergy += abs(moons[moon]['posX'])
        potentialEnergy += abs(moons[moon]['posY'])
        potentialEnergy += abs(moons[moon]['posZ'])

        kineticEnergy += abs(moons[moon]['velX'])
        kineticEnergy += abs(moons[moon]['velY'])
        kineticEnergy += abs(moons[moon]['velZ'])

        moons[moon]['energy'] = potentialEnergy * kineticEnergy
        totalEnergy += potentialEnergy * kineticEnergy
    return totalEnergy

#part1
#print(do())

#part2
print(do2())