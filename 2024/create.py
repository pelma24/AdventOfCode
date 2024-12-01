import os
import sys
from pathlib import Path

def createFiles(filepath, filepathInput, filepathExampleInput, day):
    if not Path(filepath).exists():
        with open(filepath, 'w') as f:
            f.writelines(['from HelperFunctions import readInputFile\n', 'from HelperFunctions import readExampleInput\n', 'from HelperFunctions import convertToInt\n\n', 'def do1(splitInput):\n', 
            '\treturn \'done\'\n\n', 'def do2(splitInput):\n', '\treturn \'done\'\n\n', 'def do():\n', f'\tstrInput = readInputFile({day})\n', f'\tstrInput = readExampleInput({day})\n\n',
            '\tprint(do1(strInput))\n', '\tprint(do2(strInput))\n\n', '\tprint(\'done\')\n\n\n', 'do()'])
    if not Path(filepathInput).exists():
        open(filepathInput, 'a').close()
    if not Path(filepathExampleInput).exists():
        open(filepathExampleInput, 'a').close()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        day = sys.argv[1]
    else:
        files = [Path(f).stem for f in os.listdir() if Path(f).is_file()]
        day = max([int(f.replace('day', '')) for f in files if f.startswith('day')], default=0) + 1
        
    filepath = os.path.join(f'day{day}.py')
    filepathInput = os.path.join('Input', f'day{day}.txt')
    filepathExampleInput = os.path.join('Input', f'day{day}_example.txt')
    createFiles(filepath, filepathInput, filepathExampleInput, day)      