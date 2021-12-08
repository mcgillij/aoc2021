# aoc Day8
from collections import Counter

#with open('test_input', 'r') as f:
with open('day8_input', 'r') as f:
    data = [line.strip().split("|") for line in f.readlines()]
    # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    base_chars = "abcefg cf acdeg acdfg bdcf abdfg abdefg acf abcdefg abcdfg"
    char_mapping = Counter(base_chars)

    map_lookup = {
            sum([*map(char_mapping.get, nums)]): i
            for i, nums in zip(range(10), base_chars.split())
            }

    part1 = part2 = 0

    for display, lights in data:
        # just check for the chars we know the lengths of for part1
        part1 += len([x for x in lights.split() if len(x) in (2, 3, 4, 7)])
        part2_mapping = Counter(display)
        part2 += int(''.join([str(map_lookup[sum([*map(part2_mapping.get, nums)])])
            for nums in lights.split()]))

    print(f'{part1=}')
    print(f'{part2=}')
