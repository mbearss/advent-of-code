import re
import numpy as np


def parse_digits(text):
    d = line.strip().split(',')
    return [int(''.join(re.findall(r'\d', x))) for x in d]


def solve(A, B):
    a = (B[0] * A[1, 1] - B[1] * A[1, 0]) / (A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0])
    b = (B[1] * A[0, 0] - B[0] * A[0, 1]) / (A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0])

    if a == int(a) and b == int(b):
        return int(3 * a + b)
    return 0


if __name__ == '__main__':
    part1, part2 = 0, 0
    with open('input.txt') as f:
        A = np.zeros((2, 2))
        B = np.zeros((2, 1))
        row = 0
        for line in f:
            if row == 3:
                part1 += solve(A, B)
                part2 += solve(A, B + 10000000000000)
                row = -1
            elif row == 2:
                B = np.array(parse_digits(line))
            else:
                A[row, 0], A[row, 1] = parse_digits(line)
            row += 1
    part1 += solve(A, B)
    part2 += solve(A, B + 10000000000000)

    print('1:', part1)
    print('2:', part2)
