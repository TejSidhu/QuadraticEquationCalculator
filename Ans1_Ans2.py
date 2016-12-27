import math

def Answer1(a, b, c):
    part1 = math.sqrt((b ** 2 - (4 * a * c)))
    part2 = -b + part1
    part3 = (part2 / (2 * a))
    return part3


def Answer2(a, b, c):
    part1 = math.sqrt((b ** 2 - (4 * a * c)))
    part2 = -b - part1
    part3 = (part2 / (2 * a))
    return part3