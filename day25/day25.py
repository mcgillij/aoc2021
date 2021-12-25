# AoC day 25

#with open('test_input') as f:
with open('day25_input') as f:
    data = [list(line.strip()) for line in f.readlines()]

    east = set()
    south = set()

    length = len(data[0])
    height = len(data)

    for y, char_list in enumerate(data):
        for x, char in enumerate(char_list):
            if char == ">":
                east.add((x, y))
            elif char == "v":
                south.add((x, y))

    part1 = 0
    while True:
        new_east = set()
        new_south = set()

        for e in east:
            coords = ((e[0] + 1) % length, e[1])
            if coords not in east and coords not in south:
                new_east.add(coords)
            else:
                new_east.add(e)

        for s in south:
            coords = (s[0], (s[1] + 1) % height)
            if coords not in south and coords not in new_east:
                new_south.add(coords)
            else:
                new_south.add(s)

        part1 += 1

        if new_south == south and east == new_east:
            break

        east = new_east
        south = new_south

    print(f'{part1=}')
    print('no part 2 for xmas! Sleigh launched!')
