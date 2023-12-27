import numpy as np
from scipy import ndimage

SIZE = 25
if __name__ == '__main__':
    g = np.zeros(shape=(SIZE, SIZE, SIZE), dtype=int)
    init = []
    with open('input.txt') as f:
        for line in f:
            init.append([0 if l == '.' else 1 for l in line.strip()])

    for i in range(len(init)):
        for j in range(len(init[0])):
            g[SIZE // 2, i - 1 + SIZE // 2 ,j - 1 + SIZE // 2] = init[i][j]

    fp = np.ones(shape=(3, 3, 3))
    fp[1, 1, 1] = 0

    for i in range(6):
        x = ndimage.generic_filter(g, np.sum, footprint=fp, mode='constant', cval=0)

        temp = np.array(g)
        temp[(g == 1) & ((x < 2) | (x > 3))] = 0
        temp[(g == 0) & (x == 3)] = 1
        g = temp

    print('1:', np.sum(g))

    g = np.zeros(shape=(SIZE, SIZE, SIZE, SIZE), dtype=int)
    for i in range(len(init)):
        for j in range(len(init[0])):
            g[SIZE // 2, SIZE // 2, i - 1 + SIZE // 2 ,j - 1 + SIZE // 2] = init[i][j]

    fp = np.ones(shape=(3, 3, 3, 3))
    fp[1, 1, 1, 1] = 0

    for i in range(6):
        x = ndimage.generic_filter(g, np.sum, footprint=fp, mode='constant', cval=0)

        temp = np.array(g)
        temp[(g == 1) & ((x < 2) | (x > 3))] = 0
        temp[(g == 0) & (x == 3)] = 1
        g = temp

    print('2:', np.sum(g))
