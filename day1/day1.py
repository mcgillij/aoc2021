import more_itertools

with open('day1_input', 'r') as f:
    lines = f.readlines()

    window = more_itertools.windowed
    greater = lambda tup: tup[1] > tup[0]
    func = lambda lst: sum(map(greater, window(lst, 2)))

    # part 1
    input_list = list(map(int, (map(str.strip, lines))))
    print(f'part1: {func(input_list)}')

    # part 2
    l = map(sum, window(input_list,3))
    print(f'part2: {func(l)}')
