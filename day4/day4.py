# aoc Day4

#draws, *boards=open('test_input').read().split('\n\n')
draws, *boards=open('day4_input').read().split('\n\n')

draws = draws.split(',')
board_check = lambda x, y: 5 * x[y] + x[~y]

card_scores = []
for called_number, board_list in sorted((min(max(draws.index(b[board_check((i // 2, j), i % 2)]) for j in range(5)) for i in range(10)), b) for b in[p.split() for p in boards]):
    # print(called_number, board_list)
    card_scores.append(sum(map(int, set(board_list) - set(draws[:called_number + 1]))) * int(draws[called_number]))

part1_winner, *_the_rest, part2_last_winner = card_scores
print(f'{part1_winner=}, {part2_last_winner=}')
