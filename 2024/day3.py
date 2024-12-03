from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt
import re


def do1(strInput):
	
	findings = re.findall('mul\((\d+),(\d+)\)', strInput)
	
	result = 0

	for finding in findings:
		result = result + int(finding[0]) * int(finding[1])
	
	return result

def do2(strInput):
	matches = {}

	for match in re.finditer('do\(\)', strInput):
		matches[match.start()] = 'do'

	for match in re.finditer('don\'t\(\)', strInput):
		matches[match.start()] = 'dont'

	for match in re.finditer('mul\((\d+),(\d+)\)', strInput):
		matches[match.start()] = match.groups()

	active = True
	result = 0

	for key in sorted(matches.keys()):
		match matches[key]:
			case 'do':
				active = True
			case 'dont':
				active = False
			case (a,b):
				if active:
					result = result + int(a) * int(b)

	return result


def do():
	strInput = readInputFile(3)

	print(do1(strInput))
	print(do2(strInput))

	print('done')


do()