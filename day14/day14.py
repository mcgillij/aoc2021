# aoc Day14

from collections import defaultdict

polymer_template = defaultdict(int)
insert = defaultdict(int)

PART1_INSERTIONS = 10
PART2_INSERTIONS = 40

with open('day14_input', 'r') as f:
#with open('test_input', 'r') as f:
    start_polymers, _, *connections = f.read().splitlines()
    connections = dict(r.split(' -> ') for r in connections)

    for i, j in zip(start_polymers, start_polymers[1:]):
        insert[i + j] += 1
    for k in start_polymers:
        polymer_template[k] += 1

    def process(INSERTIONS):
        for _ in range(INSERTIONS):
            for key, val in insert.copy().items():
                link = connections.get(key)
                insert[key] -= val
                insert[key[0] + link] += val
                insert[link + key[1]] += val
                polymer_template[link] += val

            print(f'Insertions: {_ + 1}: {max(polymer_template.values()) - min(polymer_template.values())}')

# only one at a time since we modify the insert dict
# part1
process(PART1_INSERTIONS)

# part2
#process(PART2_INSERTIONS)
