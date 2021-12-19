# AoC day19

def get_scanners():
    scanners = []
    with open("day19_input") as f:
    #with open("test_input") as f:
        for line in f.read().splitlines():
            if '---' in line:
                scanners.append([])
            elif line.strip():
                scanners[-1].append(tuple(map(int, line.split(','))))
        return scanners


def reorient(position, axis1, sign1, axis2, sign2):
    axis3 = 3 - (axis1 + axis2)
    sign3 = 1 if (((axis2 - axis1) % 3 == 1) ^ (sign1 != sign2)) else -1
    return (position[axis1] * sign1, position[axis2] * sign2, position[axis3] * sign3)


def diffs(positions):
    return [
        (x1 - x, y1 - y, z1 - z)
        for (x, y, z), (x1, y1, z1)
        in zip (positions, positions[1:])
    ]


def align(known_beacons, unaligned_beacons):
    for axis in range(3):
        known_sorted = sorted(known_beacons, key = lambda position: position[axis])
        unaligned_beacons.sort(key = lambda position: position[axis])
        known_diffs = diffs(known_sorted)
        unaligned_diffs = diffs(unaligned_beacons)
        intersection = set(known_diffs) & set(unaligned_diffs)
        if intersection:
            diff = intersection.pop()
            kx, ky, kz = known_sorted[known_diffs.index(diff)]
            ux, uy, uz = unaligned_beacons[unaligned_diffs.index(diff)]
            ox, oy, oz = (ux - kx, uy - ky, uz - kz)
            moved = {(x - ox, y - oy, z - oz) for (x, y, z) in unaligned_beacons}
            matches = known_beacons & moved
            if len(matches) >= 12:
                return moved, (ox, oy, oz)
    return None, None


def orient_and_align(known_beacons, readings):
    for axis1 in range(3):
        for sign1 in [1, -1]:
            for axis2 in {0, 1, 2} - {axis1}:
                for sign2 in [1, -1]:
                    orientation = (axis1, sign1, axis2, sign2)
                    unaligned_beacons = [reorient(reading, *orientation)
                                         for reading in readings]
                    aligned_beacons, scanner_pos = align(known_beacons, unaligned_beacons)
                    if aligned_beacons:
                        return aligned_beacons, scanner_pos
    return None, None


def orient_all(known_beacons, known_scanners, unaligned_readings):
    while unaligned_readings:
        progress = False
        for readings in list(unaligned_readings):
            beacons, scanner_pos = orient_and_align(known_beacons, readings)
            if beacons:
                unaligned_readings.remove(readings)
                known_beacons |= beacons
                known_scanners.append(scanner_pos)
                progress = True


def solve():
    scanner_readings = get_scanners()
    known_scanners = [(0, 0, 0)]
    known_beacons = set(scanner_readings[0])
    unaligned_readings = scanner_readings[1:]

    orient_all(known_beacons, known_scanners, unaligned_readings)
    beacons = len(known_beacons)

    max_distance = 0 # max distance
    for x0, y0, z0 in known_scanners:
        for x1, y1, z1 in known_scanners:
            dist = abs(x1 - x0) + abs(y1 - y0) + abs(z1 - z0)
            max_distance = max(dist, max_distance)
    return beacons, max_distance


part1, part2 = solve()
print(f'{part1=}')
print(f'{part2=}')
