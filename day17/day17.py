# AoC day17

from re import findall

with open('day17_input') as f:
#with open('test_input') as f:
    data = f.read().strip()

    x1, x2, y1, y2 = map(int, findall(r'-?\d+', data)) 
    part1 = sum(range(-y1))
    print(f'{part1=}')

    def calc_x(v, p=0): # calc all x values
        while p <= x2:
            yield p >= x1;
            p += v;
            v -= (v > 0)

    def calc_y(v, p=0): # calc all y values
        while p >= y1:
            yield p <= y2; 
            p += v;
            v -= 1

    part2 = sum(any(map(lambda a,b: a&b, calc_x(x), calc_y(y)))
        for x in range(1 + x2) for y in range(y1, -y1))

    print(f'{part2=}')
