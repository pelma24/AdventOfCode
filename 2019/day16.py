input = """59767332893712499303507927392492799842280949032647447943708128134759829623432979665638627748828769901459920331809324277257783559980682773005090812015194705678044494427656694450683470894204458322512685463108677297931475224644120088044241514984501801055776621459006306355191173838028818541852472766531691447716699929369254367590657434009446852446382913299030985023252085192396763168288943696868044543275244584834495762182333696287306000879305760028716584659188511036134905935090284404044065551054821920696749822628998776535580685208350672371545812292776910208462128008216282210434666822690603370151291219895209312686939242854295497457769408869210686246"""


def inputSplit(input):
    intInput = []
    for x in input:
        intInput.append(int(x))
    return intInput

def do():
    
    splitInput = inputSplit(input)
    result = splitInput.copy()
    
    for i in range(100):
        for outputPos in range(len(splitInput)):
            pattern = createPattern(outputPos)
            result[outputPos] = applyPattern(pattern, splitInput)
        splitInput = result.copy()
    
    return result

def applyPattern(pattern, splitInput):
    patternPos = 1
    sum = 0
    for pos in range(len(splitInput)):
        sum += splitInput[pos] * pattern[patternPos]
        patternPos = (patternPos + 1) % len(pattern)    
    return abs(sum) % 10

def createPattern(pos):
    pattern = [0, 1, 0, -1]
    resultPattern = []

    for position in range(len(pattern)):
        for repetition in range(pos + 1):
            resultPattern.append(pattern[position])
    
    return resultPattern



print(do()[:8])