from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt

def do1(splitInput):
	
    list1 = []
    list2 = []
    for entry in splitInput:
        entry1,entry2 = entry.split('   ')
        list1.append(entry1)
        list2.append(entry2)
	
    list1.sort()
    list1 = convertToInt(list1)
    list2.sort()
    list2 = convertToInt(list2)
	
    result = 0

    for i in range(len(list1)):
        result = result + abs(list1[i] - list2[i])

    return result


def do2(splitInput):
	
    list1 = []
    list2 = []
    for entry in splitInput:
        entry1,entry2 = entry.split('   ')
        list1.append(entry1)
        list2.append(entry2)
    
    list1 = convertToInt(list1)
    list2 = convertToInt(list2)

    result = 0
    for entry in list1:
         result = result + entry * list2.count(entry)
    
    return result
def do():
	strInput = readInputFile(1)

	splitInput = strInput.split('\n')
	
	print(do1(splitInput))
	print(do2(splitInput))

	print('done')


do()