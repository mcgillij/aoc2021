# AoC day16

from math import prod
from functools import reduce

def binary(hexstr):
    for d in [int(x, base=16) for x in hexstr]:
        for shift in range(3, -1, -1):
            yield (d>>shift)&1

def readn(msg, n):
    B = [next(msg) for i in range(n)]
    return reduce(lambda a,b: (a<<1)|b, B)

def parse_literal(msg):
    consumed = 0
    number = 0
    more_data = True
    while more_data:
        more_data = readn(msg, 1)
        number = (number<<4)|readn(msg, 4)
        consumed += 5
    return consumed, number

def parse_packet(msg):
    version_sum = readn(msg, 3)
    typ = readn(msg, 3)
    consumed = 6
    if typ == 4: ## literals
        b, literal = parse_literal(msg)
        consumed += b
        return consumed, literal, version_sum
    literals = []
    if readn(msg, 1) == 0: ## length type ID
        payload_len = readn(msg, 15)
        consumed += 16
        while payload_len:
            b, literal, s = parse_packet(msg)
            payload_len -= b
            consumed += b
            literals.append(literal)
            version_sum += s
    else:
        sub_packet_count = readn(msg, 11)
        consumed += 12
        for i in range(sub_packet_count):
            b, literal, s = parse_packet(msg)
            consumed += b
            literals.append(literal)
            version_sum += s
    literal = [
            sum,
            prod,
            min,
            max,
            None,
            lambda x: x[0] > x[1],
            lambda x: x[0] < x[1],
            lambda x: x[0] == x[1]
            ][typ](literals)
    return consumed, literal, version_sum

with open('day16_input') as f:
#with open('test_input') as f:
    data = f.readline().strip()
    _, part2, part1 = parse_packet(binary(data))
    print(f'{part1=}')
    print(f'{part2=}')
