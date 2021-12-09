# aoc Day9

from math import prod
from collections import namedtuple

#with open('test_input', 'r') as f:
with open('day9_input', 'r') as f:
    data = [[int(x) for x in line.strip()] for line in f.readlines()]

    pos = namedtuple('Position', 'x y')

    def get_adjacent(data, x_coord, y_coord):
        result = []
        for x,y in [(x_coord+i,y_coord+j) for i in (-1,0,1) for j in (-1,0,1) if i == 0 or j == 0]:
            if 0 <= y < len(data) and 0 <= x < len(data[0]) and ((x,y) != (x_coord, y_coord)):
                result.append((data[y][x], pos(x,y)))
        return result

    def find_low_points(data):
        return [(val, pos(x,y)) for y,r in enumerate(data) for x,val in enumerate(r) if all([x > val for x,_ in get_adjacent(data, x,y)])]

    def basin_size(data, lp, visited):
        val, co = lp
        points = [p for p in get_adjacent(data, co.x, co.y) if val < p[0] < 9 and p not in visited]
        visited.extend(points)
        for p in points:
            basin_size(data, p, visited)
        return len(visited)

    part1 = sum(lp+1 for lp,_ in find_low_points(data))
    part2 = prod(sorted([basin_size(data, lp, [lp]) for lp in find_low_points(data)])[-3:])

    print(f'{part1=}')
    print(f'{part2=}')
