import numpy as np
from tqdm import tqdm

directions = np.array([[-1, 0], [0, 1], [1, 0], [0, -1]])

def walk(loc, grid, obs=None):
    f = 0
    visited = np.zeros(shape=grid.shape)
    visited[tuple(loc)] = 1

    state_history = set()
    state_history.add((tuple(loc), f))
    while True:
        next = loc + directions[f]
        if 0 <= next[0] < grid.shape[0] and 0 <= next[1] < grid.shape[1]:
            if grid[tuple(next)] == 0 and tuple(next) != obs:
                loc += directions[f]
                visited[tuple(loc)] = 1

                state = (tuple(loc), f)
                if state in state_history:
                    return -1  # Cycle detected
                state_history.add(state)
            else:
                f = (f + 1) % 4
        else:
            break
    return np.sum(visited, dtype=int)

if __name__ == '__main__':

    grid = []
    with open('input.txt') as f:
        for r, line in enumerate(f):
            grid.append([1 if x == '#' else 0 for x in line.strip()])
            if '^' in line:
                loc = np.array([r, line.index('^')])


    grid = np.array(grid)

    p1 = walk(np.array(loc), grid)
    print('1:', p1)

    count = 0
    for index in tqdm(np.ndindex(grid.shape)):
        if index == tuple(loc):
            continue
        x = walk(np.array(loc), grid, index)
        if x == -1:
            count += 1
    print('2:', count)
