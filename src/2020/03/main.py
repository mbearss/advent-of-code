import numpy as np

def check(g: list, r: int, d: int) -> int:
    n = 0
    t = 0
    for m in range(0, len(g), d):
        t += g[m][n % len(g[0])]
        n += r
    return t

if __name__ == '__main__':
    g = []
    with open('input.txt') as f:
        for line in f:
            g.append([0 if x == '.' else 1 for x in line.strip()])

    t = [check(g, 3, 1)]
    print('1:', t[0])

    t.extend([check(g, s, 1) for s in [1, 5, 7]])
    t.append(check(g, 1, 2))
    print('2:', np.prod(t))