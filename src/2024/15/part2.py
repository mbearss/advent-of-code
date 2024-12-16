import copy
from collections import deque


def solve(G, instructions, part2):
    R = len(G)
    C = len(G[0])
    if part2:
        NG = []
        for r in range(R):
            row = []
            for c in range(C):
                if G[r][c] == '#':
                    row.append('#')
                    row.append('#')
                if G[r][c] == 'O':
                    row.append('[')
                    row.append(']')
                if G[r][c] == '.':
                    row.append('.')
                    row.append('.')
                if G[r][c] == '@':
                    row.append('@')
                    row.append('.')
            NG.append(row)
        G = NG
        C *= 2

    for r in range(R):
        for c in range(C):
            if G[r][c] == '@':
                sr, sc = r, c
                G[r][c] = '.'

    r, c = sr, sc
    for inst in instructions:
        dr, dc = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}[inst]
        nr, nc = r + dr, c + dc
        if G[nr][nc] == '#':
            continue
        elif G[nr][nc] == '.':
            r, c = nr, nc
        elif G[nr][nc] in ['[', ']', 'O']:
            Q = deque([(r, c)])
            SEEN = set()
            ok = True
            while Q:
                nr, nc = Q.popleft()
                if (nr, nc) in SEEN:
                    continue
                SEEN.add((nr, nc))
                nnr, nnc = nr + dr, nc + dc
                if G[nnr][nnc] == '#':
                    ok = False
                    break
                if G[nnr][nnc] == 'O':
                    Q.append((nnr, nnc))
                if G[nnr][nnc] == '[':
                    Q.append((nnr, nnc))
                    assert G[nnr][nnc + 1] == ']'
                    Q.append((nnr, nnc + 1))
                if G[nnr][nnc] == ']':
                    Q.append((nnr, nnc))
                    assert G[nnr][nnc - 1] == '['
                    Q.append((nnr, nnc - 1))
            if not ok:
                continue
            while len(SEEN) > 0:
                for nr, nc in sorted(SEEN):
                    nnr, nnc = nr + dr, nc + dc
                    if (nnr, nnc) not in SEEN:
                        assert G[nnr][nnc] == '.'
                        G[nnr][nnc] = G[nr][nc]
                        G[nr][nc] = '.'
                        SEEN.remove((nr, nc))
            r = r + dr
            c = c + dc

    ans = 0
    for r in range(R):
        for c in range(C):
            if G[r][c] in ['[', 'O']:
                ans += 100 * r + c
    return ans


if __name__ == "__main__":
    grid = []
    instructions = []

    with open("input.txt") as f:
        for i, line in enumerate(f):
            if "<" in line or ">" in line or "^" in line or "v" in line:
                instructions.extend(line.strip())
            elif len(line.strip()) != 0:
                grid.append(list(line.strip()))

    print('1:', solve(copy.deepcopy(grid), instructions, False))
    print('2:', solve(grid, instructions, True))
