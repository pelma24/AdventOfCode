from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt

def isSafe(report):
	
	diff = [report[x+1]-report[x] for x in range(len(report)-1)]

	if all([x in [-1,-2,-3] for x in diff]) or all([x in [1,2,3] for x in diff]):
		return True
	
	return False


def do1(splitInput):
	
	result = 0
	for report in splitInput:
		report = convertToInt(report.split(' '))
		
		if isSafe(report):
			result = result + 1
		
		else:
			for i in range(len(report)):
				adaptedReport = report.copy()
				adaptedReport.pop(i)
				if isSafe(adaptedReport):
					result = result + 1
					break
	
	return result

def do2(splitInput):
	return 'done'

def do():
	strInput = readInputFile(2)

	splitInput = strInput.split('\n')

	print(do1(splitInput))
	print(do2(splitInput))

	print('done')


do()