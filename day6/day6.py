# aoc Day6

from collections import Counter

#with open('test_input', 'r') as f:
with open('day6_input', 'r') as f:
    data = f.read()

    part1_fish = Counter(int(i) for i in data.strip().split(','))
    part2_fish = Counter(int(i) for i in data.strip().split(','))

    def spawn_fish(fishes, days):
        for day in range(days):
            f = fishes[0]
            for generation in range(8):
                fishes[generation] = fishes[generation + 1]
            fishes[8] = f
            fishes[6] += f
        return sum(fishes.values())

    print(f'part1: {spawn_fish(part1_fish, 80)}')
    print(f'part2: {spawn_fish(part2_fish, 256)}')
