# aoc Day7

from statistics import mean, median

#with open('test_input', 'r') as f:
with open('day7_input', 'r') as f:
    crab_positions = list(map(int, f.read().strip().split(',')))

    median_distance = int(median(crab_positions))
    mean_distance = int(mean(crab_positions))

    fuel_for_part1 = fuel_for_part2 = 0
    part2_choices = [0, 0, 0]

    for crab in crab_positions:
        fuel_for_part1 += (crab - median_distance)

        #hacky way to get the closest distance to the mean
        part2_choices[0] += sum([i for i in range(1, abs(crab - mean_distance) + 1)])
        part2_choices[1] += sum([i for i in range(1, abs(crab - mean_distance + 1) + 1)])
        part2_choices[2] += sum([i for i in range(1, abs(crab - mean_distance - 1) + 1)])
        fuel_for_part2 = min(part2_choices)

    print(f'{fuel_for_part1=}')
    print(f'{fuel_for_part2=}')
