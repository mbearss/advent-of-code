from functools import cache

import numpy as np


@cache
def dfs(v):
    if dfs.g[v]:
        return sum(dfs(x) for x in dfs.g[v])
    return 1

if __name__ == '__main__':
    a = []
    with open('input.txt') as f:
        for line in f:
            a.append(int(line))
    a.extend([0, max(a) + 3])
    a = np.array(sorted(a))
    d = np.diff(a)
    p1 = np.count_nonzero(d[d==1]) * np.count_nonzero(d[d==3])

    print('1:', p1)

    dfs.g = dict([(x, {y for y in range(x + 1, x + 4) if y in a}) for x in a])
    print('2:', dfs(0))