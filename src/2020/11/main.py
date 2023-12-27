import numpy as np
from scipy import ndimage


def print_seats(seats, occupy):
    p = np.full(seats.shape, '.')
    p[seats == 1] = 'L'
    p[occupy == 1] = '#'
    print(p)


if __name__ == '__main__':
    seats = []
    with open('input.txt') as f:
        for line in f:
            seats.append([0 if x == '.' else 1 for x in line.strip()])

    seats = np.array(seats, dtype=int)
    occupy = np.zeros(seats.shape, dtype=int)

    last = -1
    while last != occupy.sum():
        last = occupy.sum()
        temp = np.array(occupy)
        x = ndimage.generic_filter(occupy, np.sum, footprint=np.ones(shape=(3, 3)),
                                   mode='constant', cval=0)
        temp[(occupy == 0) & (seats == 1) & (x == 0)] = 1
        temp[(occupy == 1) & (seats == 1) & (x > 4)] = 0
        occupy = temp

    print('1:', occupy.sum())

    occupy = np.zeros(seats.shape, dtype=int)
    last = -1
    m, n = occupy.shape
    while last != occupy.sum():
        last = occupy.sum()
        temp = np.array(occupy)
        x = np.zeros(seats.shape)
        for r in range(m):
            for c in range(n):
                o = 0
                for k in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    i = np.array([r, c]) + k
                    while 0 <= i[0] < m and 0 <= i[1] < n:
                        if seats[i[0], i[1]] == 1:
                            if occupy[i[0], i[1]] == 1:
                                o += 1
                            break
                        i += k
                x[r, c] = o
        temp[(occupy == 0) & (seats == 1) & (x == 0)] = 1
        temp[(occupy == 1) & (seats == 1) & (x > 4)] = 0
        occupy = temp

    print('2:', occupy.sum())
