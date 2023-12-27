if __name__ == '__main__':
    with open('input.txt') as f:
        p1, p2 = 0, 0
        g1, g2 = set(), set()
        for line in f:
            line = line.strip()
            if len(line) != 0:
                t = [l for l in line]
                g2.update(t) if len(g1) == 0 else g2.intersection_update(t)
                g1.update(t)
            else:
                p1 += len(g1)
                p2 += len(g2)
                g1, g2 = set(), set()
        p1 += len(g1)
        p2 += len(g2)

    print('1:', p1)
    print('2:', p2)
