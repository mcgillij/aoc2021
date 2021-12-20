# AoC day20

from collections import defaultdict

#with open('test_input') as f:
with open('day20_input') as f:
    enhancement, image = f.read().split('\n\n')
    image = {(x, y): int(value == '#') for x, line in enumerate(image.split('\n')) for y, value in enumerate(line)}

    grid_neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]

    def neighbors(image):
        return {(x + dx, y + dy) for x, y in image for dy, dx in grid_neighbors}

    def enhance(image, steps):
        new_image = None
        for k in range(steps):
            new_image = defaultdict(bool)
            for i, j in neighbors(image):
                binary_string = ''
                for dx, dy in grid_neighbors:
                    binary_string += str(image.get((i + dx, j + dy), '01'[k % 2] if enhancement[0] == '#' else '0'))
                new_image[(i, j)] = int(enhancement[int(binary_string, 2)] == '#')
            image = new_image
        return new_image


    part1 = sum(enhance(image, 2).values())
    print(f'{part1=}')
    part2 = sum(enhance(image, 50).values())
    print(f'{part2=}')
