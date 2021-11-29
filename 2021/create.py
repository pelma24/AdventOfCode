import os
import sys

def createFiles(filepath, filepathInput, day):
    with open(filepath, 'w') as f:
        f.writelines(['from HelperFunctions import readInputFile\n', 'from HelperFunctions import convertToInt\n\n', 'def do1(splitInput):\n', 
        '\tprint(\'done\')\n\n', 'def do2(splitInput):\n', '\tprint(\'done\')\n\n', 'def do():\n', f'\tstrInput = readInputFile({day})\n\n', 
        '\tdo1(strInput)\n', '\tdo2(strInput)\n\n', '\tprint(\'done\')\n\n\n', 'do()'])
    open(filepathInput, 'a').close()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        day = sys.argv[1]
        filepath = os.path.join(f'day{day}.py')
        filepathInput = os.path.join('Input', f'day{day}.txt')
        createFiles(filepath, filepathInput, day)
        