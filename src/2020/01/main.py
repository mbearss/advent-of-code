import numpy as np


if __name__ == '__main__':

    reports = set()
    with open('input.txt') as f:
        for line in f:
            reports.add(int(line))

    for i1, r1 in enumerate(reports):
        if 2020 - r1 in reports:
            p1 = r1 * (2020 - r1)
        for i2, r2 in enumerate(reports):
            if i1 == i2:
                continue
            if 2020 - (r1 + r2) in reports:
                p2 = np.prod([r1, r2, 2020 - (r1 + r2)])

    print('1:', p1)
    print('2:', p2)