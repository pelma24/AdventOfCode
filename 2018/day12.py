start = "#.##.##.##.##.......###..####..#....#...#.##...##.#.####...#..##..###...##.#..#.##.#.#.#.#..####..#"

transition = """..### => .
##..# => #
#..## => .
.#..# => .
#.##. => .
#.... => .
##... => #
#...# => .
###.# => #
##.## => .
....# => .
..##. => #
..#.. => .
##.#. => .
.##.# => #
#..#. => #
.##.. => #
###.. => #
.###. => #
##### => #
####. => .
.#.#. => .
...#. => #
#.### => .
.#... => #
.#### => .
#.#.# => #
...## => .
..... => .
.#.## => #
..#.# => #
#.#.. => #"""

addition = 600

import re

def prepareTransitions():
    dic = {}

    splitTransitions = transition.split('\n')

    for entry in splitTransitions:
        match = re.match('(.*) => (.)', entry)
        pattern, result = match.groups()
        dic[pattern] = result

    return dic

def calculateSum(result):
    totalSum = 0
    for i in range(len(result)):
        if result[i] == '#':
            totalSum += i - addition

    return totalSum

def do():
    dic = prepareTransitions()
    
    points = ''
    for i in range(addition):
        points += '.'

    input = points + start + points
    for i in range(20):
        result = '..'
        for index in range(2, len(input) - 2):
            sub = input[index - 2: index + 3]

            result += dic[sub]
        input = result + '..'

        sum = calculateSum(result)


    return sum

print(do())


print(6900 * (50000000000 / 100 - 2) + 16068)