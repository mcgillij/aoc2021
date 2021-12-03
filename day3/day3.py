# Day3 aoc
import numpy as np

#with open('test_input', 'r') as f:
with open('day3_input', 'r') as f:
    lines = f.read().splitlines()

    bits = len(lines[0])

    # Part 1
    gamma = 0
    for i in range(bits):
        digit = sum([1 if line[i] == '1' else -1 for line in lines])
        gamma += (digit < 0) << (bits -1 -i)

    print(f'part1: {gamma * (~gamma & (1 << bits) -1)}')

    # Part 2
    splitter = lambda array, target : (array[target], array[~target])

    def get_min_max(array, number):
        flag = 1 << (bits -1 - number)
        zeroes, ones = splitter(array, array & flag == 0) if len(array) > 1 else (array, array)

        return (ones, zeroes) if len(ones) >= len(zeroes) else (zeroes, ones)

    values = np.array([int(line, 2) for line in lines]) # convert to base 2

    oxygen = co2 = values
    for i in range(bits):
        min_value, oxygen = get_min_max(oxygen, i)
        co2, max_value = get_min_max(co2, i)

    print(f'part2: {oxygen[0] * co2[0]}')
