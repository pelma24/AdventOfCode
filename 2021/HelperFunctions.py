
def readInputFile(day):
    with open (f'Input/day{day}.txt') as f:
        strInput = f.read()
    return strInput

def convertToInt(input):
    numbers = []
    for stringNumber in input:
        numbers.append(int(stringNumber))

    return numbers