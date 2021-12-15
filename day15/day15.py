# aoc Day15

import heapq

with open('day15_input', 'r') as f:
#with open('test_input', 'r') as f:
    data = {(x, y): int(value) for y, row in enumerate(f.read().split('\n')) for x, value in enumerate(row)}

    def dijkstra(data, end, start=(0, 0), risk=0):
        q, smallest_risk = [(risk, start)], {start: risk}

        while q:
            risk, (x, y) = heapq.heappop(q)
            if (x, y) == end:
                return risk

            neighbors = [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
            for neighbor in neighbors:
                if neighbor not in data or neighbor in smallest_risk:
                    continue
                current_risk = data[neighbor] + risk
                if current_risk < smallest_risk.get(neighbor, float('inf')):
                    smallest_risk[neighbor] = current_risk
                    heapq.heappush(q, (current_risk, neighbor))


    def find_path(data):
        max_x, max_y = map(max, zip(*data))
        part1 = dijkstra(data, (max_x, max_y))

        new_map = {}
        # generate new map
        for j in range(5): # puzzle expanded to 5x5
            for i in range(5):
                for (x, y), value in data.items():
                    calc_xy = (x + (max_x + 1) * i, y + (max_y + 1) * j)
                    calc_val = value + i + j
                    new_map[calc_xy] = calc_val if calc_val < 10 else calc_val % 9 # roll back to 1

        max_x, max_y = map(max, zip(*new_map))
        part2 = dijkstra(new_map, (max_x, max_y))
        return part1, part2

    part1, part2 = find_path(data)
    print(f'{part1=}')
    print(f'{part2=}')
