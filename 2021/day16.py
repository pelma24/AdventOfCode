from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt

hex = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

class Package:
	def __init__(self, version, typeID):
		self.size = 0
		self.number = 0
		self.packages = []
		self.version = version
		self.typeID = typeID
	def setSize(self, size):
		self.size = size
	def getSize(self):
		return self.size
	def setNumber(self, number):
		self.number = number
	def getNumber(self):
		return self.number
	def addPackage(self, package):
		self.packages.append(package)
	def setPackages(self, packages):
		self.packages = packages
	def getPackages(self):
		return self.packages
	def getVersion(self):
		return self.version
	def getTypeID(self):
		return self.typeID

def do1(splitInput):
	binaryStr = ''

	for bit in splitInput:
		binaryStr += hex[bit]

	package = decodePackage(binaryStr)
	
	versions = getAllVersionNumbers(package, [])

	return sum(versions)

def do2(splitInput):
	binaryStr = ''

	for bit in splitInput:
		binaryStr += hex[bit]

	package = decodePackage(binaryStr)

	result = calculateResult(package)

	return result

def getAllVersionNumbers(package, versions):
	versions.append(package.getVersion())

	for subPackage in package.getPackages():
		getAllVersionNumbers(subPackage, versions)
	
	return versions

def calculateResult(package):
	match package.getTypeID():
		case 0:
			result = 0
			for subPackage in package.getPackages():
				result += calculateResult(subPackage)
			return result
		case 1:
			result = 1
			for subPackage in package.getPackages():
				result *= calculateResult(subPackage)
			return result
		case 2:
			values = []
			for subPackage in package.getPackages():
				values.append(calculateResult(subPackage))
			return min(values)
		case 3:
			values = []
			for subPackage in package.getPackages():
				values.append(calculateResult(subPackage))
			return max(values)
		case 4:
			return package.getNumber()
		case 5:
			subPackages = package.getPackages()
			firstValue = calculateResult(subPackages[0])
			secondValue = calculateResult(subPackages[1])
			if firstValue > secondValue:
				return 1
			else:
				return 0
		case 6:
			subPackages = package.getPackages()
			firstValue = calculateResult(subPackages[0])
			secondValue = calculateResult(subPackages[1])
			if firstValue < secondValue:
				return 1
			else:
				return 0
		case 7:
			subPackages = package.getPackages()
			firstValue = calculateResult(subPackages[0])
			secondValue = calculateResult(subPackages[1])
			if firstValue == secondValue:
				return 1
			else:
				return 0
		case _:
			print('TypeID unknown')
			return -1


def decodePackage(binaryStr):
	version = int(binaryStr[0:3], 2)
	typeID = int(binaryStr[3:6], 2)
	package = Package(version, typeID)
	match typeID:
		case 4:
			size,number = decodeLiteral(binaryStr[6:])
			package.setSize(size)
			package.setNumber(number)
		case _:
			lengthType, subPackages = getSubPackages(binaryStr[6:])
			package.setPackages(subPackages)
			size = 7
			if lengthType == 1:
				size += 11
			else:
				size += 15
			for subPackage in subPackages:
				size += subPackage.getSize()
			package.setSize(size)

	return package

def decodeLiteral(binaryStr):
	notEnded = True
	binaryNumber = ''
	position = 0
	numberOfParts = 0
	while notEnded:
		numberOfParts += 1
		firstBit = binaryStr[position]
		position += 1
		if firstBit == '0':
			notEnded = False
		
		binaryNumber += binaryStr[position: (position + 4)]
		position += 4
	
	totalSize = 6 + numberOfParts * 5
	
	return totalSize,int(binaryNumber, 2)

def getSubPackages(binaryStr):
	lengthType = int(binaryStr[0],2)

	packages = []
	match lengthType:
		case 1:
			# number of subpackets
			numberOfPackages = int(binaryStr[1:12], 2)
			position = 12
			for i in range(numberOfPackages):
				package = decodePackage(binaryStr[position:])
				packages.append(package)
				position += package.getSize()
		case 0:
			# length of subpackages
			lengthOfSubpackages = int(binaryStr[1:16], 2)
			position = 16
			while position < 16 + lengthOfSubpackages:
				package = decodePackage(binaryStr[position:])
				packages.append(package)
				position += package.getSize()
	return lengthType, packages

def do():
	strInput = readInputFile(16)

	print(do1(strInput))
	print(do2(strInput))

	print('done')


do()