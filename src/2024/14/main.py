import numpy as np

grid = (101, 103)

def sim(P, V):
    P += V
    P[:, 0] %= grid[0]
    P[:, 1] %= grid[1]

def draw_grid(P, draw=False):
    g = np.zeros(shape=grid, dtype=int)
    for p in P:
        g[tuple(p)] += 1

    if draw:
        transposed_grid = g.T
        for row in transposed_grid:
            print("".join(str(cell) if cell != 0 else '.' for cell in row))

    q1 = np.sum(g[0:grid[0]//2, 0:grid[1]//2])
    q2 = np.sum(g[grid[0] // 2+1:, 0:grid[1] // 2])
    q3 = np.sum(g[grid[0] // 2+1:, grid[1] // 2+1:])
    q4 = np.sum(g[0:grid[0] // 2, grid[1] // 2+1:])
    return q1 * q2 * q3 * q4

def check_unique(P):
    unique_rows = np.unique(P, axis=0)
    return unique_rows.shape[0] == P.shape[0]


if __name__ == '__main__':
    pos, vel = [], []
    with open('input.txt') as f:
        for line in f:
            p, v = [x[2:].split(',') for x in line.strip().split()]
            pos.append([int(x) for x in p])
            vel.append([int(x) for x in v])

    pos = np.array(pos)
    vel = np.array(vel)

    # assume easter egg is after 100
    for _ in range(100):
        sim(pos, vel)
    print('1:', draw_grid(pos))

    i = 100
    while not check_unique(pos):
        sim(pos, vel)
        i += 1

    draw_grid(pos, draw=False)
    print('2:', i)
