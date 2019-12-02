input = 894501

def doOne():
    l = [3,7]

    elf1 = 0
    elf2 = 1

    while True:
        newRecipe = l[elf1] + l[elf2]

        numbers = [int(x) for x in str(newRecipe)]
        for number in numbers:
            l.append(number)

        elf1 = (elf1 + 1 + l[elf1]) % len(l)
        elf2 = (elf2 + 1 + l[elf2]) % len(l)

        if len(l) >= input + 10:
            return(l[input:])

def doTwo():
    l = [3,7]

    elf1 = 0
    elf2 = 1

    inputstr = [int(x) for x in str(input)]

    resultIndex = 2
    index = 0

    while True:
        
        newRecipe = l[elf1] + l[elf2]

        numbers = [int(x) for x in str(newRecipe)]
        for number in numbers:
            if number == inputstr[index]:
                resultIndex = len(l) - index
                index += 1
                if index == len(inputstr):
                    return resultIndex
            else:
                index = 0
                if number == inputstr[index]:
                    resultIndex = len(l) - index
                    index += 1
                    if index == len(inputstr):
                        return resultIndex
            l.append(number)

        elf1 = (elf1 + 1 + l[elf1]) % len(l)
        elf2 = (elf2 + 1 + l[elf2]) % len(l)        

   
print(doOne())
print(doTwo())