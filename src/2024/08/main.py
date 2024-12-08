from itertools import combinations

import numpy as np

def run(antenna, part1=True):
    freq = np.unique(antenna[antenna != 0])
    antinodes = np.zeros_like(antenna)
    for a in freq:
        row_indices, col_indices = np.where(antenna == a)
        locs = list(zip(row_indices, col_indices))
        for pairs in combinations(locs, 2):
            x = pairs[0][0] - pairs[1][0]
            y = pairs[0][1] - pairs[1][1]
            z = 2 if part1 else 1
            while True:
                nx, ny = pairs[1][0] + z * x, pairs[1][1] + z * y
                if 0 <= nx < antenna.shape[0] and 0 <= ny < antenna.shape[1]:
                    antinodes[nx, ny] = 1
                else:
                    break
                if part1:
                    break
                z += 1
            z = 2 if part1 else 1
            while True:
                nx, ny = pairs[0][0] - z * x, pairs[0][1] - z * y
                if 0 <= nx < antenna.shape[0] and 0 <= ny < antenna.shape[1]:
                    antinodes[nx, ny] = 1
                else:
                    break
                if part1:
                    break
                z += 1
    return np.sum(antinodes)

if __name__ == '__main__':
    antenna = []
    with open('input.txt') as f:
        for line in f:
            antenna.append([ord(x) if x != '.' else 0 for x in list(line.strip())])

    antenna = np.array(antenna)

    print('1:', run(antenna))
    print('2:', run(antenna, False))