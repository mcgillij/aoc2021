# aoc Day10

#with open('test_input', 'r') as f:
with open('day10_input', 'r') as f:
    data = [line.strip() for line in f.readlines()]

    char_pairs = {
            '(': ')',
            '[': ']',
            '{': '}',
            '<': '>'
            }
    start_chars = char_pairs.keys()
    error_points = {
            ')': 3,
            ']': 57,
            '}': 1197,
            '>': 25137 
            }

    part2_error_points = {
            ')': 1,
            ']': 2,
            '}': 3,
            '>': 4 
            }

    part1_score = 0
    part2_scores = []

    for nav_line in data:
        stack = []
        for char in nav_line:
            if char in start_chars:
                stack.append(char_pairs[char])
            elif char in stack[-1]:
                stack.pop()
            else:
                part1_score += error_points[char]
                break
        else: # corrupted line
            part2_score = 0
            while stack:
                part2_score = 5 * part2_score + part2_error_points[stack.pop()]
            part2_scores.append(part2_score)

    part2_scores.sort()

    print(f'{part1_score=}')
    print(f'part2: {part2_scores[len(part2_scores)//2]}')
