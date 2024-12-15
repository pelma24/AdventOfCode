from HelperFunctions import readInputFile
from HelperFunctions import readExampleInput
from HelperFunctions import convertToInt
import re

def extractInput(strInput):
	machines = {}
	for count,input in enumerate(strInput.split('\n\n')):
		a,b,p = input.split('\n')
		matchA = re.search('Button A: X\+(\d+), Y\+(\d+)', a)
		ax,ay = convertToInt(matchA.groups())
		matchB = re.search('Button B: X\+(\d+), Y\+(\d+)', b)
		bx,by = convertToInt(matchB.groups())
		matchP = re.search('Prize: X=(\d+), Y=(\d+)', p)
		px,py = convertToInt(matchP.groups())
		machines[count] = {'A': (ax,ay), 'B': (bx,by), 'Prize': (px,py)}
	
	return machines

def do1(machines):
	
	totalPrize = 0
	for machine in machines.values():
		ax,ay = machine['A']
		bx,by = machine['B']
		px,py = machine['Prize']

		pushA = (px*by - py*bx) / (ax*by - ay*bx)
		pushB = (py - pushA * ay) / by

		if pushA.is_integer() and pushB.is_integer():
			prize = pushA * 3 + pushB
			totalPrize += prize
	
	return totalPrize

def do2(machines):
	
	totalPrize = 0
	for machine in machines.values():
		ax,ay = machine['A']
		bx,by = machine['B']
		px,py = machine['Prize']
		px = px + 10000000000000
		py = py + 10000000000000

		pushA = (px*by - py*bx) / (ax*by - ay*bx)
		pushB = (py - pushA * ay) / by

		if pushA.is_integer() and pushB.is_integer():
			prize = pushA * 3 + pushB
			totalPrize += prize
	
	return totalPrize

def do():
	strInput = readInputFile(13)

	machines = extractInput(strInput)

	print(do1(machines))
	print(do2(machines))

	print('done')


do()