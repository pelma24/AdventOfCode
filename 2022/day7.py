from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt
import re

tree = {}
dirSizes = {}
fileSizes ={}
parentDir = {}

def do1(splitInput):
	buildFileSystemTree(splitInput)
	calculateSizes('/')
	
	smallDirs = sum([value for value in dirSizes.values() if value <= 100000])
	
	return smallDirs

def do2(splitInput):
	unUsedSpace = 70000000 - dirSizes['/']
	neededSpace = 30000000 - unUsedSpace
	possibleDirs = [value for value in dirSizes.values() if value >= neededSpace]
	
	return min(possibleDirs)

def buildFileSystemTree(splitInput):
	currentDirectory = '/'
	for line in splitInput:
		matchCommand = re.match('\$ .+', line)
		if matchCommand:
			match line [2:4]:
				case 'cd':
					match line[5:]:
						case '..':
							currentDirectory = parentDir[currentDirectory]
						case '/':
							currentDirectory = '/'
						case _:
							currentDirectory = currentDirectory + '/' + line[5:]
				case 'ls':
					tree[currentDirectory] = []
		else:
			matchFolder = re.match('dir .+', line)
			if matchFolder:
				folder = line[4:]
				tree[currentDirectory].append(currentDirectory + '/' + folder)
				parentDir[currentDirectory + '/' + folder] = currentDirectory
			else:
				matchFile = re.match('(?P<size>\d+) (?P<name>\D+)', line)
				size = int(matchFile.group('size'))
				name = matchFile.group('name')
				tree[currentDirectory].append(currentDirectory + '/' + name)
				fileSizes[currentDirectory + '/' + name] = size

def calculateSizes(key):
	if key in fileSizes.keys():
		return fileSizes[key]
	else:
		dirSizes[key] = 0
		for child in tree[key]:
			dirSizes[key] += calculateSizes(child)
		return dirSizes[key]

def do():
	strInput = readInputFile(7)

	splitInput = strInput.split('\n')

	print(do1(splitInput))
	print(do2(splitInput))

	print('done')


do()