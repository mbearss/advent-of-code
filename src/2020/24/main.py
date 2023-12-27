from collections import defaultdict


if __name__ == '__main__':
    tiles = defaultdict(bool)
    with open('input.txt') as f:
        for line in f:
            line = list(line.rstrip())
            q, r, s = 0, 0, 0
            while len(line) > 0:
                f = line.pop(0)
                if f == 'e':
                    q += 1
                    s -= 1
                elif f == 'w':
                    q -= 1
                    s += 1
                else:
                    f += line.pop(0)
                    if f == 'se':
                        r += 1
                        s -= 1
                    elif f == 'ne':
                        q += 1
                        r -= 1
                    elif f == 'sw':
                        q -= 1
                        r += 1
                    elif f == 'nw':
                        r -= 1
                        s += 1
            tiles[(q, r, s)] = not tiles[(q, r, s)]

    p1 = 0
    for k, v in tiles.items():
        if v:
            p1 += 1
    print('1:', p1)

    neighbors = [(1, 0, -1), (-1, 0, 1), (0, -1, 1), (0, 1, -1), (-1, 1, 0), (1, -1, 0)]
    for d in range(100):
        next = tiles.copy()
        for k, v in tiles.items():
            if v:
                for n in neighbors:
                    qrs = tuple(sum(x) for x in zip(k,n))
                    if qrs not in tiles:
                        next[qrs] = False

        tiles = next.copy()
        for k, v in tiles.items():
            nc = 0
            for n in neighbors:
                qrs = tuple(sum(x) for x in zip(k,n))
                if qrs in tiles and tiles[qrs]:
                    nc += 1

            if v and (nc == 0 or nc > 2):
                next[k] = False
            if not v and nc == 2:
                next[k] = True
        tiles = next

    p2 = 0
    for k, v in tiles.items():
        if v:
            p2 += 1
    print('2:', p2)
