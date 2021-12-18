# AoC day18

with open('day18_input') as f:
#with open('test_input') as f:
    data = [list(i) for i in f.read().splitlines()]

    #filter non number characters
    NAN = (',', '[', ']')

    def explode(item, data):

        for x in range(item - 2, -1, -1):
            if data[x] not in NAN:
                data[x] = str(int(data[x]) + int(data[item]))
                break

        for y in range(item + 3, len(data)):
            if data[y] not in NAN:
                data[y] = str(int(data[y]) + int(data[item+2]))
                break

        return data[:item - 1] + ['0'] + data[item + 4:]

    def split_pair(data):
        for i in range(len(data)):
            if data[i] not in NAN and int(data[i]) >= 10:
                x = str(int(data[i]) // 2)
                y = str((int(data[i]) + 1) // 2)
                data = data[:i] + ['['] + [x] + [','] + [y] + [']'] + data[i + 1:]
                return True, data
        return False, data

    def check_explode(data):
        depth = 0
        for i in range(len(data)):
            if depth == 5:
                return True, explode(i, data)
            if data[i] == '[':
                depth += 1
            elif data[i] == ']':
                depth -= 1
        return False, data

    def addition(x, y):
        return ['['] + x + [','] + y + [']']

    def magnitude(data):
        if type(data) == int:
            return data
        return 3 * magnitude(data[0]) + 2 * magnitude(data[1])

    def add_all(data):
        line = data[0]
        for rest in data[1:]:
            line = addition(line, rest)
            while True:
                exploded = True
                while exploded:
                    exploded, line = check_explode(line)
                split, line = split_pair(line)
                if not split:
                    break
        return line

    # part 1
    pairs = eval(''.join(add_all(data)))
    part1 = magnitude(pairs)
    print(f'{part1=}')

    # part 2
    part2 = 0
    for i in data:
        for j in data:
            l = eval(''.join(add_all([i, j])))
            part2 = max(magnitude(l), part2)

    print(f'{part2=}')
