def inputsplit(input, separator=' '):
    return input.split(separator)

def convertToInt(input):
    numbers = []
    for stringNumber in input:
        numbers.append(int(stringNumber))

    return numbers