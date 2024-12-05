import numpy as np
from scipy import ndimage

def weighted_sum(values):
    if len(values) == 4:
        return np.sum(values * [1, 10, 100, 1000])
    else:
        return np.sum(values * [1, 10, 100, 1000, 10000])

if __name__ == '__main__':

    records = []
    with open('input.txt') as f:
        grid = np.array([[ord(char) for char in row.strip()] for row in f])

    locs = np.zeros(shape=grid.shape)
    for f in (np.ones((1, 4)), np.ones((4, 1)), np.eye(4), np.rot90(np.eye(4))):
        x = ndimage.generic_filter(grid, weighted_sum, footprint=f, mode='constant')
        locs += (x == 90358) | (x == 96433)

    print('1:', np.sum(locs, dtype=int))

    x = ndimage.generic_filter(grid, weighted_sum,
                               footprint=np.array([[1, 0, 1],
                                                  [0, 1, 0],
                                                  [1, 0, 1]]), mode='constant')

    locs = (x == 920347) | (x == 914407) | (x == 860353) | (x == 854413)
    print('2:', np.sum(locs, dtype=int))
