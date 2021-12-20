from typing import NewType
from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt
from copy import deepcopy

def do1(enhancement,image):
	extendedImage = prepareImage(image)
	
	newImage = deepcopy(extendedImage)

	for i in range(2):
		newImage = enhanceImage(newImage, enhancement)
		newNewImage = []
		for lineNumber,line in enumerate(newImage):
			if lineNumber == 0 or lineNumber == len(newImage) - 1:
				continue
			newNewImage.append(line[1:-1])
		newImage = deepcopy(newNewImage)
			
	
	litPixels = 0
	for line in newImage:
		litPixels += len([x for x in line if x == '#'])

	return litPixels

def do2(enhancement,image):
	return 'done'

def enhanceImage(image, enhancement):
	newImage = deepcopy(image)

	for lineNumber,line in enumerate(image):
		if lineNumber == 0 or lineNumber == len(image) - 1:
			continue
		for position,pixel in enumerate(line):
			if position == 0 or position == len(line) - 1:
				continue
		
			neighbors = getNeighbors(image, lineNumber, position)
			pixels = ''
			for neighbor in neighbors:
				pixels += str(neighbor)
			index = int(pixels, 2)
			enhancementPixel = enhancement[index]

			newImage[lineNumber][position] = enhancementPixel
	
	return newImage

def getNeighbors(image, lineNumber, position):
	neighbors = []

	for lineDiff in [-1,0,1]:
		for posDiff in [-1,0,1]:
			#if lineNumber + lineDiff < 0  or lineNumber + lineDiff >= len(image) - 1 or position + posDiff < 0 or position + posDiff >= len(image[0]) - 1:
			#	neighbors.append('.')
			#else:
			neighbors.append(image[lineNumber + lineDiff][position + posDiff])

	neighbors = [0 if x == '.' else 1 for x in neighbors]
	return neighbors

def prepareImage(image):
	additionSize = 20
	newImage = []

	emptyLine = ['.' for x in range(additionSize)] + ['.' for x in range(len(image[0]))] + ['.' for x in range(additionSize)]
	for _ in range(additionSize):
		newImage.append(deepcopy(emptyLine))

	for line in image:
		newImage.append(['.' for x in range(additionSize)] + [x for x in line] + ['.' for x in range(additionSize)])
	
	for _ in range(additionSize):
		newImage.append(deepcopy(emptyLine))
	
	return newImage


def do():
	strInput = readInputFile(20)
	#strInput = readExampleInput(20)

	enhancement,image = strInput.split('\n\n')
	image = image.split('\n')

	print(do1(enhancement,image))
	print(do2(enhancement,image))

	print('done')


do()