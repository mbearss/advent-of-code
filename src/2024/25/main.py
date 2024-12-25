from itertools import product

import numpy as np

def process_group(q, keys, locks):
    p = np.sum(q[1:-1], axis=0)
    if sum(q[0]) == 0:
        keys.append(p)
    else:
        locks.append(p)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        q = []
        keys = []
        locks = []
        for line in f:
            line = line.strip()
            if line != '':
                q.append([1 if c == '#' else 0 for c in line])
            else:
                process_group(q, keys, locks)
                q = []
        process_group(q, keys, locks)

    row_sums = np.array([row1 + row2 for row1, row2 in product(locks, keys)])
    valid_rows = np.all(row_sums <= 5, axis=1)

    print('1:', np.sum(valid_rows))