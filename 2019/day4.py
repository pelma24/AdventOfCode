rangeLow = 134792
rangeHigh = 675810

def do1():

    result = []

    for i in range(rangeLow, rangeHigh + 1):
        if hasDouble(i) and doesNotDecrease(i):
            result.append(i) 

    return result

def do2():

    result = []

    for i in range(rangeLow, rangeHigh + 1):
        if hasOnlyOneDouble(i) and doesNotDecrease(i):
            result.append(i) 

    return result

def hasOnlyOneDouble(i):
    numbers = [int(x) for x in str(i)]

    dic = {}

    for number in numbers:
        dic[number] = dic.get(number, 0) + 1

    if 2 in dic.values():
        return True
    
    return False

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
print(len(do1()))

#part2
print(len(do2()))