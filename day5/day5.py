# aoc Day5

import re
from collections import Counter

#with open('test_input', 'r') as f:
#    data = f.read()

with open('day5_input', 'r') as f:
    data = f.read()

def graph(data, diagonal=False):
    lines = re.findall('(\d+),(\d+) -> (\d+),(\d+)', data)
    points = Counter()
    for line in lines:
        x1, y1, x2, y2 = map(int, line)
        if not diagonal and x1 != x2 and y1 != y2:
            continue
        dx, dy = x2 - x1, y2 - y1
        length = max(abs(dx), abs(dy))
        x_step, y_step = dx//length, dy//length
        points.update((x1 + i*x_step, y1 + i*y_step) for i in range(length+1))
    return sum(count > 1 for count in points.values())


print(f'Part 1: {graph(data, diagonal=False)}')
print(f'Part 2: {graph(data, diagonal=True)}')
