# aoc Day12

from collections import defaultdict

with open('day12_input', 'r') as f:
#with open('test_input', 'r') as f:
    paths = defaultdict(list)
    for source, destination in [line.strip().split('-') for line in f.readlines()]:
        paths[source].append(destination)
        paths[destination].append(source)
    print(paths)

    def pathfinding(cave, visited, one_time):
        if cave == 'end':
            return 1
        if cave.islower():
            visited.add(cave)

        total = 0
        for path in paths[cave]:
            if path not in visited:
                total += pathfinding(path, visited, one_time)

        for path in (path for path in paths[cave] if path in visited and path != 'start'):
            if one_time == ' ':
                total += pathfinding(path, visited, path)
            else:
                total += 0

        if cave != one_time:
            visited.discard(cave)
        return total;


    print(f'Part1: {pathfinding("start", set(), "")}')
    print(f'Part2: {pathfinding("start", set(), " ")}')
