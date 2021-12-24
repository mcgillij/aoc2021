# AoC day 24

from collections import defaultdict, Counter
from functools import lru_cache
import itertools
import math
import string


BLOCK_SIZE = 18

@lru_cache
def eval_block(block, digit, z0):
    """Evaluates a single block with a given digit and z0, determining the z0 afterwards"""
    x = 0 if ((z0 % 26) + int(block[5][2])) == digit else 1
    z = z0 // int(block[4][2])
    z1 = z * ((25 * x) + 1)
    z2 = z1 + (x * (digit + int(block[15][2])))
    return z2

@lru_cache
def solve(prog, idx, z0, rb):
    """Recursively determines the largest sequence of digits necessary to run the rest of the program with z = z0 to start, and ending with z = 0"""
    if idx + BLOCK_SIZE >= len(prog):
        for i in range(9, 0, -1):
            if eval_block(prog[idx:], i, z0) == 0:
                return i
        return 0
    else:
        if prog[idx + 4][2] == "1":
            # inc block
            rng = range(9, 0, -1)
        else:
            # dec block
            x = z0 % 26
            x += int(prog[idx + 5][2])
            if x <= 0 or x > 9:
                return 0
            rng = range(x, x + 1)
        for i in rng:
            val = int(prog[idx + 5][2])
            res = solve(prog, idx + BLOCK_SIZE, eval_block(prog[idx:idx + BLOCK_SIZE], i, z0), rb - 1)
            if res > 0:
                return (i * (10 ** rb)) + res
        return 0
    return 0


@lru_cache
def solve2(prog, idx, z0, rb):
    """Recursively determines the smallest sequence of digits necessary to run the rest of the program with z = z0 to start, and ending with z = 0"""
    if idx + BLOCK_SIZE >= len(prog):
        for i in range(1, 10):
            if eval_block(prog[idx:], i, z0) == 0:
                return i
        return 0
    else:
        if prog[idx + 4][2] == "1":
            # inc block
            rng = range(1, 10)
        else:
            # dec block
            x = z0 % 26
            x += int(prog[idx + 5][2])
            if x <= 0 or x > 9:
                return 0
            rng = range(x, x + 1)
        for i in rng:
            val = int(prog[idx + 5][2])
            res = solve2(prog, idx + BLOCK_SIZE, eval_block(prog[idx:idx + BLOCK_SIZE], i, z0), rb - 1)
            if res > 0:
                return (i * (10 ** rb)) + res
        return 0
    return 0


#with open('test_input') as f:
with open('day24_input') as f:
    data = tuple([tuple(line.strip().split()) for line in f.readlines()])

    part1 = solve(data, 0, 0, 13)
    part2 = solve2(data, 0, 0, 13)
    print(f'{part1=}')
    print(f'{part2=}')
