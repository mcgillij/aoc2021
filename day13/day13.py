# aoc Day13

def fold(coords, folds):
    for direction, number in folds:
        folded_coords = set()
        for x,y in coords:
            if direction == 'x':
                folded_coords.add((x if x < number else 2 * number -x, y))
            else:
                folded_coords.add((x, y if y < number else 2 * number -y))
        coords = folded_coords
    return coords

def part2(coords, folds):
    folded_coords = fold(coords, folds)

    max_x = max(x for x,y in folded_coords)
    max_y = max(y for x,y in folded_coords)

    display = [[' '] * (max_x + 1) for _ in range(max_y + 1)]

    for x, y in folded_coords:
        display[y][x] = '#'

    val = '\n'.join(''.join(row) for row in display)
    print(val)

with open('day13_input', 'r') as f:
#with open('test_input', 'r') as f:
    data = f.read().splitlines()

    coords, folds = set(), []
    for line in data:
        if ',' in line:
            x, y = map(int, line.split(','))
            coords.add((x, y))
        if line.startswith('fold'):
            direction, number = line.split()[-1].split('=')
            folds.append((direction, int(number)))


    part1 = len(fold(coords, folds[:1]))
    print(f'{part1=}')
    print("part2")
    part2(coords, folds)
