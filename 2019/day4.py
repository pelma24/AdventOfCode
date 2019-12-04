rangeLow = 134792
rangeHigh = 675810

def do():

    result = []

    for i in range(rangeLow, rangeHigh + 1):
        if hasDouble(i) and doesNotDecrease(i):
            result.append(i) 

    return result

def hasDouble(i):
    numbers = [int(x) for x in str(i)]
    
    for j in range(len(numbers) - 1):
        if numbers[j] == numbers[j + 1]:
            return True

    return False

def doesNotDecrease(i):
    numbers = [int(x) for x in str(i)]

    for j in range(len(numbers) - 1):
        if numbers[j+1] < numbers[j]:
            return False
    return True

#part1
print(len(do()))

#part2