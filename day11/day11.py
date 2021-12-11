# aoc Day11

from collections import deque


def neighbors():
    return [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)]

def step(squids):

    flashes = 0
    visited = set()
    ready = deque()

    for x in range(len(squids)):
        for y in range(len(squids[0])):
            squids[x][y] += 1
            if squids[x][y] > 9:
                ready.append((x, y))
                visited.add((x, y))

    while ready:
        x, y = ready.popleft()
        for dx, dy in neighbors():
            if 0 <= x + dx < len(squids) and 0 <= y + dy < len(squids[0]):
                squids[x + dx][y + dy] += 1
                if squids[x + dx][y + dy] > 9 and (x + dx, y + dy) not in visited:
                    ready.append((x + dx, y + dy))
                    visited.add((x + dx, y + dy))

    for x in range(len(squids)):
        for y in range(len(squids[0])):
            if squids[x][y] > 9:
                squids[x][y] = 0  # reset
                flashes += 1

    return flashes

# part1 
#with open('test_input', 'r') as f:
with open('day11_input', 'r') as f:
    data = [list(map(int, line.strip())) for line in f.readlines()]
    part1 = sum(step(data) for _ in range(100))

# part2
with open('day11_input', 'r') as f:
    # reload data
    data = [list(map(int, line.strip())) for line in f.readlines()]

    part2 = 0
    while True:
        if all([all([i == 0 for i in squids]) for squids in data]):
            break
        part2 += 1
        step(data)

print(f'{part1=}')
print(f'{part2=}')
