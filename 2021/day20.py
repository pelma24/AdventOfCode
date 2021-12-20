from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt
from copy import deepcopy

def do1(enhancement,image):
	extendedImage = prepareImage(image, 10)
	
	newImage = imageEnhancement(extendedImage, enhancement, 2)
				
	return getNumberOfLitPixels(newImage)

def do2(enhancement,image):
	extendedImage = prepareImage(image, 100)
	
	newImage = imageEnhancement(extendedImage, enhancement, 50)
				
	return getNumberOfLitPixels(newImage)

def getNumberOfLitPixels(image):
	litPixels = 0
	for line in image:
		litPixels += len([x for x in line if x == '#'])

	return litPixels

def imageEnhancement(image, enhancement, repetitions):
	for _ in range(repetitions):
		image = enhanceImage(image, enhancement)
		newImage = []
		for lineNumber,line in enumerate(image):
			if lineNumber == 0 or lineNumber == len(image) - 1:
				continue
			newImage.append(line[1:-1])
		image = deepcopy(newImage)
	
	return image

def enhanceImage(image, enhancement):
	newImage = deepcopy(image)

	for lineNumber,line in enumerate(image):
		if lineNumber == 0 or lineNumber == len(image) - 1:
			continue
		for position,_ in enumerate(line):
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
			neighbors.append(image[lineNumber + lineDiff][position + posDiff])

	neighbors = [0 if x == '.' else 1 for x in neighbors]
	return neighbors

def prepareImage(image, additionSize):
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

	enhancement,image = strInput.split('\n\n')
	image = image.split('\n')

	print(do1(enhancement,image))
	print(do2(enhancement,image))

	print('done')


do()