from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt

def prepareDisk(strInput):
	disk1 = []
	disk2 = []
	id = 0
	freeSpace = False
	for number in strInput:
		number = int(number)
		if freeSpace:
			for _ in range(number):
				disk1.append('.')
			if number != 0:
				disk2.append(('.', number))
			freeSpace = False
		else:
			for _ in range(number):
				disk1.append(id)
			disk2.append((id, number))			
			id = id + 1
			freeSpace = True

	return disk1, disk2

def move(disk, movingPart, pos):
	id,size = movingPart
	for position,part in enumerate(disk):
		if position > pos:
			break
		match part:
			case ('.', freeSize) if freeSize > size:
				disk[pos] = ('.', size)
				disk = disk[0:position] + [(id, size)] + [('.', freeSize - size)] + disk[position + 1:]
				return disk
			case ('.', freeSize) if freeSize == size:
				disk[position] = (id, size)
				disk[pos] = ('.', size)
				return disk
			case _:
				continue

	return disk

def do1(disk):

	pos = 0
	while pos < len(disk):
		if disk[pos] != '.':
			pos = pos + 1
			continue
		while True:
			newValue = disk.pop(len(disk) - 1)
			if newValue == '.':
				continue
			break
		disk[pos] = newValue
		pos = pos + 1

	return sum([pos * value for pos,value in enumerate(disk) if value != '.'])

def do2(disk):
	alreadyMoved = set()
	pos = len(disk) - 1
	while pos > 0:
		match(disk[pos]):
			case ('.', _):
				pos = pos - 1
				continue
			case (id, size) if id not in alreadyMoved:
				disk = move(disk, (id, size), pos)
				alreadyMoved.add(id)
				pos = len(disk) - 1
			case _:
				pos = pos - 1
				continue

	checksum = 0
	position = 0
	for id,size in disk:
		if id == '.':
			position = position + size
			continue
		for i in range(size):
			checksum = checksum + id * (position + i)
		position = position + size
	
	return checksum

def do():
	strInput = readInputFile(9)

	disk1,disk2 = prepareDisk(strInput)
	print(do1(disk1))
	print(do2(disk2))

	print('done')


do()