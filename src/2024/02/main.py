import numpy as np

def is_safe(r):
    x = np.diff(r)
    return -3 <= x.min() <= x.max() <= -1 or 1 <= x.min() <= x.max() <= 3


if __name__ == '__main__':

    records = []
    with open('input.txt') as f:
        for line in f:
            records.append([int(x) for x in line.strip().split()])

    print('1:', sum(is_safe(r) for r in records))

    count = 0
    for r in records:
        for i in range(len(r)):
            if is_safe(r[:i] + r[i+1:]):
                count += 1
                break
    print('2:', count)
