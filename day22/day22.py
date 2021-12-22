# AoC day22
import re


def clip(cube_a, cube_b):
    min_x_a, max_x_a, min_y_a, max_y_a, min_z_a, max_z_a = cube_a
    min_x_b, max_x_b, min_y_b, max_y_b, min_z_b, max_z_b = cube_b

    clipped_min_x = max(min_x_a, min_x_b)
    clipped_max_x = min(max_x_a, max_x_b)
    clipped_min_y = max(min_y_a, min_y_b)
    clipped_max_y = min(max_y_a, max_y_b)
    clipped_min_z = max(min_z_a, min_z_b)
    clipped_max_z = min(max_z_a, max_z_b)

    if clipped_min_x > clipped_max_x or clipped_min_y > clipped_max_y or clipped_min_z > clipped_max_z:
        return None

    clipped = clipped_min_x, clipped_max_x, clipped_min_y, clipped_max_y, clipped_min_z, clipped_max_z
    return clipped


def clip_all(clip_cube, cuboid):
    return list(set(clipped for clipped in (clip(cube, clip_cube) for cube in cuboid) if clipped is not None))


def cube_volume(cube):
    min_x, max_x, min_y, max_y, min_z, max_z = cube
    return (max_x + 1 - min_x) * (max_y + 1 - min_y) * (max_z + 1 - min_z)


def sum_volume(cuboid):
    if len(cuboid) == 0:
        return 0
    first, *remainder = cuboid 
    overlaps = clip_all(first, remainder)
    return cube_volume(first) + sum_volume(remainder) - sum_volume(overlaps)


def count_lit_cubes(typed_cuboid):
    if len(typed_cuboid) == 0:
        return 0

    (cube_state, first), *remainder = typed_cuboid
    if cube_state == 'off':
        return count_lit_cubes(remainder)

    overlaps = clip_all(
        first,
        (cube for _, cube in remainder))

    return cube_volume(first) + count_lit_cubes(remainder) - sum_volume(overlaps)


def find_cuboids(data):
    cuboids = []
    for line in data:
        on_off, *coords = format.search(line).groups()
        cuboids.append((on_off, tuple(map(int, coords))))
    return cuboids

#with open('test_input') as f:
with open('day22_input') as f:
    data = [line.strip() for line in f.readlines()]
    format = re.compile(r'(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)')

    cuboids = find_cuboids(data)

    initialization_region = (-50, 50, -50, 50, -50, 50)
    clipped = [(cube_state, clipped_cube)
               for cube_state, clipped_cube in ((cube_state, clip(initialization_region, cube))
                                             for cube_state, cube in cuboids)
               if clipped_cube is not None]

    # part1
    print(f'part1: {count_lit_cubes(clipped)}')
    # part2
    print(f'part2: {count_lit_cubes(cuboids)}')
