# AoC day21

from functools import cache, reduce
from itertools import cycle


def get_player(player, state):
    return (state[1], state[3]) if player else (state[0], state[2])

def update_player(player, state, position, score):
    if player:
        return (state[0], position, state[2], score)
    else:
        return (position, state[1], score, state[3])

@cache
def update_position(position):
    while position > 10:
        position -= 10
    return position

def roll():
    roll = cycle(range(1, 101))
    while True:
        yield sum(next(roll) for _ in range(3))

def part1(player_positions):
    scores = [0, 0]
    player = 0
    for die_number, die in enumerate(roll(), start=1):
        player_positions[player] = update_position(player_positions[player] + die)
        scores[player] += player_positions[player]
        if scores[player] >= 1000:
            print(f'Part1: {die_number * 3 * min(scores)}')
            break
        player = 1 - player

def add(tup, tup2):
    return (tup[0] + tup2[0], tup[1] + tup2[1])

def mul(tup, num):
    return (tup[0] * num, tup[1] * num)

@cache
def quantum(player, state):
    if get_player(player, state)[1] >= 21:
        return (0, 1) if player else (1, 0)

    player = 1 - player
    position, score = get_player(player, state)

    return reduce(add, (mul(quantum(player, update_player(player, state, update_position(position + die), score + update_position(position + die))), roll_map[die]) for die in roll_map))


#with open('test_input') as f:
with open('day21_input') as f:
    data = f.readlines()
    player_positions = [int(data[0][-2]), int(data[1][-2])]
    part1(player_positions)

    player_positions = [int(data[0][-2]), int(data[1][-2])]
    roll_map = {6: 7, 5: 6, 7: 6, 4: 3, 8: 3, 3: 1, 9: 1}
    winner = quantum(1, (player_positions[0],player_positions[1],0,0))
    print(f'Part2: {max(winner[0], winner[1])}')
