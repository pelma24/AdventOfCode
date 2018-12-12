
def calculateGreatestPower(dic, kernel):
    indexX = -1
    indexY = -1
    powerSums = [[0 for x in range(len(dic) - kernel)] for y in range(len(dic[0]) - kernel)]
    maxPowerSum = -10000
    for y in range(len(dic) - kernel):
        for x in range(len(dic[0]) - kernel):

            powerSum = 0
            for i in range(kernel):
                for j in range(kernel):
                    powerSum += dic[y + i][x + j]

            powerSums[y][x] = powerSum
            if powerSum > maxPowerSum:
                maxPowerSum = powerSum
                indexX = x
                indexY = y
    
    return [indexX + 1,indexY + 1, maxPowerSum]

def do():
    serial = 5034

    width = 300
    height = 300

    kernelwidth = 3

    powermatrix = [[0 for x in range(width)] for y in range(height)]

    for y in range(1, height + 1):
        for x in range(1, width + 1):
            rackID = x + 10
            powerlevel = (rackID * y + serial) * rackID
            
            powermatrix[y-1][x-1] = int((powerlevel % 1000) / 100) - 5

    maxPower = -10000
    size = 0
    topleft = []
    for i in range(1,301):
        topleftX, topleftY, powerSum = calculateGreatestPower(powermatrix, i)
        if powerSum > maxPower:
            maxPower = powerSum
            size = i
            topleft = [topleftX, topleftY]

    return [topleft, size]



print(do())