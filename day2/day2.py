from collections import namedtuple

#with open('test_input', 'r') as f:
with open('day2_input', 'r') as f:
    lines = f.readlines()
    input_list = list((map(str.strip, lines)))
    command_list = [(command, int(count)) for command, count in (line.split(' ') for line in input_list)]

    # Part 1
    pos = namedtuple('Position', ['x', 'y'])
    sub_position = pos(0, 0)
    print(sub_position)

    for command, count in command_list:
        match command:
            case 'up':
                sub_position = pos(sub_position.x, sub_position.y - count)
            case 'down':
                sub_position = pos(sub_position.x, sub_position.y + count)
            case 'forward':
                sub_position = pos(sub_position.x + count, sub_position.y)

    print(f'part1: {sub_position}')
    print(f'results: {sub_position.x * sub_position.y}')

    # Part 2
    pos = namedtuple('Position', ['x', 'y', 'aim'])
    sub_position = pos(0, 0, 0)
    print(sub_position)

    for command, count in command_list:
        match command:
            case 'up':
                sub_position = pos(sub_position.x, sub_position.y, sub_position.aim - count)
            case 'down':
                sub_position = pos(sub_position.x, sub_position.y, sub_position.aim + count)
            case 'forward':
                sub_position = pos(sub_position.x + count, sub_position.y + sub_position.aim * count, sub_position.aim)

    print(f'part2: {sub_position}')
    print(f'results: {sub_position.x * sub_position.y}')
