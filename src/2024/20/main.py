from collections import defaultdict
from itertools import combinations

import numpy as np

def run(grid, start, part2=False):
    dist = {start: 0}
    q = [start]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    rows = len(grid)
    cols = len(grid[0])

    for pos in q:
        for dx, dy in directions:
            new = (pos[0] + dx, pos[1] + dy)

            if 0 <= new[0] < rows and 0 <= new[1] < cols:
                if not grid[new[0]][new[1]] and new not in dist:
                    dist[new] = dist[pos] + 1
                    q.append(new)

    pairs = list(combinations(dist.items(), 2))

    cheats = defaultdict(int)
    for pair in pairs:
        m_dist = abs(pair[0][0][0] - pair[1][0][0]) + abs(pair[0][0][1] - pair[1][0][1])

        if 2 <= m_dist <= 20 and part2 or m_dist == 2:
            a_dist = abs(pair[0][1] - pair[1][1]) - m_dist
            cheats[a_dist] += 1

    return sum(value for key, value in cheats.items() if key >= 100)

if __name__ == '__main__':
    grid = []
    start, goal = None, None
    with open('input.txt') as f:
        for i, line in enumerate(f):
            grid.append([1 if x == '#' else 0 for x in list(line.strip())])
            if 'S' in line:
                start = (i, line.index('S'))
            if 'E' in line:
                goal = (i, line.index('E'))

    grid = np.array(grid, dtype=bool)

    print('1:', run(grid, start))
    print('2:', run(grid, start, part2=True))

